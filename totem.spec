#
# TODO:
# - what more bowsers can be supported?
#
# Conditional build
%bcond_with	gstreamer	# build with gstreamer instead xine-lib
%bcond_without	mozilla_firefox	# build with mozilla-firefox
%bcond_without	nvtv		# build without nvtv support
#
# nvtv only available on few archs
%ifnarch alpha arm %{ix86} ia64 sh %{x8664}
%undefine	with_nvtv
%endif
#
Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl):	Odtwarzacz filmów dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	1.4.3
Release:	4
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/totem/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	971f99d769cb865f9a6b55284357f415
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-idl.patch
Patch2:		%{name}-mozilla_includes.patch
Patch3:		%{name}-configure.patch
Patch4:		%{name}-codecs_path.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gnome-desktop-devel >= 2.14.0
BuildRequires:	gnome-vfs2-devel >= 2.14.0
BuildRequires:	rpmbuild(macros) >= 1.236
%if %{with gstreamer}
BuildRequires:	gstreamer-plugins-base-devel >= 0.10
%endif
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	intltool >= 0.34
BuildRequires:	iso-codes
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libmusicbrainz-devel
%{?with_nvtv:BuildRequires:	libnvtvsimple-devel >= 0.4.5}
BuildRequires:	libtool
BuildRequires:	lirc-devel
%if %{with mozilla_firefox}
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	mozilla-devel >= 5:1.7.13-2
%endif
BuildRequires:	nautilus-cd-burner-devel >= 2.14.0
BuildRequires:	nautilus-devel >= 2.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0.2-1}
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
Requires:	XFree86-libs >= 4.3.0-1.3
%if %{with gstreamer}
Requires:	gstreamer-GConf >= 0.10
Requires:	gstreamer-audiosink >= 0.10
Requires:	gstreamer-videosink >= 0.10
%else
Requires:	xine-plugin-video
# not usable
Conflicts:	xine-input-gnome-vfs <= 1.1.1
%endif
Requires:	gtk+2 >= 2:2.8.3
%if %{with mozilla_firefox}
%requires_eq	mozilla-firefox
%else
%endif
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
Requires:	gnome-desktop-libs >= 2.14.0
Requires:	nautilus-libs >= 2.14.0

%description libs
Totem shared libraries.

%description libs -l pl
Wspó³dzielone biblioteki Totema.

%package devel
Summary:	Totem include files
Summary(pl):	Pliki nag³ówkowe Totema
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.8.3

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
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-lirc \
	--enable-mozilla \
	--enable-nautilus \
	%{?with_nvtv:--enable-nvtv} \
	%{?with_gstreamer:--enable-gstreamer=0.10}

%{__make} \
%if %{with mozilla_firefox}
	MOZILLA_IDLDIR="%{_includedir}/mozilla-firefox/idl"
%else
	MOZILLA_IDLDIR="%{_includedir}/mozilla/idl"
%endif


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_plugindir} \
	typelibdir=%{_plugindir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_plugindir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.{la,a}

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install totem-handlers.schemas
%gconf_schema_install totem-video-thumbnail.schemas
%gconf_schema_install totem.schemas
%scrollkeeper_update_post
%update_desktop_database_post

%preun
%gconf_schema_uninstall totem-handlers.schemas
%gconf_schema_uninstall totem-video-thumbnail.schemas
%gconf_schema_uninstall totem.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun

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
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/totem-handlers.schemas
%{_sysconfdir}/gconf/schemas/totem-video-thumbnail.schemas
%{_sysconfdir}/gconf/schemas/totem.schemas

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtotem-plparser.so.*.*.*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so

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
