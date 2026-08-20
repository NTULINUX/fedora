%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}

%global commit 949d7562991683bfb797e7c4fed49399cba16f22
%global kver 6.18.44
%global rt rt6
%global pkg_kver %{kver}-%{rt}

Name:           kernel-rt-lto
Version:        %{kver}.%{rt}
Release:        %autorelease
Summary:        PREEMPT_RT Linux kernel

License:        GPLv2
URL:            https://github.com/NTULINUX/linux
Source0:        linux-%{commit}.zip
Source1:        rt.config

BuildRequires:  clang
BuildRequires:  lld
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  elfutils-libelf-devel
BuildRequires:  openssl-devel
BuildRequires:  bc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  diffutils
BuildRequires:  lz4
BuildRequires:  perl

%description
PREEMPT_RT Linux kernel built with -O3 and ThinLTO

%prep
%setup -q -n linux-%{commit}

%build
cp -ar %{SOURCE1} .config
LLVM=1 make %{?_smp_mflags} olddefconfig
LLVM=1 make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/boot
cp -ar .config %{buildroot}/boot/config-%{pkg_kver}
cp -ar System.map %{buildroot}/boot/System.map-%{pkg_kver}
cp -ar arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{pkg_kver}

LLVM=1 make modules_install INSTALL_MOD_PATH=%{buildroot}

rm -rf %{buildroot}/lib/modules/%{pkg_kver}/build
rm -rf %{buildroot}/lib/modules/%{pkg_kver}/source

%post
kernel-install add %{pkg_kver} /boot/vmlinuz-%{pkg_kver}

%postun
if [ $1 -eq 0 ] ; then
    kernel-install remove %{pkg_kver}
fi

%files
/boot/*-%{pkg_kver}
/lib/modules/%{pkg_kver}

%changelog
%autochangelog
