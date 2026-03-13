%global commit0 f9740671836157aefa3d960b50e6abbcda9e44df

Name:           python3-yapps2
Version:        2.2.1
Release:        1%{?dist}
Summary:        Yet Another Python Parser System

License:        MIT
URL:            https://github.com/NTULINUX/yapps2
Source0:        yapps2-%{commit0}.zip
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3dist(setuptools)

%description
Yet Another Python Parser System

Summary:        %{summary}

Requires:       python3dist(setuptools)

%prep
%autosetup -n yapps2-%{commit0}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%{_bindir}/yapps2
%{python3_sitelib}/yapps*

%changelog
* Fri Mar 13 2026 Alec Ari - 2.2.1-1
- Initial package.
