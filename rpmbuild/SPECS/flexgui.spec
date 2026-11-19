%global commit0 6cf2f3a9003cb91726e5a63daacd2392f3de0052

Name:           flexgui
Version:        20261119
Release:        %autorelease
Summary:        A flexible GUI for LinuxCNC

License:        MIT
URL:            https://github.com/jethornton/flexgui
Source0:        %{name}-%{commit0}.zip

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       linuxcnc
Requires:       python3
Requires:       python3-pyqt6

%description
Flex GUI is a tool to build exactly the GUI you want for LinuxCNC.

%prep
%setup -n %{name}-%{commit0}

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 flexgui/src/flexgui %{buildroot}%{_bindir}/
install -m 0755 flexgui/src/flexcopy %{buildroot}%{_bindir}/
install -m 0755 flexgui/src/flexqrc %{buildroot}%{_bindir}/
install -m 0755 flexgui/src/flexqss %{buildroot}%{_bindir}/
install -m 0755 flexgui/src/flexdocs %{buildroot}%{_bindir}/

install -d -m 0755 %{buildroot}%{_datadir}/applications
install -m 0644 flexgui/*.desktop %{buildroot}%{_datadir}/applications/

install -d -m 0755 %{buildroot}%{_exec_prefix}/lib/libflexgui
install -m 0644 flexgui/src/*.ui %{buildroot}%{_exec_prefix}/lib/libflexgui/
install -m 0644 flexgui/src/libflexgui/*.ui %{buildroot}%{_exec_prefix}/lib/libflexgui/
install -m 0644 flexgui/src/libflexgui/*.qss %{buildroot}%{_exec_prefix}/lib/libflexgui/
install -m 0644 flexgui/src/libflexgui/*.jpg %{buildroot}%{_exec_prefix}/lib/libflexgui/

install -d -m 0755 %{buildroot}%{python3_sitelib}/libflexgui
install -m 0644 flexgui/src/libflexgui/*.py %{buildroot}%{python3_sitelib}/libflexgui/

install -d -m 0755 %{buildroot}%{_exec_prefix}/lib/libflexgui/examples
cp -pr examples/* %{buildroot}%{_exec_prefix}/lib/libflexgui/examples/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc flexgui/FlexGUI-blackbg.png flexgui/flexgui.pdf
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_exec_prefix}/lib/libflexgui/
%{python3_sitelib}/libflexgui/

%changelog
* Thu Nov 19 2026 Alec Ari <neotheuser@ymail.com> - 20261119-1
- Bump commit

* Wed Nov 18 2026 Alec Ari <neotheuser@ymail.com> - 20261118-1
- Bump commit

* Mon Nov 16 2026 Alec Ari <neotheuser@ymail.com> - 20261116-1
- Initial Fedora 45 package, add python3-pyqt6 dep

* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
