%define debug_package %{nil}
%global set_build_flags %{nil}
%global __global_compiler_flags %{nil}
%global commit a4cc3b3e45eea26b96bf570ca327b311612f0b57

%global kver 6.18.40-rt6

Name:           kernel-rt-lto
Version:        6.18.40.rt6
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
/usr/bin/kernel-install add %{kver} /boot/vmlinuz-%{kver}

%postun
if [ $1 -eq 0 ]; then
    /usr/bin/kernel-install remove %{kver}
fi

%files
/boot/*-%{kver}
/lib/modules/%{kver}

%changelog
* Wed Jul 29 2026 Alec Ari <neotheuser@ymail.com> - 6.18.40.rt6-1
- Bump kernel, config tweaks (enable THP)

* Sun Jul 19 2026 Alec Ari <neotheuser@ymail.com> - 6.18.39.rt6-1
- Change kernel to 6.18 LTS series and update spec file

* Fri May 29 2026 Alec Ari <neotheuser@ymail.com> - 7.1.0.rc6.rt1-1
- Initial optimized PREEMPT_RT release for Fedora 44
