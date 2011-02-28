%define upstream_name    Parse-Eyapp
%define upstream_version 1.181

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2
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

