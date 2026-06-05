%global commit 81c3d892ba843993e3eae78d6efd54abaece848e

Name:          linuxcnc
Version:       06052026
Release:       1%{?dist}
Summary:       Motion controller for CNC machines and robots
License:       GPLv2+
URL:           http://www.linuxcnc.io/
Source0:       linuxcnc-%{commit}.zip

BuildRequires: intltool
BuildRequires: %{_bindir}/a2x
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: openssl-devel
BuildRequires: libusb1-devel
BuildRequires: gtk3-devel
BuildRequires: gtksourceview4
BuildRequires: gettext-devel
BuildRequires: python3-devel
BuildRequires: libudev-devel
BuildRequires: boost-devel
BuildRequires: boost-python3
BuildRequires: boost-static
BuildRequires: python3-yapps2
BuildRequires: bwidget
BuildRequires: boost-devel
BuildRequires: libmodbus-devel
BuildRequires: libtirpc-devel
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: python3-tkinter
BuildRequires: mesa-libGLU-devel
BuildRequires: libXmu-devel
BuildRequires: desktop-file-utils
BuildRequires: python3-gobject
BuildRequires: asciidoc
BuildRequires: bwidget
BuildRequires: hicolor-icon-theme
BuildRequires: tkimg
BuildRequires: libXt-devel
BuildRequires: bc
BuildRequires: libcanberra-gtk2
BuildRequires: mesa-libGLU
BuildRequires: python3-tkinter
BuildRequires: python3dist(pyopengl)
BuildRequires: python3dist(python-xlib)
BuildRequires: python3-qt5
BuildRequires: python3-qscintilla-qt5
BuildRequires: qt5-qtwebengine
BuildRequires: python3-qt5-webengine
BuildRequires: pango
BuildRequires: python3-gobject
BuildRequires: python3-cairo
BuildRequires: python3-pyside6-devel
BuildRequires: pyside6-tools
BuildRequires: fmt-devel
BuildRequires: libedit-devel
BuildRequires: shiboken6
BuildRequires: procps-ng
BuildRequires: psmisc

Suggests:      glade

Recommends:    python3-opencv
Recommends:    mesaflash
Recommends:    kernel-rt-lto

%description
Motion controller for CNC machines and robots

%prep
%setup -n linuxcnc-%{commit}

pushd src
./autogen.sh
popd

%build

pushd src
%configure
popd

%{make_build} %{?_smp_mflags} -C src

%install
%{make_install} %{?_smp_mflags} -C src \
    DESTDIR=%{buildroot}

desktop-file-install share/applications/linuxcnc-latency.desktop
desktop-file-install share/applications/linuxcnc-latency-histogram.desktop
desktop-file-install share/applications/linuxcnc-pncconf.desktop
desktop-file-install share/applications/linuxcnc-stepconf.desktop
desktop-file-install share/applications/linuxcnc.desktop

mkdir -p %{buildroot}/usr/share/icons/hicolor/48x48/apps
cp -arLv linuxcncicon.png %{buildroot}/usr/share/icons/hicolor/48x48/apps/

%files

%license COPYING COPYING.more

%{_bindir}/*
%{_prefix}/lib/%{name}/*
%{_libdir}/*
%{_sysconfdir}/*
%{_datadir}/*
%{_includedir}/linuxcnc/*
/usr/lib/tcltk/*

%changelog
* Fri Jun 05 2026 Alec Ari <neotheuser@ymail.com> - 06052026-1
- Add missing dependencies, update LinuxCNC sources, release fix

* Sat Mar 07 2026 Alec Ari <neotheuser@ymail.com> - 03072026-1
- Minor changes, fix missing icons

* Sat Feb 07 2026 Alec Ari <neotheuser@ymail.com> - 02072026-1
- Complete re-write from dwrobel, initial release
