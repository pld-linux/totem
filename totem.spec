#
# Conditional build
%bcond_with     gstreamer       # build with gstreamer instead xine-lib
%bcond_with	nvtv	        # build with nvtv support
#

Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl):	Odtwarzacz filmów dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	0.99.11
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.99/%{name}-%{version}.tar.bz2
# Source0-md5:	ba35dec88f4b185a611eb516c1b464e7
Patch0:		%{name}-locale-names.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel
%if %{with gstreamer}
BuildRequires:	gstreamer-GConf-devel >= 0.8.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
%endif
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.20
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.4.0.1
BuildRequires:	libtool
%{?with_nvtv:BuildRequires: nvtv}
BuildRequires:	pkgconfig
%{!?with_gstreamer:BuildRequires:       xine-lib-devel >= 1:1.0-0.rc3c.1}
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	XFree86-libs >= 4.3.0-1.3
Requires:	gnome-desktop >= 2.4.0
%if %{with gstreamer}
Requires:	gstreamer-colorspace >= 0.8.0
Requires:	gstreamer-videosink >= 0.8.0
%endif
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%endif

%if %{without gstreamer}
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

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%{?with_nvtv: --enable-nvtv} \
%{?with_gstreamer: --enable-gstreamer}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
/usr/bin/scrollkeeper-update

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/totem-properties-page
%{_datadir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/mime-info/%{name}.keys
%{_libdir}/bonobo/servers/Totem_properties.server
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
