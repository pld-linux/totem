#
# Conditional build
%bcond_without	bemused		# build without bemused plugin
%bcond_without	lirc		# without lirc support
#
Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl.UTF-8):	Odtwarzacz filmów dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	2.28.5
Release:	3
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	03b43f3c3a93b6dbcf1d1b370cc9297f
# PLD-specific patches
Patch0:		%{name}-configure.patch
Patch1:		%{name}-codegen.patch
URL:		http://www.gnome.org/projects/totem/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
%{?with_bemused:BuildRequires:	bluez-libs-devel}
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd45-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gmyth-devel >= 0.7.1
BuildRequires:	gmyth-upnp-devel >= 0.7.1
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.24
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-doc >= 1.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes
BuildRequires:	libepc-ui-devel >= 0.3.0
BuildRequires:	libgalago-devel >= 0.5.2
BuildRequires:	libgdata-devel >= 0.4.0
BuildRequires:	libtool
BuildRequires:	libtracker-devel
BuildRequires:	libunique-devel
BuildRequires:	libxml2-devel >= 1:2.6.31
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	nautilus-devel >= 2.26.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info >= 0.22
BuildRequires:	totem-pl-parser-devel >= 2.28.0
BuildRequires:	vala >= 0.3.5
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel >= 1.0.1
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gstreamer-GConf >= 0.10.3
Requires:	gstreamer-audiosink >= 0.10
Requires:	gstreamer-plugins-base >= 0.10.24
Requires:	gstreamer-soup
Requires:	gstreamer-videosink >= 0.10
Requires:	gtk+2 >= 2:2.16.0
Requires:	nautilus >= 2.26.0
Requires:	python-pygtk-gtk
Suggests:	galago-daemon
Suggests:	gstreamer-ffmpeg
Suggests:	gstreamer-mpeg
Suggests:	gstreamer-pango
# youtube plugin
Suggests:	gstreamer-plugins-bad
Suggests:	python-BeautifulSoup
Suggests:	python-coherence
Suggests:	python-feedparser
Suggests:	python-gnome-gconf
Suggests:	python-httplib2
Suggests:	python-json-py
Suggests:	python-listparser
Suggests:	python-pygobject >= 2.16.0
Suggests:	python-pyxdg
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

%package apidocs
Summary:	Totem API documentation
Summary(pl.UTF-8):	Dokumentacja API Totema
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Totem API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Totema.

%package -n browser-plugin-%{name}
Summary:	Totem's browser plugin
Summary(pl.UTF-8):	Wtyczka Totema do przeglądarek WWW
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	mozilla-firefox-plugin-totem
Provides:	mozilla-plugin-totem
Obsoletes:	mozilla-firefox-plugin-totem
Obsoletes:	mozilla-plugin-totem

%description -n browser-plugin-%{name}
Totem's plugin for browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka Totem do przeglądarek WWW.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper \
	--disable-vala \
	--enable-nautilus \
	--enable-python \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BROWSER_PLUGIN_DIR=%{_browserpluginsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/totem/plugins/*/*.{la,a}

%py_postclean %{_libdir}/totem/plugins

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install totem-handlers.schemas
%gconf_schema_install totem-video-thumbnail.schemas
%gconf_schema_install totem.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall totem-handlers.schemas
%gconf_schema_uninstall totem-video-thumbnail.schemas
%gconf_schema_uninstall totem.schemas

%postun
/sbin/ldconfig
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/totem
%attr(755,root,root) %{_bindir}/totem-audio-preview
%attr(755,root,root) %{_bindir}/totem-video-indexer
%attr(755,root,root) %{_bindir}/totem-video-thumbnailer
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libtotem-properties-page.so
%attr(755,root,root) %{_libdir}/totem/totem-bugreport.py
%{_datadir}/%{name}
%{_desktopdir}/totem.desktop
%{_mandir}/man1/totem.1*
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_sysconfdir}/gconf/schemas/totem-handlers.schemas
%{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas
%{_sysconfdir}/gconf/schemas/totem.schemas
%dir %{_libdir}/totem
%dir %{pluginsdir}

%if %{with bemused}
%dir %{pluginsdir}/bemused
%attr(755,root,root) %{pluginsdir}/bemused/libbemused.so
%endif

%dir %{pluginsdir}/brasero-disc-recorder
%attr(755,root,root) %{pluginsdir}/brasero-disc-recorder/libbrasero-disc-recorder.so
%{pluginsdir}/brasero-disc-recorder/brasero-disc-recorder.totem-plugin

%dir %{pluginsdir}/coherence_upnp
%{pluginsdir}/coherence_upnp/*.py[co]
%{pluginsdir}/coherence_upnp/coherence_upnp.totem-plugin

%dir %{pluginsdir}/dbus
%{pluginsdir}/dbus/*.py[co]
%{pluginsdir}/dbus/dbus-service.totem-plugin

%dir %{pluginsdir}/galago
%attr(755,root,root) %{pluginsdir}/galago/libtgp.so
%{pluginsdir}/galago/galago.totem-plugin

%dir %{pluginsdir}/gromit
%attr(755,root,root) %{pluginsdir}/gromit/libgromit.so
%{pluginsdir}/gromit/gromit.totem-plugin

%dir %{pluginsdir}/iplayer
%{pluginsdir}/iplayer/*.py[co]
%{pluginsdir}/iplayer/iplayer.ui
%{pluginsdir}/iplayer/iplayer.totem-plugin

%dir %{pluginsdir}/jamendo
%{pluginsdir}/jamendo/*.py[co]
%{pluginsdir}/jamendo/jamendo.totem-plugin
%{pluginsdir}/jamendo/jamendo.ui

%dir %{pluginsdir}/lirc
%attr(755,root,root) %{pluginsdir}/lirc/liblirc.so
%{pluginsdir}/lirc/lirc.totem-plugin
%{pluginsdir}/lirc/totem_lirc_default

%dir %{pluginsdir}/media-player-keys
%attr(755,root,root) %{pluginsdir}/media-player-keys/libmedia_player_keys.so
%{pluginsdir}/media-player-keys/media-player-keys.totem-plugin

%dir %{pluginsdir}/mythtv
%attr(755,root,root) %{pluginsdir}/mythtv/libtotem_mythtv.so
%{pluginsdir}/mythtv/mythtv.totem-plugin

%dir %{pluginsdir}/ontop
%attr(755,root,root) %{pluginsdir}/ontop/libontop.so
%{pluginsdir}/ontop/ontop.totem-plugin

%dir %{pluginsdir}/opensubtitles
%{pluginsdir}/opensubtitles/*.py[co]
%{pluginsdir}/opensubtitles/opensubtitles.totem-plugin
%{pluginsdir}/opensubtitles/opensubtitles.ui

%dir %{pluginsdir}/properties
%attr(755,root,root) %{pluginsdir}/properties/libmovie-properties.so
%{pluginsdir}/properties/movie-properties.totem-plugin

%dir %{pluginsdir}/publish
%attr(755,root,root) %{pluginsdir}/publish/libpublish.so
%{pluginsdir}/publish/publish-plugin.ui
%{pluginsdir}/publish/publish.totem-plugin

%dir %{pluginsdir}/pythonconsole
%{pluginsdir}/pythonconsole/console.py[co]
%{pluginsdir}/pythonconsole/pythonconsole.py[co]
%{pluginsdir}/pythonconsole/pythonconsole.totem-plugin

%dir %{pluginsdir}/screensaver
%attr(755,root,root) %{pluginsdir}/screensaver/libscreensaver.so
%{pluginsdir}/screensaver/screensaver.totem-plugin

%dir %{pluginsdir}/screenshot
%attr(755,root,root) %{pluginsdir}/screenshot/libscreenshot.so
%{pluginsdir}/screenshot/gallery.ui
%{pluginsdir}/screenshot/gnome-screenshot.ui
%{pluginsdir}/screenshot/screenshot.totem-plugin

%dir %{pluginsdir}/skipto
%attr(755,root,root) %{pluginsdir}/skipto/libskipto.so
%{pluginsdir}/skipto/skipto.totem-plugin
%{pluginsdir}/skipto/skipto.ui

%dir %{pluginsdir}/thumbnail
%attr(755,root,root) %{pluginsdir}/thumbnail/libthumbnail.so
%{pluginsdir}/thumbnail/thumbnail.totem-plugin

%dir %{pluginsdir}/tracker
%attr(755,root,root) %{pluginsdir}/tracker/libtracker.so
%{pluginsdir}/tracker/tracker.totem-plugin

%dir %{pluginsdir}/totem
%{pluginsdir}/totem/__init__.py[co]

%dir %{pluginsdir}/youtube
%attr(755,root,root) %{pluginsdir}/youtube/libyoutube.so
%{pluginsdir}/youtube/youtube.totem-plugin
%{pluginsdir}/youtube/youtube.ui

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/totem

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/totem-plugin-viewer
%attr(755,root,root) %{_browserpluginsdir}/*.so
