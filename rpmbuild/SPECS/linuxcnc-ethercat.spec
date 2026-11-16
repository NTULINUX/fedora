%define debug_package %{nil}

%global commit0 19046028dd8b3ba72b0b0aae66996644d8fb7257

Name:           linuxcnc-ethercat
Version:        20261116
Release:        %autorelease
Summary:        This is a set of LinuxCNC drivers for EtherCAT devices

License:        GPL-2.0-or-later
URL:            https://github.com/linuxcnc-ethercat/linuxcnc-ethercat
Source0:        linuxcnc-ethercat-%{commit0}.zip

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  expat-devel
BuildRequires:  kernel-rt-lto-nopm
BuildRequires:  linuxcnc
BuildRequires:  python3-yapps2
BuildRequires:  ethercat-master

Requires:       kernel-rt-lto-nopm
Requires:       linuxcnc
Requires:       ethercat-master

%description
This is a set of LinuxCNC drivers for EtherCAT devices

%prep
%autosetup -n %{name}-%{commit0}

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
* Mon Nov 16 2026 Alec Ari <neotheuser@ymail.com> - 20261116-1
- Initial Fedora 45 package

* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
