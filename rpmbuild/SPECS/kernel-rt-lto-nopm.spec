%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}

%global commit e7c4cf2a0c52165bec65540ecbc2a54a979d1b24
%global kver 6.18.58
%global rt rt6
%global pkg_kver %{kver}-%{rt}-lto-nopm

Name:          kernel-rt-lto-nopm
Version:       %{kver}.%{rt}
Release:       %autorelease
Summary:       PREEMPT_RT Linux kernel without power management

License:       GPL-2.0-only
URL:           https://github.com/NTULINUX/linux
Source0:       linux-%{commit}.zip
Source1:       rt_nopm.config

BuildRequires: clang
BuildRequires: lld
BuildRequires: llvm
BuildRequires: make
BuildRequires: elfutils-libelf-devel
BuildRequires: openssl-devel
BuildRequires: bc
BuildRequires: flex
BuildRequires: bison
BuildRequires: diffutils
BuildRequires: lz4
BuildRequires: perl

%description
PREEMPT_RT Linux kernel built with -O3 and ThinLTO (no power management)

%prep
%setup -q -n linux-%{commit}

%build
cp -ar %{SOURCE1} .config
LLVM=1 make %{?_smp_mflags} olddefconfig
LLVM=1 make %{?_smp_mflags}
LLVM=1 make %{?_smp_mflags} tools/objtool

%install
mkdir -p %{buildroot}/boot
cp -ar .config %{buildroot}/boot/config-%{pkg_kver}
cp -ar arch/x86/boot/bzImage %{buildroot}/boot/vmlinuz-%{pkg_kver}
cp -ar System.map %{buildroot}/boot/System.map-%{pkg_kver}

LLVM=1 make modules_install INSTALL_MOD_PATH=%{buildroot}

# For building external kernel modules (EtherCAT)
FEDORA_SRCDIR=%{buildroot}/usr/src/kernels/%{pkg_kver}
mkdir -p $FEDORA_SRCDIR/arch/x86
cp -ar .config Kconfig Makefile Module.symvers System.map $FEDORA_SRCDIR/
cp -ar arch/x86/{include,Kconfig,Makefile} $FEDORA_SRCDIR/arch/x86/
cp -ar include scripts tools $FEDORA_SRCDIR/
# Get rid of ambiguous python shebang errors
rm -rf $FEDORA_SRCDIR/tools/{perf,testing}

# Mimic Fedora's behavior when it comes to the kernel source
rm -rf %{buildroot}/lib/modules/%{pkg_kver}/build
rm -rf %{buildroot}/lib/modules/%{pkg_kver}/source
mkdir -p %{buildroot}/lib/modules/%{pkg_kver}
ln -sf ../../../../usr/src/kernels/%{pkg_kver} %{buildroot}/lib/modules/%{pkg_kver}/build
ln -sf ../../../../usr/src/kernels/%{pkg_kver} %{buildroot}/lib/modules/%{pkg_kver}/source

%post
kernel-install add %{pkg_kver} /boot/vmlinuz-%{pkg_kver}

%postun
if [ $1 -eq 0 ] ; then
    kernel-install remove %{pkg_kver}
fi

%files
/boot/*-%{pkg_kver}
/lib/modules/%{pkg_kver}
/usr/src/kernels/%{pkg_kver}

%changelog
%autochangelog
