%global commit0 eff00a6e3cd0b36767b79848677a533e7358d2b8

Name:           mesact
Version:        09292026
Release:        1%{?dist}
Summary:        Mesa Configuration Tool II

License:        MIT
URL:            https://github.com/jethornton/mesact
Source0:        %{name}-%{commit0}.zip

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils

Requires:       python3
Requires:       linuxcnc

%description
Mesa Configuration Tool II

%prep
%autosetup -n %{name}-%{commit0}

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_exec_prefix}/lib/libmesact
install -d %{buildroot}%{_docdir}/mesact
install -d %{buildroot}%{python3_sitelib}/libmesact
install -d %{buildroot}%{_datadir}/applications

install -m 755 mesact/src/mesact %{buildroot}%{_bindir}/mesact
install -m 644 mesact/src/mesact.ui %{buildroot}%{_exec_prefix}/lib/libmesact/
install -m 644 mesact/src/libmesact/mesact.qss %{buildroot}%{_exec_prefix}/lib/libmesact/
install -m 644 mesact/src/libmesact/mesact.jpg %{buildroot}%{_exec_prefix}/lib/libmesact/
install -m 644 mesact/mesact.pdf %{buildroot}%{_docdir}/mesact/
install -m 644 mesact/src/libmesact/*.py %{buildroot}%{python3_sitelib}/libmesact/

desktop-file-install mesact/mesa-configuration.desktop
desktop-file-install mesact/mesa-docs.desktop

gzip %{buildroot}%{_pkgdocdir}/mesact.pdf

%files
%doc LICENSE
%{_pkgdocdir}/mesact.pdf.gz
%{_bindir}/mesact
%{_exec_prefix}/lib/libmesact/
%{python3_sitelib}/libmesact/
%{_datadir}/applications/*.desktop

%changelog
* Tue Sep 29 2026 Alec Ari <neotheuser@ymail.com> - 09292026-1
- Initial package
