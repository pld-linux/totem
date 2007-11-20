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
Version:	2.20.1
Release:	3
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/totem/2.20/%{name}-%{version}.tar.bz2
# Source0-md5:	6627727e7abd7a7f95257be8df6359a6
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-idl.patch
Patch2:		%{name}-configure.patch
Patch3:		%{name}-codegen.patch
URL:		http://www.gnome.org/projects/totem/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_bemused:BuildRequires:	bluez-libs-devel}
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	gnome-control-center-devel
BuildRequires:	gnome-desktop-devel >= 2.20.0
BuildRequires:	gnome-vfs2-devel >= 2.20.0
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10}
BuildRequires:	gtk+2-devel >= 2:2.12.1
BuildRequires:	intltool >= 0.36.2
BuildRequires:	iso-codes
BuildRequires:	libgalago-devel >= 0.5.2
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.20.0
BuildRequires:	libmusicbrainz-devel
%{?with_nvtv:BuildRequires:	libnvtvsimple-devel >= 0.4.5}
BuildRequires:	libtool
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	nautilus-cd-burner-devel >= 2.20.0
BuildRequires:	nautilus-devel >= 2.20.0
BuildRequires:	pkgconfig
# support for --with-omf in find_lang.sh
BuildRequires:	rpm-build >= 4.4.9-10
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	scrollkeeper
BuildRequires:	shared-mime-info >= 0.22
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0.2-1}
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86vm-devel >= 1.0.1
BuildRequires:	xulrunner-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
%if %{with gstreamer}
Requires:	gstreamer-GConf >= 0.10.3
Requires:	gstreamer-audiosink >= 0.10
Requires:	gstreamer-videosink >= 0.10
%else
Requires:	xine-plugin-video
# unusable
Conflicts:	xine-input-gnome-vfs
%endif
Requires:	gtk+2 >= 2:2.12.1
Requires:	nautilus >= 2.20.0
%requires_eq	xulrunner-libs
Suggests:	galago-daemon
Suggests:	gstreamer-ffmpeg
Suggests:	gstreamer-mpeg
Suggests:	gstreamer-pango
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

%package libs
Summary:	Totem shared libraries
Summary(pl.UTF-8):	Współdzielone biblioteki Totema
Group:		Libraries
Requires:	gnome-desktop-libs >= 2.20.0
Requires:	nautilus-libs >= 2.20.0

%description libs
Totem shared libraries.

%description libs -l pl.UTF-8
Współdzielone biblioteki Totema.

%package devel
Summary:	Totem include files
Summary(pl.UTF-8):	Pliki nagłówkowe Totema
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.12.1

%description devel
Totem headers files.

%description devel -l pl.UTF-8
Pliki nagłówkowe Totema.

%package static
Summary:	Static Totem libraries
Summary(pl.UTF-8):	Statyczne biblioteki Totema
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Totem libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Totema.

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
%patch3 -p1

sed -i -e s#sr\@Latn#sr\@latin# po/LINGUAS
mv po/sr\@{Latn,latin}.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper \
	%{?with_lirc:--enable-lirc} \
	--enable-mozilla \
	--enable-nautilus \
	--%{?with_nvtv:enable}%{!?with_nvtv:disable}-nvtv \
	%{?with_gstreamer:--enable-gstreamer}

%{__make} \
	MOZILLA_IDLDIR="%{_includedir}/xulrunner/idl"


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MOZILLA_PLUGINDIR=%{_browserpluginsdir} \
	typelibdir=%{_browserpluginsdir} \
	xptdir=%{_browserpluginsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/totem/plugins/*/*.{la,a}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
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
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

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
%attr(755,root,root) %{_bindir}/totem-video-indexer
%attr(755,root,root) %{_bindir}/totem-video-thumbnailer
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/libtotem-properties-page.so
%{_datadir}/%{name}
%{_desktopdir}/totem.desktop
%{_mandir}/man1/totem.1*
%{_mandir}/man1/totem-video-thumbnailer.1*
%{_iconsdir}/hicolor/*/*/totem.*
#%{_pixmapsdir}/vanity.png
%{_sysconfdir}/gconf/schemas/totem-handlers.schemas
%{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas
%{_sysconfdir}/gconf/schemas/totem.schemas
%dir %{_libdir}/totem
%dir %{_libdir}/totem/plugins
%{?with_bemused:%dir %{_libdir}/totem/plugins/bemused}
%dir %{_libdir}/totem/plugins/galago
%dir %{_libdir}/totem/plugins/gromit
%dir %{_libdir}/totem/plugins/lirc
%dir %{_libdir}/totem/plugins/media-player-keys
%dir %{_libdir}/totem/plugins/ontop
%dir %{_libdir}/totem/plugins/properties
%dir %{_libdir}/totem/plugins/screensaver
%dir %{_libdir}/totem/plugins/skipto
%attr(755,root,root) %{_libdir}/totem/plugins/*/*.so
%{_libdir}/totem/plugins/*/*.totem-plugin
%{_libdir}/totem/plugins/*/*.ui

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser.so
%{_libdir}/libtotem-plparser.la
%{_includedir}/totem
%{_pkgconfigdir}/totem-plparser.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtotem-plparser.a

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/totem-plugin-viewer
%attr(755,root,root) %{_browserpluginsdir}/*.so
%attr(755,root,root) %{_browserpluginsdir}/*.xpt
