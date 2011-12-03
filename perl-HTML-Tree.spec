#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Tree
Summary:	A suite for making parse trees out of HTML source
Summary(pl.UTF-8):	Pakiet do tworzenie przetworzonych drzew źródła w HTML-u
Name:		perl-HTML-Tree
Version:	4.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a145ad037ac54b6192c0046383d267da
URL:		http://search.cpan.org/dist/HTML-Tree/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-HTML-Parser >= 3.46
BuildRequires:	perl-HTML-Tagset >= 3.02
# HTML::FormatText used in HTML::Element by default; don't use as BuildRequires (loop)
Requires:	perl-HTML-Format
Requires:	perl-HTML-Parser >= 3.46
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of modules that represent, create and extract
information from HTML syntax trees. Modules included: HTML::Element,
HTML::TreeBuilder, HTML::AsSubs, HTML::Parse.

%description -l pl.UTF-8
Kolekcja modułów do operowania na drzewach składni HTML. Pakiet
zawiera moduły: HTML::Element, HTML::TreeBuilder, HTML::AsSubs,
HTML::Parse.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for external HTML::TreeBuilder subclasses
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/TreeBuilder

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/HTML/Tree/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/htmltree
%{perl_vendorlib}/HTML/AsSubs.pm
%{perl_vendorlib}/HTML/Element.pm
%{perl_vendorlib}/HTML/Parse.pm
%{perl_vendorlib}/HTML/Tree.pm
%{perl_vendorlib}/HTML/TreeBuilder.pm
%dir %{perl_vendorlib}/HTML/Element
%{perl_vendorlib}/HTML/Element/traverse.pm
%dir %{perl_vendorlib}/HTML/TreeBuilder
%{_mandir}/man3/HTML::AsSubs.3pm*
%{_mandir}/man3/HTML::Element*.3pm*
%{_mandir}/man3/HTML::Parse.3pm*
%{_mandir}/man3/HTML::Tree*.3pm*
