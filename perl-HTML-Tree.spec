%include	/usr/lib/rpm/macros.perl
Summary:	HTML-Tree perl module
Summary(pl):	Modu³ perla HTML-Tree
Name:		perl-HTML-Tree
Version:	3.11
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Tree-%{version}.tar.gz
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
%setup -q -n HTML-Tree-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/*.pm
%{_mandir}/man3/*
