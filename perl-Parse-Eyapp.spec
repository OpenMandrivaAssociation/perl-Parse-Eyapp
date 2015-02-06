%define upstream_name    Parse-Eyapp
%define upstream_version 1.181

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4
Summary:    Bottom up parser generator
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dumper)
BuildRequires: perl(List::Util)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Parse::Eyapp (Extended yapp) is a collection of modules that extends Francois
Desarmenien Parse::Yapp 1.05. Eyapp extends yacc/yapp syntax with
functionalities like named attributes, EBNF-like expressions, modifiable
default action (like Parse::RecDescent autoaction), grammar reuse, automatic
abstract syntax tree building, syntax directed data generation, translation
schemes, tree regular expressions, tree transformations, scope analysis
support, directed acyclic graphs and a few more.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/eyapp
%{_bindir}/treereg
%{perl_vendorlib}/Parse



%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.181.0-2mdv2011.0
+ Revision: 640778
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.181.0-1
+ Revision: 638935
- update to new version 1.181

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.179.0-1
+ Revision: 635208
- update to new version 1.179

* Tue Jan 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.178.0-1mdv2011.0
+ Revision: 628596
- update to new version 1.178

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.176.0-1mdv2011.0
+ Revision: 625278
- update to new version 1.176
- update to new version 1.174

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.172.0-1mdv2011.0
+ Revision: 612251
- update to new version 1.172

* Mon Nov 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.171.0-1mdv2011.0
+ Revision: 602980
- new version

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 594367
- update to new version 1.170

* Sun Jul 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.165.0-1mdv2011.0
+ Revision: 558807
- new version

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.164.0-1mdv2011.0
+ Revision: 553972
- update to 1.164

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.163.0-1mdv2011.0
+ Revision: 552533
- update to 1.163

* Sun Apr 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.1
+ Revision: 536210
- update to 1.160

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 1.158.0-1mdv2010.1
+ Revision: 530266
- update to 1.158

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.157.0-1mdv2010.1
+ Revision: 508994
- new version

* Sun Jan 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.154.0-1mdv2010.1
+ Revision: 492672
- import perl-Parse-Eyapp


* Sun Jan 17 2010 cpan2dist 1.154-1mdv
- initial mdv release, generated with cpan2dist
