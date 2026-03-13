%global snapshot 1
%global commit0  b792287f5bec9086916aa9b81788e0ea38f02c24

Name:           winetricks
Version:        20260313
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
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/io.github.winetricks.Winetricks.metainfo.xml

%changelog
* Fri Mar 13 2026 Alec Ari <neotheuser@ymail.com> - 20260313-1
- Allow Wine installation from WineHQ, use latest snapshot, remove unneeded sed

* Mon Jan 26 2026 Vojtech Trefny <vtrefny@redhat.com> - 20260125-1
- Update to 20260125 (#2432744)

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20250102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20250102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Vojtech Trefny <vtrefny@redhat.com> - 20250102-2
- SPDX license identifier updated to LGPL-2.1-or-later

* Mon Jan 06 2025 Vojtech Trefny <vtrefny@redhat.com> - 20250102-1
- Update to 20250102 (#2335280)

* Fri Dec 06 2024 Vojtech Trefny <vtrefny@redhat.com> - 20240105-1
- Update to 20240105 (#2257082)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 20230212-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230212-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20230212-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20230212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 František Zatloukal <fzatlouk@redhat.com> - 20230212-1
- Update to 20230212

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20220411-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20220411-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 18 2022 František Zatloukal <fzatlouk@redhat.com> - 20220411-1
- Update to 20220411

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20210825-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 20 2021 František Zatloukal <fzatlouk@redhat.com> - 20210825-1
- Update to 20210825

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20210206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 08 2021 František Zatloukal <fzatlouk@redhat.com> - 20210206-1
- Update to 20210206

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201206-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Tom Stellard <tstellar@redhat.com> - 20201206-2
- Add BuildRequires: make

* Tue Dec 15 2020 František Zatloukal <fzatlouk@redhat.com> - 20201206-1
- Update to 20201206

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20200412-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Ernestas Kulik <ekulik@redhat.com> - 20200412-1
- Update to 20200412

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20191224-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Ernestas Kulik <ekulik@redhat.com> - 20191224-1
- Update to 20191224

* Fri Sep 13 2019 Ernestas Kulik <ekulik@redhat.com> - 20190912-1
- Update to 20190912

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20190615-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Ernestas Kulik <ekulik@redhat.com> - 20190615-1
- Update to 20190615

* Tue Mar 12 2019 Ernestas Kulik <ekulik@redhat.com> - 20190310-1
- Update to 20190310

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20181203-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Ernestas Kulik <ekulik@redhat.com> - 20181203-3
- Update files

* Sun Jan 20 2019 Ernestas Kulik <ekulik@redhat.com> - 20181203-2
- Update sources

* Sun Jan 20 2019 Ernestas Kulik <ekulik@redhat.com> - 20181203-1
- Update to 20181203

* Sun Jan 20 2019 Ernestas Kulik <ekulik@redhat.com> - 20180603-5
- Add conditional dependency on kdialog or zenity

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180603-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Raphael Groner <raphgro@fedoraproject.org> - 20180603-3
- avoid shebang warning of rpmlint for appdata

* Sat Jun 23 2018 Raphael Groner <raphgro@fedoraproject.org> - 20180603-2
- uploud sources

* Sat Jun 23 2018 Raphael Groner <raphgro@fedoraproject.org> - 20180603-1
- 20180603

* Mon Mar 05 2018 Raphael Groner <raphgro@fedoraproject.org> - 20180217-4
- new sources

* Mon Mar 05 2018 Raphael Groner <raphgro@fedoraproject.org> - 20180217-3
- ping

* Mon Mar 05 2018 Raphael Groner <raphgro@fedoraproject.org> - 20180217-2
- RPMAUTOSPEC: unresolvable merge
