%global snapshot 1
%global commit0  f3890f670867b5ffbc3938726db45c0f7d16c8ba

Name:           winetricks
Version:        20261113
Release:        %autorelease
Summary:        Work around common problems in Wine

License:        LGPL-2.1-or-later
URL:            https://github.com/Winetricks/%{name}
%if 0%{?snapshot}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.zip
%else
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch

# need arch-specific wine, not available everywhere:
# - adopted from wine.spec
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
# - explicitly not ppc64* to hopefully not confuse koschei
ExcludeArch:    ppc64 ppc64le

BuildRequires:  make
BuildRequires:  desktop-file-utils

Requires:       (winehq-stable or winehq-devel or winehq-staging or wine-common)
Requires:       cabextract gzip unzip wget which
Requires:       hicolor-icon-theme
Requires:       (kdialog if kdialog else zenity)

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.

%prep
%if 0%{?snapshot}
%setup -qn%{name}-%{commit0}
%else
%setup -q
%endif

%install
%make_install
# some tarballs do not install appdata
install -m0644 -D -t %{buildroot}%{_datadir}/metainfo src/io.github.winetricks.Winetricks.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING debian/copyright
%doc README.md
%{_bindir}/winetricks
%{_mandir}/man1/winetricks.1*
%{_datadir}/applications/winetricks.desktop
%{_datadir}/bash-completion/completions/winetricks
%{_datadir}/icons/hicolor/scalable/apps/winetricks.svg
%{_datadir}/metainfo/io.github.winetricks.Winetricks.metainfo.xml

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
