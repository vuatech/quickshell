%global commit      eabf79ebb640dbfab6a3ff4639db65e64e05d941
%global snapdate    20250319

Name:               quickshell
Version:            0^%{snapdate}g%(c=%{commit}; echo ${c:0:7})
Release:            1
Summary:            Flexible QtQuick based desktop shell toolkit

License:            LGPL-3.0-only AND GPL-3.0-only
URL:                https://github.com/quickshell-mirror/quickshell
Source0:            %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Group:		Graphical desktop/Other

BuildSystem:	cmake
BuildOption:-DDISTRIBUTOR="OpenMandriva LX" BuildOption:-DISTRIBUTOR_DEBUGINFO_AVAILABLE=YES BuildOption:-DCMAKE_BUILD_TYPE=RelWithDebInfo BuildOption:-DINSTALL_QML_PREFIX="%{_qtdir}" BuildOption:-DINSTALL_QMLDIR="%{_qtdir}/qml"

BuildRequires:	qt6declarative
BuildRequires:  cmake(spirv-tools)
BuildRequires:  qtshadertools

Requires:   pkgconfig(cli11)
Requires:   pkgconfig(qt6base)
Requires:   pkgconfig(qt6svg)

%description

%prep
%autosetup -p1

%files
