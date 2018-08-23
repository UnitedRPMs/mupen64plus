%define debug_package %{nil}

Name:		mupen64plus
Version:	2.5
Release:	2%{?dist}

Summary:	Nintendo 64 Emulator (GTK Gui)
License:	GPLv2+
Group:		Emulators
URL:		http://code.google.com/p/mupen64plus/
Source0:	https://github.com/mupen64plus/mupen64plus-core/releases/download/%{version}/mupen64plus-bundle-src-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires:	SDL_ttf-devel
BuildRequires:	gtk2-devel
BuildRequires:	lirc-devel
BuildRequires:	desktop-file-utils

BuildRequires:	mesa-libGLU-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libpng-devel
BuildRequires:	SDL-devel
BuildRequires:	freetype-devel
BuildRequires:	boost-devel
BuildRequires:	gzip
BuildRequires:	glew-devel
BuildRequires:  binutils
BuildRequires:	nasm
BuildRequires:  gcc-c++

Requires:	SDL_ttf
Requires:	mesa-libGLU
Requires:	libsamplerate
Requires:	libpng
Requires:	SDL
Requires:	freetype
Requires:	boost

Conflicts:	mupen64plus-qt
Conflicts:	mupen64plus-cli

%description
Mupen64plus is a Nintendo 64 Emulator.
This package includes a GTK front-end and all the plug-ins.

%prep
%autosetup -n %{name}-bundle-src-%{version} 

%build

sh m64p_build.sh


%install

./m64p_install.sh DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} LIBDIR=%{_libdir} LDCONFIG='true'



%files
%defattr(755, root, root)
%{_bindir}/%{name}
%{_libdir}/mupen64plus/mupen64plus-audio-sdl.so
%{_libdir}/mupen64plus/mupen64plus-rsp-hle.so
%{_libdir}/mupen64plus/mupen64plus-video-rice.so
%{_libdir}/mupen64plus/mupen64plus-input-sdl.so
%{_libdir}/libmupen64plus.so.2
%{_libdir}/libmupen64plus.so.2.0.0
%{_libdir}/mupen64plus/mupen64plus-video-glide64mk2.so
%{_datadir}/%{name}/
%{_datadir}/applications/mupen64plus.desktop
%{_datadir}/icons/hicolor/48x48/apps/mupen64plus.png
%{_datadir}/icons/hicolor/scalable/apps/mupen64plus.svg
%{_mandir}/man6/mupen64plus.6.gz
%{_includedir}/mupen64plus/

%changelog

* Wed Jul 05 2017 David Vásquez <davidjeremias82[AT]gmail [DOT] com> -2.5-2
- Rebuilt

* Fri Oct 02 2015 David Vásquez <davidjeremias82[AT]gmail [DOT] com> -2.5-1
- Updated to 2.5

* Fri Jul 04 2014 David Vásquez <davidjeremias82[AT]gmail [DOT] com> - 2.0-6
- Excluded innecesary sources

* Fri Nov 22 2013 David Vasquez <davidjeremias82[AT]gmail [DOT] com> 2.0-5
- Added Modules Input SDL

* Wed Sep 25 2013 David Vasquez <davidjeremias82[AT]gmail [DOT] com> 2.0-4
- Initial build rpm
