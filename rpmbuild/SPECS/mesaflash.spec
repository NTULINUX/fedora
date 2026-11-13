%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}

%global commit0 11e6f8571cc79d3acae57274aa57c4b99d26cb3f

Name:           mesaflash
Version:        20261113
Release:        %autorelease
Summary:        Configuration and diagnostic tool for Mesa Electronics boards

License:        GPL-2.0-or-later
URL:            https://github.com/linuxcnc/mesaflash
Source0:        %{name}-%{commit0}.zip

BuildRequires:  make
BuildRequires:  /usr/bin/git
BuildRequires:  gcc
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libmd)

%description
Configuration and diagnostic tool for Mesa Electronics
PCI(E)/ETH/EPP/USB/SPI boards.

%prep
%autosetup -n %{name}-%{commit0}

%build
make %{?_smp_mflags}

%install
%{make_install} OWNERSHIP="" DESTDIR="%{buildroot}%{_prefix}"

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
