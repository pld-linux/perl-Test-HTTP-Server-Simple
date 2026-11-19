#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	HTTP-Server-Simple
Summary:	Basic test functions for HTTP::Server::Simple
Summary(pl.UTF-8):	Podstawowe funkcje testowe modułu HTTP::Server:Simple
Name:		perl-Test-HTTP-Server-Simple
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/A/AL/ALEXMV/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b46cd262f054fa51685b551ff55b5dfd
URL:		http://search.cpan.org/dist/Test-HTTP-Server-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Server-Simple
BuildRequires:	perl-Test-Builder-Tester >= 1.04
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This mixin class provides methods to test an
HTTP::Server::Simple-based web server. Currently, it provides only one
such method: started_ok.

%description -l pl.UTF-8
Zestaw klas zawierających metody testowe serwera WWW bazującego na
module HTTP::Server::Simple. Obecnie dostępna jest tylko jedna taka
metoda: started_ok.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/HTTP/Server
%{_mandir}/man3/*
