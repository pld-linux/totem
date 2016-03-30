#
# Conditional build
%bcond_without	lirc		# without lirc support

Summary:	Movie player for GNOME based on the gstreamer engine
Summary(pl.UTF-8):	Odtwarzacz filmów dla GNOME oparty na silniku gstreamer
Name:		totem
Version:	3.20.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	e904a2513f28a79475541552c01b7ef9
# PLD-specific patches
Patch0:		%{name}-configure.patch
Patch1:		%{name}-python3.patch
URL:		https://wiki.gnome.org/Apps/Videos
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.14.0
BuildRequires:	clutter-devel >= 1.18.0
BuildRequires:	clutter-gst-devel >= 3.0.0
BuildRequires:	clutter-gtk-devel >= 1.5.5
BuildRequires:	docbook-dtd45-xml
BuildRequires:	gdk-pixbuf2-devel >= 2.24.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.36.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-doc-utils >= 0.20.3
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	grilo-devel >= 0.2.12
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.4.2
BuildRequires:	gstreamer-plugins-base-devel >= 1.4.2
BuildRequires:	gtk+3-devel >= 3.16.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libpeas-devel >= 1.1.0
BuildRequires:	libpeas-gtk-devel >= 1.1.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.31
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	pylint
BuildRequires:	python-devel >= 2.3
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info >= 0.22
BuildRequires:	totem-pl-parser-devel >= 3.10.1
BuildRequires:	vala >= 2:0.14.1
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
Requires(post,postun):	glib2 >= 1:2.28.0
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Requires:	clutter-gst >= 3.0.0
Requires:	glib2 >= 1:2.36.0
Requires:	gnome-icon-theme >= 3.0.0
Requires:	gstreamer-audiosink >= 1.4.2
Requires:	gstreamer-plugins-bad >= 1.4.2
Requires:	gstreamer-plugins-base >= 1.4.2
Requires:	gstreamer-plugins-good >= 1.4.2
Requires:	gstreamer-soundtouch >= 1.4.2
Requires:	gstreamer-soup >= 1.4.2
Requires:	gstreamer-videosink >= 1.4.2
Requires:	gstreamer-visualisation >= 1.4.2
Requires:	hicolor-icon-theme
Requires:	libpeas-loader-python3
Suggests:	gstreamer-libav
Suggests:	gstreamer-mpeg
Suggests:	gstreamer-pango
Suggests:	python3-dbus
Suggests:	python3-pygobject3 >= 3.0.0
Obsoletes:	browser-plugin-totem < 3.14.1-1
Obsoletes:	mozilla-firefox-plugin-totem < 3.14.1-1
Obsoletes:	mozilla-plugin-totem < 3.14.1-1
Obsoletes:	totem-iplayer
Obsoletes:	totem-jamendo
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
Requires:	gtk+3 >= 3.16.0
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
Requires:	glib2-devel >= 1:2.36.0
Requires:	gtk+3-devel >= 3.16.0
Requires:	totem-pl-parser-devel >= 3.10.1

%description devel
This package contains the files necessary to develop applications
using Totem's libraries.

%description devel -l pl.UTF-8
Pakiet zawiera pliki potrzebne do rozwoju aplikacji używających
bibliotek programu Totem.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos necessários para desenvolvimento de
aplicações utilizando as bibliotecas do Totem.

%package static
Summary:	Static libraries for totem
Summary(pl.UTF-8):	Biblioteki statyczne dla totem
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libraries for Totem.

%description static -l pl.UTF-8
Pakiet zawiera statyczne biblioteki Totem.

%package im-status
Summary:	Instant Messenger status plugin for Totem
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Obsoletes:	totem-galago

%description im-status
This package provides a plugin to set your Instant Messenger status to
away when a movie is playing.

%package gromit
Summary:	Gromit Annotations plugin for Totem
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	gromit

%description gromit
This package provides a plugin to make annotations on screen.

%package lirc
Summary:	LIRC (Infrared remote) plugin for Totem
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description lirc
This package provides a plugin to add LIRC (Infrared remote) support
to Totem.

%package opensubtitles
Summary:	Subtitle Downloader plugin for Totem
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	libpeas >= 1.1.0
Requires:	python3-pygobject3

%description opensubtitles
This package provides a plugin to look for subtitles for the currently
playing movie.

%package youtube
Summary:	YouTube plugin for Totem
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-ffmpeg
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-x264

%description youtube
This package provides a plugin to allow browsing YouTube videos in
Totem, and watching them.

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

%package -n nautilus-totem
Summary:	Video and Audio Properties tab for Nautilus
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 3.0.0

%description -n nautilus-totem
This package provides a Nautilus extension that shows the properties
of audio and video files in the properties dialog.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-nautilus \
	--enable-python \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p"

%{__rm}	$RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.{la,a} \
	$RPM_BUILD_ROOT%{_libdir}/totem/plugins/*/*.{la,a} \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%glib_compile_schemas
%scrollkeeper_update_postun
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/totem
%attr(755,root,root) %{_bindir}/totem-audio-preview
%attr(755,root,root) %{_bindir}/totem-video-thumbnailer
%{_datadir}/appdata/org.gnome.Totem.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Totem.service
%{_datadir}/%{name}
%{_desktopdir}/org.gnome.Totem.desktop
%{_mandir}/man1/totem.1*
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_iconsdir}/hicolor/*/*/*.png
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

%dir %{pluginsdir}/brasero-disc-recorder
%attr(755,root,root) %{pluginsdir}/brasero-disc-recorder/libbrasero-disc-recorder.so
%{pluginsdir}/brasero-disc-recorder/brasero-disc-recorder.plugin

%dir %{pluginsdir}/dbus
%{pluginsdir}/dbus/__pycache__
%{pluginsdir}/dbus/*.py
%{pluginsdir}/dbus/dbusservice.plugin

%dir %{pluginsdir}/media-player-keys
%attr(755,root,root) %{pluginsdir}/media-player-keys/libmedia_player_keys.so
%{pluginsdir}/media-player-keys/media-player-keys.plugin

%dir %{pluginsdir}/ontop
%attr(755,root,root) %{pluginsdir}/ontop/libontop.so
%{pluginsdir}/ontop/ontop.plugin

%dir %{pluginsdir}/properties
%attr(755,root,root) %{pluginsdir}/properties/libmovie-properties.so
%{pluginsdir}/properties/movie-properties.plugin

%dir %{pluginsdir}/pythonconsole
%{pluginsdir}/pythonconsole/__pycache__
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

%dir %{pluginsdir}/vimeo
%attr(755,root,root) %{pluginsdir}/vimeo/libvimeo.so
%{pluginsdir}/vimeo/vimeo.plugin

%dir %{pluginsdir}/zeitgeist-dp
%attr(755,root,root) %{pluginsdir}/zeitgeist-dp/libtotem-zeitgeist-dp-plugin.so
%{pluginsdir}/zeitgeist-dp/zeitgeist-dp.plugin

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

%files static
%defattr(644,root,root,755)
%{_libdir}/libtotem.a

%files im-status
%defattr(644,root,root,755)
%dir %{pluginsdir}/im-status
%attr(755,root,root) %{pluginsdir}/im-status/libtotem-im-status.so
%{pluginsdir}/im-status/totem-im-status.plugin

%files gromit
%defattr(644,root,root,755)
%dir %{pluginsdir}/gromit
%attr(755,root,root) %{pluginsdir}/gromit/libgromit.so
%{pluginsdir}/gromit/gromit.plugin

%files lirc
%defattr(644,root,root,755)
%dir %{pluginsdir}/lirc
%attr(755,root,root) %{pluginsdir}/lirc/liblirc.so
%{pluginsdir}/lirc/lirc.plugin
%{pluginsdir}/lirc/totem_lirc_default

%files opensubtitles
%defattr(644,root,root,755)
%dir %{pluginsdir}/opensubtitles
%{pluginsdir}/opensubtitles/__pycache__
%{pluginsdir}/opensubtitles/*.py
%{pluginsdir}/opensubtitles/opensubtitles.plugin
%{pluginsdir}/opensubtitles/opensubtitles.ui
%{_datadir}/glib-2.0/schemas/org.gnome.totem.plugins.opensubtitles.gschema.xml
%{_datadir}/GConf/gsettings/opensubtitles.convert

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/totem

%files -n nautilus-totem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libtotem-properties-page.so
