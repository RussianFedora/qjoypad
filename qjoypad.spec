Name:           qjoypad
Version:        4.3.0
Release:        2%{?dist}
Summary:        Remap joystick events as keyboard or mouse events

License:        GPLv2+
URL:            https://github.com/panzi/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(libudev)
# linked by name
BuildRequires:  libXtst-devel
BuildRequires:  libX11-devel

BuildRequires:  /usr/bin/desktop-file-validate

Requires:       hicolor-icon-theme

%description
QJoyPad takes input from a gamepad or joystick and translates it into key
strokes or mouse actions, letting you control any XWindows program with your
game controller.

%prep
%autosetup
mkdir build

%build
pushd build
  %cmake ..
  %make_build
popd

%install
pushd build
  %make_install
popd
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
%license LICENSE.txt
%doc README.md INSTALL.txt
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Jun 26 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 4.3.0-2
- License actually is GPLv2+, not GPLv2
- Make out-of-tree builds
- Use cmake() style dependencies
- Add missing Requires: hicolor-icon-theme
- Trivial fixes

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
