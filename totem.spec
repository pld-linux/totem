#
# TODO:
# - Make choice to build plugin with firefox or mozilla or none?
#
# Conditional build
%bcond_with	gstreamer	# build with gstreamer instead xine-lib
%bcond_without	nvtv		# build without nvtv support
#
# nvtv only available on few archs
%ifnarch alpha arm %{ix86} ia64 sh %{x8664}
%undefine		with_nvtv
%endif
#
Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl):	Odtwarzacz film�w dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	1.2.0
Release:	3.1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/totem/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	e07aded62a929779a4cd28c16fdb2efd
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-idl.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
BuildRequires:	mozilla-firefox-devel
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
Requires:	nautilus-libs >= 2.12.0

%description libs
Totem shared libraries.

%description libs -l pl
Wsp�dzielone biblioteki Totema.

%package devel
Summary:	Totem include files
Summary(pl):	Pliki nag��wkowe Totema
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.8.3

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

%package -n mozilla-firefox-plugin-totem
Summary:	Totem's plugin for Mozilla Firefox
Summary(pl):	Wtyczka Totema dla Mozilla Firefox
Group:		Libraries
Requires:	mozilla-firefox
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-firefox-plugin-totem
Totem's plugin for Mozilla Firefox.

%description -n mozilla-firefox-plugin-totem -l pl
Wtyczka Totema dla Mozilla Firefox.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-mozilla \
	%{?with_nvtv:--enable-nvtv} \
	%{?with_gstreamer:--enable-gstreamer}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/mozilla-firefox/plugins/*.{la,a}
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

%files -n mozilla-firefox-plugin-totem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/totem-mozilla-viewer
%attr(755,root,root) %{_libdir}/mozilla-firefox/plugins/*.so
%{_libdir}/mozilla-firefox/plugins/*.xpt
