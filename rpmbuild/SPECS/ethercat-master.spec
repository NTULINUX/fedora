%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}

%global commit0 6e9d8f4dc54d04115d5014f9588dbb06f02c05e4
%global kernel_version 6.18.58-rt6-lto-nopm

Name:           ethercat-master
Version:        20261111
Release:        %autorelease
Summary:        This is an open-source EtherCAT master implementation for Linux 2.6 or newer.

License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/linuxcnc-ethercat/ethercat
Source0:        ethercat-%{commit0}.zip

BuildRequires:  make
BuildRequires:  /usr/bin/git
BuildRequires:  gcc
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libmd)

%description
This is an open-source EtherCAT master implementation for Linux 2.6 or newer.

%prep
%autosetup -n ethercat-%{commit0}
./bootstrap

%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--with-systemdsystemunitdir=/usr/lib/systemd/system \
	--disable-8139too \
	--disable-eoe \
	--enable-cycles \
	--enable-hrtimer \
	--disable-rtdm \
	--disable-debug-if \
	--disable-debug-ring \
	--disable-regalias \
	--disable-tty \
	--enable-wildcards \
	--enable-sii-assign \
	--enable-rt-syslog

LLVM=1 make %{?_smp_mflags} all modules

%install
%{make_install} INSTALL_MOD_PATH="%{buildroot}" modules_install
rm -f %{buildroot}/lib/modules/%{kernel_version}/modules.*
rm -rf %{buildroot}/etc/init.d

%files
%license COPYING COPYING.LESSER
/usr/bin/ethercat
/usr/sbin/ethercatctl
%{_sysconfdir}/*
%{_includedir}/*
%{_prefix}/lib/cmake/*
%{_prefix}/lib/libethercat.*
%{_prefix}/lib/pkgconfig/*
%{_unitdir}/*
%{_datadir}/*
/lib/modules/%{kernel_version}/ethercat

%changelog
%autochangelog
