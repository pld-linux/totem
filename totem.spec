#
# Conditional build
%bcond_with	gstreamer	# build with gstreamer instead xine-lib
%bcond_with	nvtv		# build with nvtv support
#

Summary:	Movie player for GNOME 2 based on the gstreamer engine
Summary(pl):	Odtwarzacz film�w dla GNOME 2 oparty na silniku gstreamer
Name:		totem
Version:	0.101
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/gnome/sources/totem/0.101/%{name}-%{version}.tar.bz2
# Source0-md5:	c85edd6a39fa2514f09c0c8afe6bf135
Patch0:		%{name}-desktop.patch
URL:		http://www.hadess.net/totem.php3
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-vfs2-devel
%if %{with gstreamer}
BuildRequires:	gstreamer-GConf-devel >= 0.8.5
BuildRequires:	gstreamer-devel >= 0.8.7
BuildRequires:	gstreamer-plugins-devel >= 0.8.5
%endif
BuildRequires:	gtk+2-devel >= 2:2.6.2
BuildRequires:	intltool >= 0.20
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.4.0.1
%{?with_nvtv:BuildRequires: libnvtvsimple-devel >= 0.4.5}
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	nautilus-cd-burner-devel >= 2.9.6
BuildRequires:	pkgconfig
%{!?with_gstreamer:BuildRequires:	xine-lib-devel >= 2:1.0-0.rc4a.1}
Requires(post,postun):	/sbin/ldconfig
Requires(post):	GConf2
Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{version}-%{release}
Requires:	XFree86-libs >= 4.3.0-1.3
Requires:	gnome-desktop >= 2.4.0
%if %{with gstreamer}
Requires:	gstreamer-colorspace >= 0.8.5
Requires:	gstreamer-videosink >= 0.8.5
%else
Requires:	xine-plugin-video
%endif
Requires:	gtk+2 >= 2:2.4.4
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

%package devel
Summary:	Totem include files
Summary(pl):	Pliki nag��wkowe totem 
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.6.2

%description devel
Totem headers files.

%description devel -l pl
Pliki nag��wkowe totem.

%package libs
Summary:	Totem library
Summary(pl):	Biblioteka totem
Group:		Libraries

%description libs
Totem library.

%description libs -l pl
Biblioteka totem.

%package static
Summary:	Static totem library
Summary(pl):	Statyczna biblioteka totem
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static totem library.

%description static -l pl
Statyczna biblioteka totem.

%prep
%setup -q
%patch0 -p1

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no
%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/sbin/ldconfig
%gconf_schema_install
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/sbin/ldconfig
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/*.schemas
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
