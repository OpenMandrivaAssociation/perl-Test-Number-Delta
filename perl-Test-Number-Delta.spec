%define pkgname Test-Number-Delta

Name:      perl-Test-Number-Delta
Summary:   Test-Number-Delta - Perl module
Version:   1.03
Release:   %mkrel 2
License:   Artistic
Group:     Development/Perl
URL:       http://www.cpan.org
Buildroot: %{_tmppath}/%{name}-%{version}
Buildarch: noarch
Source:    http://search.cpan.org//CPAN/authors/id/D/DA/DAGOLDEN/Test-Number-Delta-1.03.tar.gz

%description
Test::Number::Delta compare the difference between numbers against a given
tolerance.


%prep
%setup -q -n %{pkgname}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{perl_vendorlib}/Test
%_mandir/man3/Test::Number::Delta.*

