%define _lto_cflags %{nil}
%global commit caa13ca6ae62045c56d379e23010ec18f548224d

Name:          linuxcnc
Version:       07302026
Release:       1%{?dist}
Summary:       Motion controller for CNC machines and robots
License:       GPLv2+
URL:           http://www.linuxcnc.io/
Source0:       linuxcnc-%{commit}.zip

BuildRequires: %{_bindir}/a2x
BuildRequires: %{_bindir}/convert
BuildRequires: %{_bindir}/dd
BuildRequires: %{_bindir}/git
BuildRequires: %{_bindir}/intltool-extract
BuildRequires: %{_bindir}/nc
BuildRequires: %{_bindir}/which
BuildRequires: asciidoc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: avahi
BuildRequires: bc
BuildRequires: boost-devel
BuildRequires: boost-python3
BuildRequires: boost-python3-devel
BuildRequires: boost-static
BuildRequires: bwidget
BuildRequires: desktop-file-utils
BuildRequires: docbook-xsl
BuildRequires: dvipng
BuildRequires: fmt-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: ghostscript
BuildRequires: glade
BuildRequires: GraphicsMagick
BuildRequires: graphviz
BuildRequires: groff
BuildRequires: gtk3-devel
BuildRequires: gtksourceview3
BuildRequires: gtksourceview4
BuildRequires: hicolor-icon-theme
BuildRequires: initscripts
BuildRequires: inkscape
BuildRequires: intltool
BuildRequires: kmod
BuildRequires: kmod-devel
BuildRequires: libcanberra-gtk2
BuildRequires: libcanberra-gtk3
BuildRequires: libcap-devel
BuildRequires: libedit-devel
BuildRequires: libgpiod-devel
BuildRequires: libmodbus-devel
BuildRequires: librsvg2-tools
BuildRequires: libtirpc-devel
BuildRequires: libudev-devel
BuildRequires: libusb1-devel
BuildRequires: libusbx-devel
BuildRequires: libuuid-devel
BuildRequires: libXaw-devel
BuildRequires: libXmu-devel
BuildRequires: libxslt
BuildRequires: libXt
BuildRequires: libXt-devel
BuildRequires: linkchecker
BuildRequires: lsb_release
BuildRequires: mesa-libGLU
BuildRequires: mesa-libGLU-devel
BuildRequires: openssl-devel
BuildRequires: PackageKit-gtk3-module
BuildRequires: pam
BuildRequires: pam-devel
BuildRequires: pango
BuildRequires: pango-devel
BuildRequires: procps-ng
BuildRequires: psmisc
BuildRequires: pyside6-tools
BuildRequires: python-lxml
BuildRequires: python3-cairo
BuildRequires: python3-configobj
BuildRequires: python3-devel
BuildRequires: python3-gobject
BuildRequires: python3-poppler-qt5
BuildRequires: python3-pyopengl
BuildRequires: python3-pyside6-devel
BuildRequires: python3-qscintilla-qt5
BuildRequires: python3-qt5
BuildRequires: python3-qt5-webengine
BuildRequires: python3-tkinter
BuildRequires: python3-xlib
BuildRequires: python3-yapps2
BuildRequires: qt5-qtwebengine
BuildRequires: qt5-qtwebengine-devel
BuildRequires: rubygem-asciidoctor
BuildRequires: shiboken6
BuildRequires: source-highlight
BuildRequires: tcl-devel
BuildRequires: tk-devel
BuildRequires: tkimg

Requires:      avahi
Requires:      boost-python3
Requires:      bwidget
Requires:      desktop-file-utils
Requires:      glade
Requires:      gtksourceview3
Requires:      gtksourceview4
Requires:      hicolor-icon-theme
Requires:      initscripts
Requires:      inkscape
Requires:      kmod
Requires:      libcanberra-gtk2
Requires:      libcanberra-gtk3
Requires:      mesa-libGLU
Requires:      PackageKit-gtk3-module
Requires:      pam
Requires:      pango
Requires:      procps-ng
Requires:      psmisc
Requires:      pyside6-tools
Requires:      python-lxml
Requires:      python3-cairo
Requires:      python3-configobj
Requires:      python3-devel
Requires:      python3-docopt
Requires:      python3-gobject
Requires:      python3-poppler-qt5
Requires:      python3-pybind11
Requires:      python3-pyopengl
Requires:      python3-pyqtgraph
Requires:      python3-pyside6
Requires:      python3-qscintilla-qt5
Requires:      python3-qt5
Requires:      python3-qt5-webengine
Requires:      python3-simpleeval
Requires:      python3-sqlalchemy
Requires:      python3-tkinter
Requires:      python3-vtk
Requires:      python3-xlib
Requires:      qt5-qtwebengine
Requires:      qt6-qttools-devel
Requires:      source-highlight
Requires:      tkimg

Recommends:    kernel-rt-lto
Recommends:    mesaflash
Recommends:    python3-opencv

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
%{make_install} %{?_smp_mflags} -C src DESTDIR=%{buildroot}

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

%changelog
* Thu Jul 30 2026 Alec Ari <neotheuser@ymail.com> - 07302026-1
- Bump LinuxCNC commit, complete dependency overhaul

* Wed Jul 29 2026 Alec Ari <neotheuser@ymail.com> - 07292026-1
- Bump LinuxCNC commit (memory leak fixes)

* Sun Jul 19 2026 Alec Ari <neotheuser@ymail.com> - 07192026-1
- Bump LinuxCNC commit

* Tue Jun 16 2026 Alec Ari <neotheuser@ymail.com> - 06162026-1
- Bump LinuxCNC commit, drops requirement for setting TCLLIBPATH

* Sat Jun 06 2026 Alec Ari <neotheuser@ymail.com> - 06062026-1
- Disable LTO to avoid possible misoptimization

* Fri Jun 05 2026 Alec Ari <neotheuser@ymail.com> - 06052026-2
- Add a lot more dependencies

* Fri Jun 05 2026 Alec Ari <neotheuser@ymail.com> - 06052026-1
- Add missing dependencies, update LinuxCNC sources, release fix

* Sat Mar 07 2026 Alec Ari <neotheuser@ymail.com> - 03072026-1
- Minor changes, fix missing icons

* Sat Feb 07 2026 Alec Ari <neotheuser@ymail.com> - 02072026-1
- Complete re-write from dwrobel, initial release
