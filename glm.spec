# The library consists of headers only
%global debug_package %{nil}

Name:           glm
Version:        0.9.7.6
Release:        2
Summary:        C++ mathematics library for graphics programming
Group:          Development/C
License:        MIT
URL:            https://github.com/g-truc/glm
Source0:	https://github.com/g-truc/glm/releases/download/0.9.7.6/%{name}-%{version}.zip
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
%setup -q -n glm

%build
%cmake
%make

%check

%install
%makeinstall_std -C build
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name CMakeLists.txt -exec rm -f {} ';'

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc copying.txt
%doc doc/%{name}.pdf
%doc doc/api/
