# $Id$
# Authority: matthias
# Upstream: <madman-discuss$lists,sourceforge,net>

Summary: Madman Administrates Digital Music Archives Neatly
Name: madman
Version: 0.94
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://madman.sourceforge.net/

Source: http://dl.sf.net/madman/madman-%{version}.tar.gz
Patch0: madman-0.93-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: scons, gcc-c++, glib-devel, qt-devel
BuildRequires: xmms-devel, libid3tag-devel, libogg-devel, libvorbis-devel
# xmms-devel, *sigh*
BuildRequires: gtk+-devel
Requires: xmms

%description
Madman is a music manager application that allows you to easily keep your
music database organized and tidy, and it helps you listen to better music,
be happier, brighten your teeth and quickly restore world peace.

%prep
%setup
%patch0 -p1 -b .gcc34

%build
scons prefix="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
scons prefix="%{buildroot}%{_prefix}" install

### What is this file anyway?
%{__rm} -f %{buildroot}%{_prefix}/bin/.sconsign

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/madman
%{_libdir}/madman/

%changelog
* Sat May 24 2008 Dag Wieers <dag@wieers.com> - 0.94-1
- Updated to release 0.94.

* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 0.93-2
- Add gcc 3.4 fix from Debian bug #260503.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 0.93-1
- Update to 0.93.
- Update to use the new SCons build.

* Fri Apr  2 2004 Matthias Saou <http://freshrpms.net/> 0.91.1-1
- Initial RPM release.
