%define modname	Test-Number-Delta
%define modver 1.06

Summary:	Test-Number-Delta - Perl module
Name:		perl-%{modname}
Version:	%{modver}
Release:	5
License:	Artistic
Group:		Development/Perl
Url:		https://github.com/dagolden/Test-Number-Delta
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-Number-Delta-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl-devel

%description
Test::Number::Delta compare the difference between numbers against a given
tolerance.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::Number::Delta.*
