Summary:	Movie player for GNOME 2 based on the xine engine
Summary(pl):	Odtwarzacz filmów dla GNOME 2 oparty na silniku xine
Name:		totem
Version:	0.90.0
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.hadess.net/files/software/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.hadess.net/totem.php3
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	xine-lib-devel >= 1.0-beta3
Requires(post):	GConf2
Requires:	gnome-desktop >= 2.0.0
Requires:	xine-lib >= 1.0-beta3
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
%configure
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime-info/%{name}.keys
%{_datadir}/%{name}
%{_pixmapsdir}/*
