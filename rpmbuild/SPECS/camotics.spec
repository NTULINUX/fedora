%global debug_package %{nil}

%global camotics_commit e84665f2fa9d1151f03282ac7e01320bc65e015b
%global cbang_commit 14146609d60915b65b7c4b38dd36b9b6505e7bfa

Name:           camotics
Version:        20261113
Release:        %autorelease
Summary:        Open-Source Simulation & Computer Aided Machining - A 3-axis CNC GCode simulator

# Licenses in order: camotics / cbang / boost, clipper / libevent
License:        GPLv2+ and LGPLv2+ and Boost and BSD
URL:            http://camotics.org/
Source0:        CAMotics-%{camotics_commit}.zip
Source1:        cbang-%{cbang_commit}.zip

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
mv -v cbang-%{cbang_commit} CAMotics-%{camotics_commit}/cbang

%build
cd CAMotics-%{camotics_commit}/cbang
scons -j`nproc` v8_compress_pointers=false
cd ..
scons -j`nproc`

%install
export QA_RPATHS=$(( 0x0001 ))

cd CAMotics-%{camotics_commit}
scons install install_prefix=%{buildroot}/usr

desktop-file-install CAMotics.desktop

%files
%license CAMotics-%{camotics_commit}/LICENSE CAMotics-%{camotics_commit}/COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
