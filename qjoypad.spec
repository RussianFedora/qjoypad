Name: qjoypad
Version: 4.1.0
Release: 2%{?dist}
Summary: Remap joystick events as keyboard or mouse events

License: GPLv2
Url: http://qjoypad.sourceforge.net/
Source0: http://downloads.sourceforge.net/qjoypad/%{name}-%{version}.tar.gz
Source1: qjoypad.desktop
Patch0: fix_qt4.patch
Patch1: remove_docs.patch

BuildRequires: gcc-c++
BuildRequires: qt-devel
BuildRequires: desktop-file-utils
BuildRequires: libXtst-devel

%description
qjoypad a simple Linux/QT program that lets you use your gaming devices where you want them: in your games! QJoyPad takes input from a gamepad or joystick and translates it into key strokes or mouse actions, letting you control any XWindows program with your game controller.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export SUBLIBS="-lX11"
mkdir -p %{buildroot}
cd src
%configure  --prefix=%{_prefix} --install-dir=%{buildroot}
%make_build

%install
cd src
%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%clean
rm -rf %{buildroot}

%files
%doc LICENSE.txt README.txt
%{_bindir}/%{name}
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}/*
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Jan 19 2016 V1TSK <vitaly@easycoding.org> - 4.1.0-2
- Fixed build under Fedora 23+.

* Mon Nov 30 2009 tambet@novell.com - 4.1.0-1
- Initial import.
