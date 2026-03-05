%global debug_package %{nil}
%global commit1 654ede640ec5f21321db1fcf090fcb9df09d25ed
%global commit2 a7c88e961fd16e0ff421a9cf23fb54da8f42718a

Name:           camotics
Version:        03052026
Release:        1
Summary:        Open-Source Simulation & Computer Aided Machining - A 3-axis CNC GCode simulator

# Licenses in order: camotics / cbang / boost, clipper / libevent
License:        GPLv2+ and LGPLv2+ and Boost and BSD
URL:            http://camotics.org/
Source0:        CAMotics-%{commit1}.zip
Source1:        cbang-%{commit2}.zip

BuildRequires:  bzip2-devel
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  leveldb-devel
BuildRequires:  libappstream-glib
BuildRequires:  libevent-devel
BuildRequires:  lz4-devel
BuildRequires:  openssl-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  scons
BuildRequires:  snappy-devel
BuildRequires:  sqlite-devel
BuildRequires:  v8-11.3-devel
BuildRequires:  yaml-cpp-devel

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
%{_bindir}/*
%{_datadir}/*

%changelog
* Thu Mar 05 2026 Alec Ari <neotheuser@ymail.com> - 03052026-1
- Complete re-write
