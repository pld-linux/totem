#
# Conditional build
%bcond_without	lirc		# without lirc support

Summary:	Movie player for GNOME based on the gstreamer engine
Summary(pl.UTF-8):	Odtwarzacz filmów dla GNOME oparty na silniku gstreamer
Name:		totem
Version:	3.34.1
Release:	4
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	7f8e99c8f59cf4e53f185cc6b0e7f017
# PLD-specific patches
Patch10:	%{name}-configure.patch
URL:		https://wiki.gnome.org/Apps/Videos
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	clutter-devel >= 1.18.0
BuildRequires:	clutter-gst-devel >= 3.0.0
BuildRequires:	clutter-gtk-devel >= 1.8.1
BuildRequires:	docbook-dtd45-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.24.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-desktop-devel
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	grilo-devel >= 0.3.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.6.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.6.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libpeas-devel >= 1.1.0
BuildRequires:	libpeas-gtk-devel >= 1.1.0
BuildRequires:	libxml2-devel >= 1:2.6.31
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	py3lint >= 2.4.4
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info >= 0.22
BuildRequires:	totem-pl-parser-devel >= 3.10.1
BuildRequires:	vala >= 2:0.14.1
BuildRequires:	vala-zeitgeist
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.1.1
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libXxf86vm-devel >= 1.0.1
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	zeitgeist-devel >= 0.9.12
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	clutter-gst >= 3.0.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-icon-theme >= 3.0.0
Requires:	gstreamer-audiosink >= 1.6.0
Requires:	gstreamer-plugins-bad >= 1.6.0
Requires:	gstreamer-plugins-base >= 1.6.0
Requires:	gstreamer-plugins-good >= 1.6.0
Requires:	gstreamer-soundtouch >= 1.6.0
Requires:	gstreamer-soup >= 1.6.0
Requires:	gstreamer-videosink >= 1.6.0
Requires:	gstreamer-visualisation >= 1.6.0
Requires:	hicolor-icon-theme
Requires:	libpeas-loader-python3 >= 1.1.0
Suggests:	gstreamer-libav >= 1.6.0
Suggests:	gstreamer-mpeg >= 1.6.0
Suggests:	gstreamer-pango >= 1.6.0
Suggests:	python3-dbus
Suggests:	python3-pygobject3 >= 3.0.0
Obsoletes:	browser-plugin-totem < 3.14.1-1
Obsoletes:	mozilla-firefox-plugin-totem < 3.14.1-1
Obsoletes:	mozilla-plugin-totem < 3.14.1-1
Obsoletes:	nautilus-totem
Obsoletes:	totem-gromit
Obsoletes:	totem-iplayer
Obsoletes:	totem-jamendo
Obsoletes:	totem-lirc
Obsoletes:	totem-publish
Obsoletes:	totem-tracker
Obsoletes:	totem-upnp
Obsoletes:	totem-youtube
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		pluginsdir	%{_libdir}/totem/plugins

%description
Totem is simple movie player for the GNOME desktop based on gstreamer.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl.UTF-8
Totem to prosty odtwarzacz filmów dla środowiska GNOME oparty na
gstreamer. Ma prostą listę odtwarzania, tryb pełnoekranowy, kontrolę
położenia w pliku i głośności, a także w miarę kompletną obsługę z
klawiatury.

%package libs
Summary:	Totem libraries
Summary(pl.UTF-8):	Biblioteki Totem
Group:		X11/Libraries
Requires:	gtk+3 >= 3.20.0
Requires:	totem-pl-parser >= 3.10.1

%description libs
This package contains Totem libraries.

%description libs -l pl.UTF-8
Pakiet zawiera biblioteki Totem.

%package devel
Summary:	Header files for totem
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44.0
Requires:	gtk+3-devel >= 3.20.0
Requires:	totem-pl-parser-devel >= 3.10.1
Obsoletes:	totem-static < 3.26.0

%description devel
This package contains the files necessary to develop applications
using Totem's libraries.

%description devel -l pl.UTF-8
Pakiet zawiera pliki potrzebne do rozwoju aplikacji używających
bibliotek programu Totem.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos necessários para desenvolvimento de
aplicações utilizando as bibliotecas do Totem.

%package im-status
Summary:	Instant Messenger status plugin for Totem
Summary(pl.UTF-8):	Wtyczka Totema obsługująca stan na komunikatorze
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Obsoletes:	totem-galago

%description im-status
This package provides a plugin to set your Instant Messenger status to
away when a movie is playing.

%description im-status -l pl.UTF-8
Ten pakiet zawiera wtyczkę ustawiającą stan na komunikatorze na
nieobecny ("away"), kiedy odtwarzany jest film.

%package opensubtitles
Summary:	Subtitle Downloader plugin for Totem
Summary(pl.UTF-8):	Wtyczka Totema ściągająca napisy
Group:		Applications/Multimedia
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	%{name} = %{version}-%{release}
Requires:	libpeas >= 1.1.0
Requires:	python3-pygobject3

%description opensubtitles
This package provides a plugin to look for subtitles for the currently
playing movie.

%description opensubtitles -l pl.UTF-8
Ten pakiet zawiera wtyczkę wyszukującą napisy do aktualnie
odtwarzanego filmu.

%package youtube
Summary:	YouTube plugin for Totem
Summary(pl.UTF-8):	Wtyczka Totema obsługująca YouTube
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-libav >= 1.6.0
Requires:	gstreamer-plugins-bad >= 1.6.0
Requires:	gstreamer-x264 >= 1.6.0

%description youtube
This package provides a plugin to allow browsing YouTube videos in
Totem, and watching them.

%description youtube -l pl.UTF-8
Ten pakiet zawiera wtyczkę pozwalającą na przeglądanie w Totemie
filmów z YouTube'a i oglądanie ich.

%package apidocs
Summary:	Totem API documentation
Summary(pl.UTF-8):	Dokumentacja API Totema
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Totem API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Totema.

%prep
%setup -q
%patch10 -p1

%build
%meson build \
	-Denable-python=yes \
	-Denable-gtk-doc=true

# work-around for https://github.com/mesonbuild/meson/issues/1994
%meson_build -C build src/Totem-1.0.gir
%meson_build -C build -j1

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%glib_compile_schemas
%update_desktop_database_postun
%update_icon_cache hicolor

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post opensubtitles
%glib_compile_schemas

%postun opensubtitles
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/totem
%attr(755,root,root) %{_bindir}/totem-video-thumbnailer
%attr(755,root,root) %{_libexecdir}/totem-gallery-thumbnailer
%{_datadir}/metainfo/org.gnome.Totem.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Totem.service
%{_datadir}/%{name}
%{_desktopdir}/org.gnome.Totem.desktop
%{_mandir}/man1/totem.1*
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/glib-2.0/schemas/org.gnome.totem.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.totem.gschema.xml
%{_datadir}/GConf/gsettings/totem.convert
%dir %{_libdir}/totem
%dir %{pluginsdir}

%dir %{pluginsdir}/apple-trailers
%{pluginsdir}/apple-trailers/apple-trailers.plugin
%attr(755,root,root) %{pluginsdir}/apple-trailers/libapple-trailers.so

%dir %{pluginsdir}/autoload-subtitles
%{pluginsdir}/autoload-subtitles/autoload-subtitles.plugin
%attr(755,root,root) %{pluginsdir}/autoload-subtitles/libautoload-subtitles.so

%dir %{pluginsdir}/dbus
%{pluginsdir}/dbus/*.py
%{pluginsdir}/dbus/dbusservice.plugin

%dir %{pluginsdir}/media-player-keys
%attr(755,root,root) %{pluginsdir}/media-player-keys/libmedia-player-keys.so
%{pluginsdir}/media-player-keys/media-player-keys.plugin

%dir %{pluginsdir}/open-directory
%attr(755,root,root) %{pluginsdir}/open-directory/libopen-directory.so
%{pluginsdir}/open-directory/open-directory.plugin

%dir %{pluginsdir}/properties
%attr(755,root,root) %{pluginsdir}/properties/libmovie-properties.so
%{pluginsdir}/properties/movie-properties.plugin

%dir %{pluginsdir}/pythonconsole
%{pluginsdir}/pythonconsole/console.py
%{pluginsdir}/pythonconsole/pythonconsole.py
%{pluginsdir}/pythonconsole/pythonconsole.plugin
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.pythonconsole.gschema.xml
%{_datadir}/GConf/gsettings/pythonconsole.convert

%dir %{pluginsdir}/recent
%attr(755,root,root) %{pluginsdir}/recent/librecent.so
%{pluginsdir}/recent/recent.plugin

%dir %{pluginsdir}/rotation
%attr(755,root,root) %{pluginsdir}/rotation/librotation.so
%{pluginsdir}/rotation/rotation.plugin

%dir %{pluginsdir}/save-file
%attr(755,root,root) %{pluginsdir}/save-file/libsave-file.so
%{pluginsdir}/save-file/save-file.plugin

%dir %{pluginsdir}/screensaver
%attr(755,root,root) %{pluginsdir}/screensaver/libscreensaver.so
%{pluginsdir}/screensaver/screensaver.plugin

%dir %{pluginsdir}/screenshot
%attr(755,root,root) %{pluginsdir}/screenshot/libscreenshot.so
%{pluginsdir}/screenshot/gallery.ui
%{pluginsdir}/screenshot/screenshot.plugin

%dir %{pluginsdir}/skipto
%attr(755,root,root) %{pluginsdir}/skipto/libskipto.so
%{pluginsdir}/skipto/skipto.plugin
%{pluginsdir}/skipto/skipto.ui

%{_datadir}/thumbnailers/totem.thumbnailer

%dir %{pluginsdir}/variable-rate
%attr(755,root,root) %{pluginsdir}/variable-rate/libvariable-rate.so
%{pluginsdir}/variable-rate/variable-rate.plugin

%dir %{pluginsdir}/vimeo
%attr(755,root,root) %{pluginsdir}/vimeo/libvimeo.so
%{pluginsdir}/vimeo/vimeo.plugin

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtotem.so.0
%{_libdir}/girepository-1.0/Totem-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem.so
%{_includedir}/totem
%{_pkgconfigdir}/totem.pc
%{_datadir}/gir-1.0/Totem-1.0.gir

%files im-status
%defattr(644,root,root,755)
%dir %{pluginsdir}/im-status
%attr(755,root,root) %{pluginsdir}/im-status/libtotem-im-status.so
%{pluginsdir}/im-status/totem-im-status.plugin

%files opensubtitles
%defattr(644,root,root,755)
%dir %{pluginsdir}/opensubtitles
%{pluginsdir}/opensubtitles/*.py
%{pluginsdir}/opensubtitles/opensubtitles.plugin
%{pluginsdir}/opensubtitles/opensubtitles.ui
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.opensubtitles.gschema.xml
%{_datadir}/GConf/gsettings/opensubtitles.convert

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/totem
