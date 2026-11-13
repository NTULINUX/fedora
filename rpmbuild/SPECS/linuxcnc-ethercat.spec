%define debug_package %{nil}

%global commit0 db2a37dc73695e8d027f30db55e9a49ff5af812b

Name:           linuxcnc-ethercat
Version:        20261113
Release:        %autorelease
Summary:        This is a set of LinuxCNC drivers for EtherCAT devices

License:        GPL-2.0-or-later
URL:            https://github.com/linuxcnc-ethercat/linuxcnc-ethercat
Source0:        linuxcnc-ethercat-%{commit0}.zip

BuildRequires:  kernel-rt-lto-nopm
BuildRequires:  linuxcnc
BuildRequires:  ethercat-master

Requires:       kernel-rt-lto-nopm
Requires:       linuxcnc
Requires:       ethercat-master

%description
This is a set of LinuxCNC drivers for EtherCAT devices

%prep
%autosetup -n linuxcnc-ethercat-%{commit0}

%build
%make_build

%install
%make_install DESTDIR=%{buildroot}

%files
%license LICENSE
%{_bindir}/*
%{_prefix}/lib/linuxcnc/modules/*.so
%{_datadir}/linuxcnc-ethercat/*

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
