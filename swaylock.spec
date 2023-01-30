#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swaylock
Version  : 1.7.2
Release  : 9
URL      : https://github.com/swaywm/swaylock/archive/v1.7.2/swaylock-1.7.2.tar.gz
Source0  : https://github.com/swaywm/swaylock/archive/v1.7.2/swaylock-1.7.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: swaylock-bin = %{version}-%{release}
Requires: swaylock-data = %{version}-%{release}
Requires: swaylock-license = %{version}-%{release}
Requires: swaylock-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : libxkbcommon-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fish)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : scdoc
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# swaylock
swaylock is a screen locking utility for Wayland compositors. It is compatible
with any Wayland compositor which implements one of the following Wayland
protocols:

%package bin
Summary: bin components for the swaylock package.
Group: Binaries
Requires: swaylock-data = %{version}-%{release}
Requires: swaylock-license = %{version}-%{release}

%description bin
bin components for the swaylock package.


%package data
Summary: data components for the swaylock package.
Group: Data

%description data
data components for the swaylock package.


%package license
Summary: license components for the swaylock package.
Group: Default

%description license
license components for the swaylock package.


%package man
Summary: man components for the swaylock package.
Group: Default

%description man
man components for the swaylock package.


%prep
%setup -q -n swaylock-1.7.2
cd %{_builddir}/swaylock-1.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675100313
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/swaylock
cp %{_builddir}/swaylock-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/swaylock/841449f83a67bf0e5197b94f9b9b61eb3ff097e0 || :
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/swaylock

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/swaylock
/usr/share/fish/vendor_completions.d/swaylock.fish
/usr/share/zsh/site-functions/_swaylock

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swaylock/841449f83a67bf0e5197b94f9b9b61eb3ff097e0

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swaylock.1
