# The library consists of headers only
%global debug_package %{nil}

Name:           glm
Version:        0.9.5.3
Release:        2
Summary:        C++ mathematics library for graphics programming
Group:          Development/C
License:        MIT
URL:            http://glm.g-truc.net/
Source0:        http://downloads.sourceforge.net/ogl-math/%{name}-%{version}/%{name}-%{version}.7z
BuildRequires:  cmake
# For unpacking the source
BuildRequires:	p7zip

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

# A couple of files had CRLF line-ends in them.
sed -i 's/\r//' copying.txt
sed -i 's/\r//' readme.txt

%build
%{cmake} -DGLM_TEST_ENABLE=ON ..
%make

%check
cd build

#ctest --output-on-failure

%install
cd build

%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name CMakeLists.txt -exec rm -f {} ';'

%files devel
%doc copying.txt readme.txt
%{_includedir}/%{name}

%files doc
%doc doc/%{name}.pdf
%doc doc/api/

