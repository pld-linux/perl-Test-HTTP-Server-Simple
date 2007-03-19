#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	HTTP-Server-Simple
Summary:	Basic test functions for HTTP::Server::Simple
Summary(pl.UTF-8):	Podstawowe funkcje testowe modułu HTTP::Server:Simple
Name:		perl-Test-HTTP-Server-Simple
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/G/GL/GLASSER/Test-HTTP-Server-Simple-%{version}.tar.gz
# Source0-md5:	bb23602669311fa2dd5a61bfc01e05dd
URL:		http://search.cpan.org/dist/Test-HTTP-Server-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Server-Simple
BuildRequires:	perl-Test-Builder-Tester >= 1.01
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/HTTP/Server/*.pm
%{_mandir}/man3/*
