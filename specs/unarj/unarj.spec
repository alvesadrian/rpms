# $Id$
# Authority: dag

%define real_version 2.63a

Summary: Uncompressor for .arj format archive files
Name: unarj
Version: 2.63
Release: 0.a
Group: Applications/Archiving
License: distributable


Source: http://www.ibiblio.org/pub/Linux/utils/compress/unarj-%{real_version}.tar.gz
Patch: unarj-subdir.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
The UNARJ program is used to uncompress .arj format archives.  The
.arj format archive was mostly used on DOS machines.

%prep
%setup -n %{name}-%{real_version}
#%patch -p1

%build
%{__make} clean
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 unarj %{buildroot}%{_bindir}/unarj

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc *.txt
%{_bindir}/*

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 2.43-1
- Initial package. (using DAR)
