# $Id$
# Authority: dag
# Upstream: Malcolm Smith <malxau@users.sf.net>

Summary: Shared Library for Data Structures
Name: libds
Version: 1.5.2
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://yallara.cs.rmit.edu.au/~malsmith/products/libds/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

### FIXME: Source URL isn't clear about the filename, fails for wget and rpm. (Please fix upstream)
#Source: http://yallara.cs.rmit.edu.au/~malsmith/products/libds/download.php?file=libds-%{version}.tar.bz2
Source: libds-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Shared Library for Data Structures.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc htmldocs/*
%{_bindir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/*
%exclude %{_libdir}/*.la

%changelog
* Sun May 16 2004 Dag Wieers <dag@wieers.com> - 1.5.2-1
- Updated to release 1.5.2.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 1.5.1-1
- Updated to release 1.5.1.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.5.0-0
- Updated to release 1.5.0.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 1.4.0-0
- Updated to release 1.4.0.

* Tue Sep 09 2003 Dag Wieers <dag@wieers.com> - 1.3.1-0
- Initial package. (using DAR)
