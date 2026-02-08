Name:          linuxcnc
Version:       02072026
Release:       1
Summary:       Motion controller for CNC machines and robots
License:       GPLv2+
URL:           http://www.linuxcnc.io/
Source0:       linuxcnc-ffee136f3652ce1aacafaa171e8ca5805e3d473d.zip

BuildRequires: intltool
BuildRequires: %{_bindir}/a2x
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: openssl-devel
BuildRequires: libusb1-devel
BuildRequires: gtk2-devel
BuildRequires: gtk3-devel
BuildRequires: gtksourceview4
BuildRequires: gettext-devel
BuildRequires: python3-devel
BuildRequires: libudev-devel
BuildRequires: boost-devel
BuildRequires: boost-python3
BuildRequires: boost-static
BuildRequires: python3-Yapps
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
BuildRequires: blt
BuildRequires: bwidget
BuildRequires: hicolor-icon-theme
BuildRequires: tkimg
BuildRequires: libXt-devel
BuildRequires: bc
BuildRequires: tclx
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

Suggests:      glade

Recommends:    python3-opencv
Recommends:    mesaflash

%description
Motion controller for CNC machines and robots

%prep
%setup -n linuxcnc-ffee136f3652ce1aacafaa171e8ca5805e3d473d

pushd src
./autogen.sh
popd

%build

pushd src
%configure \
    --enable-non-distributable=yes
popd

%{make_build} -C src

%install
%{make_install} -C src \
    DESTDIR=%{buildroot}

%files

%license COPYING COPYING.more

%{_bindir}/*
%caps(cap_ipc_lock,cap_net_admin,cap_sys_rawio,cap_sys_nice+ep) %{_bindir}/rtapi_app
%{_prefix}/lib/%{name}/*
%{_libdir}/*
%{_sysconfdir}/*
%{_datadir}/*
%{_mandir}/*
%dir %{_includedir}/linuxcnc
%{_includedir}/linuxcnc/*
/usr/lib/tcltk/*

%changelog
* Sat Feb 07 2026 Alec Ari <neotheuser@ymail.com> - 02072026-1
- Complete re-write from dwrobel, initial release
