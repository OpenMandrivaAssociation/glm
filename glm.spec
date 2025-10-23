# The library consists of headers only
%global debug_package %{nil}

%define _disable_ld_no_undefined 1
%define _disable_lto 1


# Upstream no longer provide CMAKE install target. Files should be installed manually. 
# Also upstream cease providing .pc files so .pc file need to be re-created manually. Also at some poing worth to bring back cmake files.

Name:           glm
Version:        1.0.2
Release:        1
Summary:        C++ mathematics library for graphics programming
Group:          Development/C
License:        MIT
URL:            https://github.com/g-truc/glm
Source0:	https://github.com/g-truc/glm/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:  https://src.fedoraproject.org/rpms/glm/raw/rawhide/f/glm-1.0.1-without-werror.patch
BuildRequires:  cmake

%description
GLM is a C++ library for doing mathematics operations
required in many OpenGL based applications. Its interface
has been designed to resemble the built-in matrix and vector
types of the OpenGL shading language.

%package        devel
Summary:        C++ mathematics library for graphics programming

%description    devel
GLM is a C++ library for doing mathematics operations
required in many OpenGL based applications. Its interface
has been designed to resemble the built-in matrix and vector
types of the OpenGL shading language.

%{name}-devel is only required for building software that uses
the GLM library. Because GLM currently is a header-only library,
there is no matching run time package.

%package        doc
Summary:        Documentation for %{name}-devel
Group:          Books/Computer books
BuildArch:      noarch

%description    doc
The %{name}-doc package contains reference documentation and
a programming manual for the %{name}-devel package.

%prep
# Some glm releases, like version 0.9.3.1, place contents of
# the source archive directly into the archive root. Others,
# like glm 0.9.3.2, place them into a single subdirectory.
# The former case is inconvenient, but it can be be
# compensated for with the -c option of the setup macro.
#
# When updating this package, take care to check if -c is
# needed for the particular version.

%autosetup -p1

%build
export CC=gcc
export CXX=g++
%cmake -DCMAKE_INSTALL_DATAROOTDIR=%{_datadir}/cmake
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install -C build
install -d $RPM_BUILD_ROOT%{_includedir}

cp -a glm $RPM_BUILD_ROOT%{_includedir}

#mkdir -p $RPM_BUILD_ROOT/usr/lib/pkgconfig/
#cp glm.pc $RPM_BUILD_ROOT/usr/lib/pkgconfig/


# Dirty hack to provide .pc file. Needed bc of upstream stupidity.
mkdir -p %{buildroot}%{_libdir}/pkgconfig/
cat << "EOF" > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
prefix=/usr
includedir=${prefix}/include

Name: GLM
Description: OpenGL Mathematics
Version: %{version}
EOF
 
%files devel
%{_includedir}/%{name}
#{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/libglm.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/cmake/glm/

%files doc
%doc doc/api/
