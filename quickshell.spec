%global commit      eabf79ebb640dbfab6a3ff4639db65e64e05d941
%global snapdate    20250319
%global quickshell_shortcommit %(c=%{commit}; echo ${c:0:7})
%global bumpver 1

Name:               quickshell
Version:            0~%{bumpver}.git%{quickshell_shortcommit}
Release:            4
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Group:		Graphical desktop/Other

BuildSystem:	cmake
BuildOption:-DDISTRIBUTOR="OpenMandriva LX" BuildOption:-DISTRIBUTOR_DEBUGINFO_AVAILABLE=YES BuildOption:-DCMAKE_BUILD_TYPE=RelWithDebInfo BuildOption:-DINSTALL_QML_PREFIX="%{_qtdir}" BuildOption:-DINSTALL_QMLDIR="%{_qtdir}/qml"

BuildRequires:      cmake
BuildRequires:      cmake(Qt6Core)
BuildRequires:      cmake(Qt6Qml)
BuildRequires:      cmake(Qt6ShaderTools)
BuildRequires:      cmake(Qt6WaylandClient)
BuildRequires:      gcc-c++
BuildRequires:      ninja-build
BuildRequires:      pkgconfig(breakpad)
BuildRequires:      pkgconfig(CLI11)
BuildRequires:      pkgconfig(gbm)
BuildRequires:      pkgconfig(jemalloc)
BuildRequires:      pkgconfig(libdrm)
BuildRequires:      pkgconfig(libpipewire-0.3)
BuildRequires:      pkgconfig(pam)
BuildRequires:      pkgconfig(wayland-client)
BuildRequires:      pkgconfig(wayland-protocols)
BuildRequires:      qt6-qtbase-private-devel
BuildRequires:      spirv-tools

%description

%prep
%autosetup -n %{name}-%{commit} -p1

%files
