%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}
%global commit aa4cb4fe13329e93f4a06d6bdc0728458d0c82e2

%global kver 7.1.0-rc6-rt1

Name:           kernel-rt-lto
Version:        7.1.0.rc6.rt1
Release:        1%{?dist}
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
cp -arLv %{SOURCE1} .config
LLVM=1 make %{?_smp_mflags} olddefconfig
LLVM=1 make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/boot
cp -ar .config %{buildroot}/boot/config-%{kver}
cp -ar System.map %{buildroot}/boot/System.map-%{kver}
cp -ar arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{kver}

make modules_install INSTALL_MOD_PATH=%{buildroot}

rm -rf %{buildroot}/lib/modules/%{kver}/build
rm -rf %{buildroot}/lib/modules/%{kver}/source

%post
kernel-install add %{kver} /boot/vmlinuz-%{kver}

%preun
kernel-install remove %{kver}

%files
/boot/*-%{kver}
/lib/modules/%{kver}

%changelog
* Fri May 29 2026 Alec Ari <neotheuser@ymail.com> - 7.1.0.rc6.rt1-1
- Initial optimized PREEMPT_RT release for Fedora 44
