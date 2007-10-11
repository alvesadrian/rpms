# $Id$
# Authority: dag
# Upstream: Wes Hardaker <wjhns117$hardakers,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name QWizard

Summary: Perl module to display questions and act on the answers
Name: perl-QWizard
Version: 3.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/QWizard/

Source: http://www.cpan.org/modules/by-module/QWizard/QWizard-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-QWizard is a Perl module to display a series of questions, get the
answers, and act on the answers. 

This package contains the following Perl modules:

    QWizard
    QWizard::API
    QWizard::Generator
    QWizard::Generator::Best
    QWizard::Generator::HTML
    QWizard::Generator::HTML::Vertical
    QWizard::Generator::ReadLine
    QWizard::Plugins::Bookmarks
    QWizard::Plugins::History
    QWizard::Storage::Base
    QWizard::Storage::CGICookie
    QWizard::Storage::CGIParam
    QWizard::Storage::File
    QWizard::Storage::Memory
    QWizard::Storage::SQL

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST MANIFEST.SKIP META.yml README examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorlib}/QWizard/
%{perl_vendorlib}/QWizard.pm
%{perl_vendorlib}/QWizard_Widgets.pl
%{perl_vendorlib}/QWizard_Widgets.pod
%{perl_vendorlib}/auto/QWizard/

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 3.08-1
- Initial package. (using DAR)
