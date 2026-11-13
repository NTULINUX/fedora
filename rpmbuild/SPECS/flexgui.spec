%global commit0 dd38878b984ba1b30a784343e96cda22c84be3fc

Name:           flexgui
Version:        20261113
Release:        %autorelease
Summary:        A flexible GUI for LinuxCNC

License:        MIT
URL:            https://github.com/jethornton/flexgui
Source0:        %{name}-%{commit0}.zip

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       python3
Requires:       linuxcnc

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
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
