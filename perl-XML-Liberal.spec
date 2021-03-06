#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	XML
%define	pnam	Liberal
Summary:	XML::Liberal - Super liberal XML parser that parses broken XML
Summary(pl.UTF-8):	XML::Liberal - bardzo liberalny analizator XML analizujący uszkodzony XML
Name:		perl-XML-Liberal
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f90276d4080cdf3b4712a3b843a4f9ef
URL:		http://search.cpan.org/dist/XML-Liberal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-HTML-Entities-Numbered >= 0.04
BuildRequires:	perl-Module-Pluggable-Fast >= 0.16
BuildRequires:	perl-XML-LibXML >= 1.58
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Liberal is a super liberal XML parser that can fix broken XML
stream and create a DOM node out of it.

%description -l pl.UTF-8
XML::Liberal to bardzo liberalny analizator XML potrafiący naprawić
uszkodzony strumień XML i utworzyć z niego węzeł DOM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/XML/*.pm
%{perl_vendorlib}/XML/Liberal
%{_mandir}/man3/*
