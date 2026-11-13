%global debug_package %{nil}
%global commit1 e84665f2fa9d1151f03282ac7e01320bc65e015b
%global commit2 14146609d60915b65b7c4b38dd36b9b6505e7bfa

Name:           camotics
Version:        20261113
Release:        %autorelease
Summary:        Open-Source Simulation & Computer Aided Machining - A 3-axis CNC GCode simulator

# Licenses in order: camotics / cbang / boost, clipper / libevent
License:        GPLv2+ and LGPLv2+ and Boost and BSD
URL:            http://camotics.org/
Source0:        CAMotics-%{commit1}.zip
Source1:        cbang-%{commit2}.zip

BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  leveldb-devel
BuildRequires:  libappstream-glib
BuildRequires:  libevent-devel
BuildRequires:  libyaml-devel
BuildRequires:  lz4-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  python3-six
BuildRequires:  python3-setuptools
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtwebsockets-devel
BuildRequires:  re2-devel
BuildRequires:  scons
BuildRequires:  snappy-devel
BuildRequires:  sqlite-devel
BuildRequires:  v8-11.3-devel

%description
With CAMotics, you can simulate 3-axis GCode programs for CNCs and visualize the results in 3D.

%prep
%setup -c -a 0 -a 1
mv -v cbang-%{commit2} CAMotics-%{commit1}/cbang

%build
cd CAMotics-%{commit1}/cbang
scons -j`nproc` v8_compress_pointers=false
cd ..
scons -j`nproc`

%install
export QA_RPATHS=$(( 0x0001 ))

cd CAMotics-%{commit1}
scons install install_prefix=%{buildroot}/usr

desktop-file-install CAMotics.desktop

%files
%license CAMotics-%{commit1}/LICENSE CAMotics-%{commit1}/COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
