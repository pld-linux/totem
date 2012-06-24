# TODO:
# - this is a GNOME player and should use gstreamer as well
#
Summary:	Movie player for GNOME 2 based on the xine engine
Summary(pl):	Odtwarzacz film�w dla GNOME 2 oparty na silniku xine
Name:		totem
Version:	0.99.8
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.99/%{name}-%{version}.tar.bz2
# Source0-md5:	fc8c0fcf96bcea69a7c957ef1666cd7e
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
URL:		http://www.hadess.net/totem.php3
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.4.0.1
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel >= 1.0b12-3
#BuildRequires:	gstreamer-play-devel >= 0.6.0
#BuildRequires:	gstreamer-GConf-devel >= 0.6.0
Requires(post):	GConf2
Requires:	XFree86-libs >= 4.3.0-1.3
Requires:	gnome-desktop >= 2.4.0
Requires:	xine-lib
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

%build
%configure
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
%{_omf_dest_dir}/totem
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
