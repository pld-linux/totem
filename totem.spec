#
# TODO:
# - what more bowsers can be supported?
#
# Conditional build
%bcond_without	gstreamer	# build with gstreamer instead xine-lib
%bcond_without	nvtv		# build without nvtv support
%bcond_without	lirc		# without lirc support
#
# nvtv only available on few archs
%ifnarch alpha arm %{ix86} ia64 sh %{x8664}
%undefine	with_nvtv
%endif
#
Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl):	Odtwarzacz filmów dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	1.5.90
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/totem/1.5/%{name}-%{version}.tar.bz2
# Source0-md5:	f4d03b463cfb08299b5bce75e3ed3ec1
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-idl.patch
Patch2:		%{name}-mozilla_includes.patch
Patch3:		%{name}-configure.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gnome-desktop-devel >= 2.15.90
BuildRequires:	gnome-vfs2-devel >= 2.15.90
BuildRequires:	rpmbuild(macros) >= 1.236
%if %{with gstreamer}
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.7
%endif
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool >= 0.35
BuildRequires:	iso-codes
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.90
BuildRequires:	libmusicbrainz-devel
%{?with_nvtv:BuildRequires:	libnvtvsimple-devel >= 0.4.5}
BuildRequires:	libtool
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	mozilla-firefox-devel
BuildRequires:	nautilus-cd-burner-devel >= 2.15.5
BuildRequires:	nautilus-devel >= 2.15.90
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0.2-1}
BuildRequires:	xorg-lib-libXv-devel
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2:2.10.1
Requires(post,postun):	scrollkeeper
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
Requires:	gtk+2 >= 2:2.10.1
Requires:	nautilus >= 2.15.90
%requires_eq	mozilla-firefox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/browser-plugins

# list of supported browsers, in free form text
%define		browsers	mozilla, mozilla-firefox, netscape, seamonkey

%if %{with gstreamer}
%description
Totem is simple movie player for the GNOME desktop based on gstreamer.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl
Totem to prosty odtwarzacz filmów dla ¶rodowiska GNOME oparty na
gstreamer. Ma prost± listê odtwarzania, tryb pe³noekranowy, kontrolê
po³o¿enia w pliku i g³o¶no¶ci, a tak¿e w miarê kompletn± obs³ugê z
klawiatury.

%else
%description
Totem is simple movie player for the GNOME desktop based on xine-libs.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl
Totem to prosty odtwarzacz filmów dla ¶rodowiska GNOME oparty na
xine-libs. Ma prost± listê odtwarzania, tryb pe³noekranowy, kontrolê
po³o¿enia w pliku i g³o¶no¶ci, a tak¿e w miarê kompletn± obs³ugê z
klawiatury.
%endif

%package libs
Summary:	Totem shared libraries
Summary(pl):	Wspó³dzielone biblioteki Totema
Group:		Libraries
Requires:	gnome-desktop-libs >= 2.15.90
Requires:	nautilus-libs >= 2.15.90

%description libs
Totem shared libraries.

%description libs -l pl
Wspó³dzielone biblioteki Totema.

%package devel
Summary:	Totem include files
Summary(pl):	Pliki nag³ówkowe Totema
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.1

%description devel
Totem headers files.

%description devel -l pl
Pliki nag³ówkowe Totema.

%package static
Summary:	Static Totem libraries
Summary(pl):	Statyczne biblioteki Totema
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Totem libraries.

%description static -l pl
Statyczne biblioteki Totema.

%package -n browser-plugin-%{name}
Summary:	Totem's browser plugin
Summary(pl):	Wtyczka Totema do przegl±darek WWW
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins(%{_target_base_arch})
Provides:	mozilla-firefox-plugin-totem
Provides:	mozilla-plugin-totem
Obsoletes:	mozilla-firefox-plugin-totem
Obsoletes:	mozilla-plugin-totem

%description -n browser-plugin-%{name}
Totem's plugin for browsers.

Supported browsers: %{browsers}.

%description -n browser-plugin-%{name} -l pl
Wtyczka Totem do przegl±darek WWW.

Obs³ugiwane przegl±darki: %{browsers}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{?with_lirc:--enable-lirc} \
	--enable-mozilla \
	--enable-nautilus \
	%{?with_nvtv:--enable-nvtv} \
	%{?with_gstreamer:--enable-gstreamer}

%{__make} \
	MOZILLA_IDLDIR="%{_includedir}/mozilla-firefox/idl"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_plugindir} \
	typelibdir=%{_plugindir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_plugindir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.{la,a}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ug

%find_lang %{name} --all-name --with-gnome

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

%triggerin -n browser-plugin-%{name} -- mozilla
%nsplugin_install -d %{_libdir}/mozilla/plugins libtotem_mozilla.{so,xpt}

%triggerun -n browser-plugin-%{name} -- mozilla
%nsplugin_uninstall -d %{_libdir}/mozilla/plugins libtotem_mozilla.{so,xpt}

%triggerin -n browser-plugin-%{name} -- mozilla-firefox
%nsplugin_install -d %{_libdir}/mozilla-firefox/plugins libtotem_mozilla.{so,xpt}

%triggerun -n browser-plugin-%{name} -- mozilla-forefox
%nsplugin_uninstall -d %{_libdir}/mozilla-firefox/plugins libtotem_mozilla.{so,xpt}

%triggerin -n browser-plugin-%{name} -- netscape-common
%nsplugin_install -d %{_libdir}/netscape/plugins libtotem_mozilla.{so,xpt}

%triggerun -n browser-plugin-%{name} -- netscape-common
%nsplugin_uninstall -d %{_libdir}/netscape/plugins libtotem_mozilla.{so,xpt}

%triggerin -n browser-plugin-%{name} -- seamonkey
%nsplugin_install -d %{_libdir}/seamonkey/plugins libtotem_mozilla.{so,xpt}

%triggerun -n browser-plugin-%{name} -- seamonkey
%nsplugin_uninstall -d %{_libdir}/seamonkey/plugins libtotem_mozilla.{so,xpt}

# as rpm removes the old obsoleted package files after the triggers
# are ran, add another trigger to make the links there.
%triggerpostun -n browser-plugin-%{name} -- mozilla-plugin-%{name}
%nsplugin_install -f -d %{_libdir}/mozilla/plugins libtotem_mozilla.{so,xpt}

%triggerpostun -n browser-plugin-%{name} -- mozilla-firefox-plugin-%{name}
%nsplugin_install -f -d %{_libdir}/netscape/plugins libtotem_mozilla.{so,xpt}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_iconsdir}/hicolor/*/*/media-player-48.png
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/totem-handlers.schemas
%{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas
%{_sysconfdir}/gconf/schemas/totem.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser.so
%{_libdir}/libtotem-plparser.la
%{_includedir}/totem
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtotem-plparser.a

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/totem-mozilla-viewer
%attr(755,root,root) %{_plugindir}/*.so
%attr(755,root,root) %{_plugindir}/*.xpt
