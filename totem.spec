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
Summary(pl):	Odtwarzacz film�w dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	2.16.4
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/totem/2.16/%{name}-%{version}.tar.bz2
# Source0-md5:	dacfc1089125170bc47517c39fbc7828
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-idl.patch
Patch2:		%{name}-mozilla_includes.patch
Patch3:		%{name}-configure.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gnome-desktop-devel >= 2.16.2
BuildRequires:	gnome-vfs2-devel >= 2.16.3
%if %{with gstreamer}
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.10
%endif
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool >= 0.35.0
BuildRequires:	iso-codes
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libmusicbrainz-devel
%{?with_nvtv:BuildRequires:	libnvtvsimple-devel >= 0.4.5}
BuildRequires:	libtool
%{?with_lirc:BuildRequires:	lirc-devel}
BuildRequires:	xulrunner-devel
BuildRequires:	nautilus-cd-burner-devel >= 2.16.1
BuildRequires:	nautilus-devel >= 2.16.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	scrollkeeper
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0.2-1}
BuildRequires:	xorg-lib-libXv-devel
Requires(post,preun):	GConf2 >= 2.16.0
Requires(post,postun):	gtk+2 >= 2:2.10.6
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
Requires:	gtk+2 >= 2:2.10.6
Requires:	hicolor-icon-theme
Requires:	nautilus >= 2.16.3
%requires_eq	xulrunner-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%if %{with gstreamer}
%description
Totem is simple movie player for the GNOME desktop based on gstreamer.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl
Totem to prosty odtwarzacz film�w dla �rodowiska GNOME oparty na
gstreamer. Ma prost� list� odtwarzania, tryb pe�noekranowy, kontrol�
po�o�enia w pliku i g�o�no�ci, a tak�e w miar� kompletn� obs�ug� z
klawiatury.

%else
%description
Totem is simple movie player for the GNOME desktop based on xine-libs.
It features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl
Totem to prosty odtwarzacz film�w dla �rodowiska GNOME oparty na
xine-libs. Ma prost� list� odtwarzania, tryb pe�noekranowy, kontrol�
po�o�enia w pliku i g�o�no�ci, a tak�e w miar� kompletn� obs�ug� z
klawiatury.
%endif

%package libs
Summary:	Totem shared libraries
Summary(pl):	Wsp�dzielone biblioteki Totema
Group:		Libraries
Requires:	gnome-desktop-libs >= 2.16.2
Requires:	nautilus-libs >= 2.16.3

%description libs
Totem shared libraries.

%description libs -l pl
Wsp�dzielone biblioteki Totema.

%package devel
Summary:	Totem include files
Summary(pl):	Pliki nag��wkowe Totema
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.6

%description devel
Totem headers files.

%description devel -l pl
Pliki nag��wkowe Totema.

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
Summary(pl):	Wtyczka Totema do przegl�darek WWW
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

%description -n browser-plugin-%{name} -l pl
Wtyczka Totem do przegl�darek WWW.

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
	--%{?with_nvtv:enable}%{!?without_nvtv:disable}-nvtv \
	%{?with_gstreamer:--enable-gstreamer}

%{__make} \
	MOZILLA_IDLDIR="%{_includedir}/xulrunner/idl"


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	plugindir=%{_browserpluginsdir} \
	typelibdir=%{_browserpluginsdir} \
	xptdir=%{_browserpluginsdir} \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_browserpluginsdir}/*.{la,a}
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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_iconsdir}/hicolor/*/*/totem.*
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
%attr(755,root,root) %{_browserpluginsdir}/*.so
%attr(755,root,root) %{_browserpluginsdir}/*.xpt
