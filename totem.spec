#
# Conditional build
%bcond_without	bemused		# build without bemused plugin
%bcond_without	gstreamer	# build with xine-lib instead of gstreamer
%bcond_without	nvtv		# build without nvtv support
%bcond_without	lirc		# without lirc support
#
# nvtv only available on few archs
%ifnarch alpha arm %{ix86} ia64 sh %{x8664}
%undefine	with_nvtv
%endif
#
Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl.UTF-8):	Odtwarzacz filmów dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	2.23.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	118b9b3030814872697505ef1e1b0b96
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-configure.patch
Patch2:		%{name}-codegen.patch
URL:		http://www.gnome.org/projects/totem/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
%{?with_bemused:BuildRequires:	bluez-libs-devel}
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gmyth-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-vfs2-devel >= 2.22.0
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-base-devel >= 0.10.12}
BuildRequires:	gtk+2-devel >= 2:2.12.8
BuildRequires:	intltool >= 0.36.2
BuildRequires:	iso-codes
BuildRequires:	libepc-ui-devel
BuildRequires:	libgalago-devel >= 0.5.2
BuildRequires:	libgnomeui-devel >= 2.22.01
%{?with_nvtv:BuildRequires:	libnvtvsimple-devel >= 0.4.5}
BuildRequires:	libtool
BuildRequires:	libtracker-devel
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	pkgconfig
BuildRequires:	python-pygtk-devel >= 2:2.12.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	shared-mime-info >= 0.22
BuildRequires:	startup-notification-devel >= 0.8
BuildRequires:	totem-pl-parser-devel >= 2.22.1
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0.2-1}
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel >= 1.0.1
BuildRequires:	xulrunner-devel >= 1.8.1.12-1.20080208.3
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
%if %{with gstreamer}
Requires:	gstreamer-GConf >= 0.10.3
Requires:	gstreamer-audiosink >= 0.10
Requires:	gstreamer-videosink >= 0.10
%else
Requires:	xine-plugin-video
# unusable
Conflicts:	xine-input-gnome-vfs
%endif
Requires:	gtk+2 >= 2:2.12.8
Requires:	nautilus >= 2.22.0
Suggests:	galago-daemon
Suggests:	gstreamer-ffmpeg
Suggests:	gstreamer-mpeg
Suggests:	gstreamer-pango
# youtube plugin
Suggests:	gstreamer-plugins-bad
Suggests:	gstreamer-soup
Suggests:	python-gdata
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gstreamer}
%description
Totem is simple movie player for the GNOME desktop based on gstreamer.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl.UTF-8
Totem to prosty odtwarzacz filmów dla środowiska GNOME oparty na
gstreamer. Ma prostą listę odtwarzania, tryb pełnoekranowy, kontrolę
położenia w pliku i głośności, a także w miarę kompletną obsługę z
klawiatury.

%else
%description
Totem is simple movie player for the GNOME desktop based on xine-libs.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl.UTF-8
Totem to prosty odtwarzacz filmów dla środowiska GNOME oparty na
xine-libs. Ma prostą listę odtwarzania, tryb pełnoekranowy, kontrolę
położenia w pliku i głośności, a także w miarę kompletną obsługę z
klawiatury.
%endif

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
%patch2 -p1

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv po/sr@{Latn,latin}.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper \
	%{?with_lirc:--enable-lirc} \
	--enable-mozilla \
	--enable-nautilus \
	--%{?with_nvtv:enable}%{!?with_nvtv:disable}-nvtv \
	%{?with_gstreamer:--enable-gstreamer} \
	--with-gecko=xulrunner

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MOZILLA_PLUGINDIR=%{_browserpluginsdir} \
	typelibdir=%{_browserpluginsdir} \
	xptdir=%{_browserpluginsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/totem/plugins/*/*.{la,a}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install totem-handlers.schemas
%gconf_schema_install totem-mythtv.schemas
%gconf_schema_install totem-video-thumbnail.schemas
%gconf_schema_install totem.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall totem-handlers.schemas
%gconf_schema_uninstall totem-mythtv.schemas
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
%attr(755,root,root) %{_libdir}/libbaconvideowidget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbaconvideowidget.so.0
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libtotem-properties-page.so
%attr(755,root,root) %{_libdir}/totem/totem-bugreport.py
%{_datadir}/%{name}
%{_desktopdir}/totem.desktop
%{_mandir}/man1/totem.1*
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_iconsdir}/hicolor/*/*/totem.*
%{_sysconfdir}/gconf/schemas/totem-handlers.schemas
%{_sysconfdir}/gconf/schemas/totem-mythtv.schemas
%{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas
%{_sysconfdir}/gconf/schemas/totem.schemas
%dir %{_libdir}/totem
%dir %{_libdir}/totem/plugins
%if %{with bemused}
%dir %{_libdir}/totem/plugins/bemused
%attr(755,root,root) %{_libdir}/totem/plugins/bemused/libbemused.so
%endif
%dir %{_libdir}/totem/plugins/galago
%attr(755,root,root) %{_libdir}/totem/plugins/galago/libtgp.so
%{_libdir}/totem/plugins/galago/galago.totem-plugin
%dir %{_libdir}/totem/plugins/gromit
%attr(755,root,root) %{_libdir}/totem/plugins/gromit/libgromit.so
%{_libdir}/totem/plugins/gromit/gromit.totem-plugin
%dir %{_libdir}/totem/plugins/lirc
%attr(755,root,root) %{_libdir}/totem/plugins/lirc/liblirc.so
%{_libdir}/totem/plugins/lirc/lirc.totem-plugin
%dir %{_libdir}/totem/plugins/media-player-keys
%attr(755,root,root) %{_libdir}/totem/plugins/media-player-keys/libmedia_player_keys.so
%{_libdir}/totem/plugins/media-player-keys/media-player-keys.totem-plugin
%dir %{_libdir}/totem/plugins/mythtv
%attr(755,root,root) %{_libdir}/totem/plugins/mythtv/libtotem_mythtv.so
%{_libdir}/totem/plugins/mythtv/mythtv.totem-plugin
%dir %{_libdir}/totem/plugins/ontop
%attr(755,root,root) %{_libdir}/totem/plugins/ontop/libontop.so
%{_libdir}/totem/plugins/ontop/ontop.totem-plugin
%dir %{_libdir}/totem/plugins/properties
%attr(755,root,root) %{_libdir}/totem/plugins/properties/libmovie-properties.so
%{_libdir}/totem/plugins/properties/movie-properties.totem-plugin
%dir %{_libdir}/totem/plugins/publish
%attr(755,root,root) %{_libdir}/totem/plugins/publish/libpublish.so
%{_libdir}/totem/plugins/publish/publish-plugin.ui
%{_libdir}/totem/plugins/publish/publish.totem-plugin
%dir %{_libdir}/totem/plugins/screensaver
%attr(755,root,root) %{_libdir}/totem/plugins/screensaver/libscreensaver.so
%{_libdir}/totem/plugins/screensaver/screensaver.totem-plugin
%dir %{_libdir}/totem/plugins/skipto
%attr(755,root,root) %{_libdir}/totem/plugins/skipto/libskipto.so
%{_libdir}/totem/plugins/skipto/skipto.totem-plugin
%{_libdir}/totem/plugins/skipto/skipto.ui
%dir %{_libdir}/totem/plugins/thumbnail
%attr(755,root,root) %{_libdir}/totem/plugins/thumbnail/libthumbnail.so
%{_libdir}/totem/plugins/thumbnail/thumbnail.totem-plugin
%dir %{_libdir}/totem/plugins/totem
%{_libdir}/totem/plugins/totem/*.py[co]
%dir %{_libdir}/totem/plugins/tracker
%attr(755,root,root) %{_libdir}/totem/plugins/tracker/libtracker.so
%{_libdir}/totem/plugins/tracker/tracker.totem-plugin
%dir %{_libdir}/totem/plugins/youtube
%{_libdir}/totem/plugins/youtube/youtube.py[co]
%{_libdir}/totem/plugins/youtube/youtube.totem-plugin
%{_libdir}/totem/plugins/youtube/youtube.ui

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/totem-plugin-viewer
%attr(755,root,root) %{_browserpluginsdir}/*.so
%attr(755,root,root) %{_browserpluginsdir}/*.xpt
