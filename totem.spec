Summary:	Movie player for GNOME 2 based on the xine engine
Summary(pl):	Odtwarzacz film�w dla GNOME 2 oparty na silniku xine
Name:		totem
Version:	0.99.9
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.99/%{name}-%{version}.tar.bz2
# Source0-md5:	e90467c1b4185edbad6571a139e4a42c
Patch0:		%{name}-locale-names.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	intltool >= 0.20
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.4.0.1
BuildRequires:	libtool
BuildRequires:	gstreamer-GConf-devel >= 0.7.0.3
BuildRequires:	gstreamer-plugins-devel >= 0.7.0.3
BuildRequires:	pkgconfig
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	XFree86-libs >= 4.3.0-1.3
Requires:	gnome-desktop >= 2.4.0
Requires:	gstreamer-colorspace >= 0.7.0.3
Requires:	gstreamer-videosink
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Totem is simple movie player for the GNOME desktop based on xine. It
features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl
Totem to prosty odtwarzacz film�w dla �rodowiska GNOME oparty na xine.
Ma prost� playlist�, tryb pe�noekranowy, kontrol� po�o�enia w pliku i
g�o�no�ci, a tak�e w miar� kompletn� obs�ug� z klawiatury.

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
    --enable-gstreamer
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
