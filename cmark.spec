#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmark
Version  : 0.30.2
Release  : 3
URL      : https://github.com/commonmark/cmark/archive/refs/tags/0.30.2.tar.gz
Source0  : https://github.com/commonmark/cmark/archive/refs/tags/0.30.2.tar.gz
Summary  : CommonMark parsing, rendering, and manipulation
Group    : Development/Tools
License  : BSD-3-Clause
Requires: cmark-lib = %{version}-%{release}
Requires: cmark-license = %{version}-%{release}
Requires: cmark-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : python3

%description
cmark
=====
[![CI
tests](https://github.com/commonmark/cmark/workflows/CI%20tests/badge.svg)](https://github.com/commonmark/cmark/actions)

%package dev
Summary: dev components for the cmark package.
Group: Development
Requires: cmark-lib = %{version}-%{release}
Provides: cmark-devel = %{version}-%{release}
Requires: cmark = %{version}-%{release}

%description dev
dev components for the cmark package.


%package lib
Summary: lib components for the cmark package.
Group: Libraries
Requires: cmark-license = %{version}-%{release}

%description lib
lib components for the cmark package.


%package license
Summary: license components for the cmark package.
Group: Default

%description license
license components for the cmark package.


%package man
Summary: man components for the cmark package.
Group: Default

%description man
man components for the cmark package.


%prep
%setup -q -n cmark-0.30.2
cd %{_builddir}/cmark-0.30.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647875548
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1647875548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cmark
cp %{_builddir}/cmark-0.30.2/COPYING %{buildroot}/usr/share/package-licenses/cmark/fa524e3e5b56232fdada455ba84c938f5a1487d2
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/bin/cmark

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cmark.h
/usr/include/cmark_export.h
/usr/include/cmark_version.h
/usr/lib64/cmake/cmark/cmark-config-version.cmake
/usr/lib64/cmake/cmark/cmark-config.cmake
/usr/lib64/cmake/cmark/cmark-targets-relwithdebinfo.cmake
/usr/lib64/cmake/cmark/cmark-targets.cmake
/usr/lib64/libcmark.so
/usr/lib64/pkgconfig/libcmark.pc
/usr/share/man/man3/cmark.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcmark.so.0.30.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cmark/fa524e3e5b56232fdada455ba84c938f5a1487d2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cmark.1
