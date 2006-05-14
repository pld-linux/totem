#
# TODO:
# - what more bowsers can be supported?
#
# Conditional build
%bcond_with	gstreamer	# build with gstreamer instead xine-lib
%bcond_with	mozilla_firefox	# build with mozilla-firefox
%bcond_without	nvtv		# build without nvtv support
#
# nvtv only available on few archs
%ifnarch alpha arm %{ix86} ia64 sh %{x8664}
%undefine		with_nvtv
%endif
#
Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl):	Odtwarzacz filmów dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/totem/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	a1ccda72948706edf13d2e1e69b48969
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-idl.patch
Patch2:		%{name}-mozilla_includes.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel >= 2.12.0
%if %{with gstreamer}
BuildRequires:	gstreamer-GConf-devel >= 0.8.11
BuildRequires:	gstreamer-devel >= 0.8.11
BuildRequires:	gstreamer-plugins-devel >= 0.8.11
%endif
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	intltool >= 0.34
BuildRequires:	iso-codes
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libmusicbrainz-devel
BuildRequires:	libtool
%{?with_nvtv:BuildRequires: libnvtvsimple-devel >= 0.4.5}
BuildRequires:	lirc-devel
%if %{with mozilla_firefox}
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	mozilla-devel >= 5:1.7.12
%endif
BuildRequires:	nautilus-cd-burner-devel >= 2.12.0
BuildRequires:	nautilus-devel >= 2.12.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0.2-1}
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Requires:	XFree86-libs >= 4.3.0-1.3
Requires:	gnome-desktop >= 2.12.0
%if %{with gstreamer}
Requires:	gstreamer-audiosink >= 0.8.11
Requires:	gstreamer-colorspace >= 0.8.11
Requires:	gstreamer-videosink >= 0.8.11
%else
Requires:	xine-plugin-video
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
Requires:	nautilus-libs >= 2.12.0

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

%package -n mozilla-firefox-plugin-totem
Summary:	Totem's plugin for Mozilla Firefox
Summary(pl):	Wtyczka Totema dla Mozilli Firefox
Group:		Libraries
%requires_eq	mozilla-firefox
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-firefox-plugin-totem
Totem's plugin for Mozilla Firefox.

%description -n mozilla-firefox-plugin-totem -l pl
Wtyczka Totema dla Mozilli Firefox.

%package -n mozilla-plugin-totem
Summary:	Totem's plugin for Mozilla
Summary(pl):	Wtyczka Totema dla Mozilli
Group:		Libraries
Requires:	mozilla-embedded = %(rpm -q --qf '%{EPOCH}:%{VERSION}' --whatprovides mozilla-embedded)
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-plugin-totem
Totem's plugin for Mozilla.

%description -n mozilla-plugin-totem -l pl
Wtyczka Totema dla Mozilli.

%package -n browser-plugin-%{name}
Summary:	Totem's browser plugin
Summary(pl):	Wtyczka Totema do przegl±darek WWW
Group:		X11/Libraries
Requires:	browser-plugins(%{_target_base_arch})
Requires:	%{name} = %{version}-%{release}
Provides:	mozilla-plugin-totem
Obsoletes:	mozilla-plugin-totem
Provides:	mozilla-firefox-plugin-totem
Obsoletes:	mozilla-firefox-plugin-totem

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
	%{?with_gstreamer:--enable-gstreamer}

%{__make} \
	MOZILLA_IDLDIR="%{_datadir}/idl"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_plugindir} \
	typelibdir=%{_plugindir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_plugindir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.{la,a}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

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
