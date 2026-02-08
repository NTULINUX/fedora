# Fedora 43 packages by NTULINUX

To begin, you must download LinuxCNC from this specific snapshot,
and place in the SOURCES directory:

https://github.com/LinuxCNC/linuxcnc/archive/ffee136f3652ce1aacafaa171e8ca5805e3d473d.zip

Install `rpm-build` and `fedpkg`:

`sudo dnf install rpm-build fedpkg`

Now run:

`sudo dnf builddep SPECS/linuxcnc.spec`

Execute build from inside the rpmbuild directory by running:

`rpmbuild -bb SPECS/linuxcnc.spec`

If there are any missing dependencies, please file a bug!
