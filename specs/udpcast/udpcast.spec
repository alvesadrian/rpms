# $Id$
# Authority: dag
# Upstream: <udpcast$udpcast,linux,lu>

%define real_version 20050307

Summary: UDP broadcast installation
Name: udpcast
Version: 0.0.20050307
Release: 1
License: GPL or BSD
Group: Applications/System
URL: http://udpcast.linux.lu/

Source: http://udpcast.linux.lu/current/udpcast-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Requires: netcfg

%description
Allows easy installation of client machines via UDP broadcast

%prep
%setup -n %{name}

%build
#%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} udp-receiver udp-sender

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 udp-receiver %{buildroot}%{_bindir}/udp-receiver
%{__install} -D -m0755 udp-sender %{buildroot}%{_bindir}/udp-sender
#%{__install} -D -m0644 udp-receiver.1 %{buildroot}%{_mandir}/man1/udp-receiver.1
#%{__install} -D -m0644 udp-sender.1 %{buildroot}%{_mandir}/man1/udp-sender.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog.txt cmd.html COPYING README*
#%doc %{_mandir}/man1/udp-receiver.1*
#%doc %{_mandir}/man1/udp-sender.1*
%{_bindir}/udp-receiver
%{_bindir}/udp-sender

%changelog
* Tue Mar 08 2005 Dag Wieers <dag@wieers.com> - 0.0.20050307-1
- Updated to release 20050307.

* Sun Feb 27 2005 Dag Wieers <dag@wieers.com> - 0.0.20050226-1
- Updated to release 20050226.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.0.20040222-1
- Updated to release 20040222.

* Thu Oct 02 2003 Dag Wieers <dag@wieers.com> - 0.0.20030831-0
- Initial package. (using DAR)
