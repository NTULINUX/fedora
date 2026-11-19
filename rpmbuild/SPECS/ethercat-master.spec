%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}

%global commit0 f53a970163ba3a7dd67d900af326079afeebea10
%global kver 6.18.58-rt6-lto-nopm

Name:           ethercat-master
Version:        20261119
Release:        %autorelease
Summary:        This is an open-source EtherCAT master implementation

License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/linuxcnc-ethercat/ethercat
Source0:        ethercat-%{commit0}.zip

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  kernel-rt-lto-nopm
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libmd)

%description
This is an open-source EtherCAT master implementation

%prep
%autosetup -n ethercat-%{commit0}
./bootstrap

%build
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--localstatedir=/var \
	--with-systemdsystemunitdir=/usr/lib/systemd/system \
	--with-linux-dir=/lib/modules/%{kver}/build \
	--enable-generic \
	--enable-8139too \
	--enable-e100 \
	--enable-e1000 \
	--enable-e1000e \
	--enable-r8169 \
	--enable-igb \
	--enable-igc \
	--enable-genet \
	--disable-stmmac-pci \
	--disable-dwmac-intel \
	--disable-ccat \
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
rm -f %{buildroot}/lib/modules/%{kver}/modules.*
rm -rf %{buildroot}/etc/init.d

%post
/sbin/depmod -a %{kver}
%systemd_post ethercat.service

%preun
%systemd_preun ethercat.service

%postun
/sbin/depmod -a %{kver}
%systemd_postun_with_restart ethercat.service

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
/lib/modules/%{kver}/ethercat

%changelog
* Thu Nov 19 2026 Alec Ari <neotheuser@ymail.com> - 20261119-1
- Bump commit, add hardware drivers from Debian's DKMS

* Mon Nov 16 2026 Alec Ari <neotheuser@ymail.com> - 20261116-1
- Initial Fedora 45 package

* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
