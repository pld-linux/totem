
%define 	snap	20030630

Summary:	Movie player for GNOME 2 based on the xine engine
Summary(pl):	Odtwarzacz filmów dla GNOME 2 oparty na silniku xine
Name:		totem
Version:	0.99.4
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.99/%{name}-%{version}.tar.bz2
# Source0-md5:	d8ce64a2bc1cda421cae9e44c2c6587e
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
URL:		http://www.hadess.net/totem.php3
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.3.3.1-2
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel >= 1.0b12-3
#BuildRequires:	gstreamer-play-devel >= 0.6.0
#BuildRequires:	gstreamer-GConf-devel >= 0.6.0
Requires(post):	GConf2
Requires:	XFree86-libs >= 4.3.0-1.3
Requires:	gnome-desktop >= 2.3.4-2
Requires:	xine-lib >= 1.0b12-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Totem is simple movie player for the GNOME desktop based on xine. It
features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation.

%description -l pl
Totem to prosty odtwarzacz filmów dla ¶rodowiska GNOME oparty na xine.
Ma prost± playlistê, tryb pe³noekranowy, kontrolê po³o¿enia w pliku i
g³o¶no¶ci, a tak¿e w miarê kompletn± obs³ugê z klawiatury.

%prep
%setup -q

%build
#./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/totem-properties-page
%{_libdir}/bonobo/servers/Totem_properties.server
%{_datadir}/application-registry/%{name}.applications
%{_desktopdir}/*.desktop
%{_datadir}/mime-info/%{name}.keys
%{_datadir}/%{name}
%{_pixmapsdir}/*
