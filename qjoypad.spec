Name: qjoypad
Version: 4.3.0
Release: 1%{?dist}
Summary: Remap joystick events as keyboard or mouse events

License: GPLv2
Url: https://github.com/panzi/qjoypad
Source0: https://github.com/panzi/qjoypad/archive/v%{version}.tar.gz#/qjoypad-%{version}.tar.gz

BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(xtst)

BuildRequires: desktop-file-utils
BuildRequires: qt5-linguist
BuildRequires: gcc-c++
BuildRequires: cmake

%description
QJoyPad takes input from a gamepad or joystick and translates it into key
strokes or mouse actions, letting you control any XWindows program with your
game controller.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake .
%make_build

%install
%make_install
%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%doc README.md INSTALL.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Apr 03 2016 V1TSK <vitaly@easycoding.org> - 4.3.0-1
* Updated to 4.3.0.

* Sat Jan 23 2016 V1TSK <vitaly@easycoding.org> - 4.2.1-2.20160123git0e9145f
- Updated to latest Git release with Qt5 support.

* Sat Jan 23 2016 V1TSK <vitaly@easycoding.org> - 4.2.1-1
- Changed source to fork. Updated SPEC file.

* Tue Jan 19 2016 V1TSK <vitaly@easycoding.org> - 4.1.0-2
- Fixed build under Fedora 23+.

* Mon Nov 30 2009 tambet@novell.com - 4.1.0-1
- Initial import.
