%define debug_package %{nil}
%undefine _hardened_build

Name:           wavemon
Version:        0.9.7
Release:        1%{?dist}
Summary:        Ncurses-based monitoring application for wireless network devices

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/uoaerg/wavemon
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libpcap-devel
BuildRequires:  libnl3-devel
BuildRequires:  autoconf
BuildRequires:  automake

%description
wavemon is a wireless device monitoring application that allows you to
watch all important information like device configuration, encryption,
and power management parameters and network information at once.
Adaptive level bargraphs for link quality, signal/noise strength and
signal-to-noise ratio.  The customizeable "level alarm" feature that
notices the user of changes in signal level strength audibly and/or
visually. wavemon is able to list of access points in range and shows
full-screen level histogram displaying signal/noise levels and SNR.

%prep
%autosetup
sed -e '/^CFLAGS=/d' -i configure.ac
sed -r 's|\?=|=|g' -i Makefile.in
autoreconf -fiv

%build
CFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"
CXXFLAGS="$RPM_OPT_FLAGS -fPIC -pie -Wl,-z,relro -Wl,-z,now"

%configure
make %{?_smp_mflags}

%install
%make_install
# Delete wrong placed doc files
rm -rf %{buildroot}%{_datadir}/%{name}/*

%files
%doc README.md
%license LICENSE
%{_mandir}/man*/wavemon*.*
%{_bindir}/wavemon

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 0.9.7-1
- Fedora 44 refresh
