%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary: 	HTML-Tree perl module
Summary(pl):	Modu³ perla HTML-Tree
Name: 		perl-HTML-Tree
Version: 	0.51
Release: 	3
Copyright: 	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Tree-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-HTML-Parser >= 2.19
BuildRequires:	perl-Font-AFM >= 1.17
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-HTML-Parser >= 2.19
Requires:	perl-Font-AFM >= 1.17
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a collection of modules that represent, create and extract
information from HTML syntax trees. Modules included: HTML::Element,
HTML::TreeBuilder, HTML::AsSubs, HTML::Formatter, HTML::FormatText,
HTML::FormatPS.

%description -l pl
Kolekcja modu³ów do operowania na drzewach sk³adni HTML. Pakiet zawiera 
modu³y: HTML::Element, HTML::TreeBuilder, HTML::AsSubs, HTML::Formatter, 
HTML::FormatText, HTML::FormatPS.

%prep
%setup -q -n HTML-Tree-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML-Tree
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes}.gz

%{perl_sitelib}/HTML/*.pm
%{perl_sitearch}/auto/HTML-Tree

%{_mandir}/man3/*
