#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	Tree
Summary:	HTML::Tree Perl module
Summary(cs):	Modul HTML::Tree pro Perl
Summary(da):	Perlmodul HTML::Tree
Summary(de):	HTML::Tree Perl Modul
Summary(es):	Módulo de Perl HTML::Tree
Summary(fr):	Module Perl HTML::Tree
Summary(it):	Modulo di Perl HTML::Tree
Summary(ja):	HTML::Tree Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	HTML::Tree ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul HTML::Tree
Summary(pl):	Modu³ Perla HTML::Tree
Summary(pt):	Módulo de Perl HTML::Tree
Summary(pt_BR):	Módulo Perl HTML::Tree
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl HTML::Tree
Summary(sv):	HTML::Tree Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl HTML::Tree
Summary(zh_CN):	HTML::Tree Perl Ä£¿é
Name:		perl-HTML-Tree
Version:	3.15
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Parser >= 2.19
# do not change to BuildRequires
Requires:	perl-HTML-Format
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of modules that represent, create and extract
information from HTML syntax trees. Modules included: HTML::Element,
HTML::TreeBuilder, HTML::AsSubs, HTML::Parse.

%description -l pl
Kolekcja modu³ów do operowania na drzewach sk³adni HTML. Pakiet
zawiera modu³y: HTML::Element, HTML::TreeBuilder, HTML::AsSubs,
HTML::Parse.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/HTML/*.pm
%dir %{perl_sitelib}/HTML/Element
%{perl_sitelib}/HTML/Element/*.pm
%{_mandir}/man3/*
