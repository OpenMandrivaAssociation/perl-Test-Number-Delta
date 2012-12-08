%define upstream_name    Test-Number-Delta
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Test-Number-Delta - Perl module
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Test::Number::Delta compare the difference between numbers against a given
tolerance.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-4mdv2012.0
+ Revision: 765731
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-3
+ Revision: 764248
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-2
+ Revision: 667338
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 405588
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2009.0
+ Revision: 224137
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 10 2007 Thierry Vignaud <tv@mandriva.org> 1.03-1mdv2008.1
+ Revision: 96736
- import perl-Test-Number-Delta


* Wed Oct 10 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.03-1mdv2008.1
- Initial build.
