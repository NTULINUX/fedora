%global commit ce94068dc3ad8b8db5f28225598a97a9eb059ecb

Name:           halviewer
Version:        20261113
Release:        %autorelease
Summary:        Graphical halviewer for LinuxCNC

License:        GPL-3.0-only
URL:            https://github.com/multigcs/halviewer
Source0:        %{name}-%{commit}.zip

BuildArch:      noarch

Requires:       python3-devel
Requires:       python3-graphviz
Requires:       linuxcnc

%description
Graphical halviewer for LinuxCNC

%prep
%setup -n %{name}-%{commit}

%install
install -D -m 0755 halviewer.py %{buildroot}%{_bindir}/halviewer

%files
%license LICENSE
%{_bindir}/halviewer

%changelog
* Fri Nov 13 2026 Alec Ari <neotheuser@ymail.com> - 20261113-1
- Fedora 44 refresh
