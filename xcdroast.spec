%define		ver	0.98
Summary:	An X Window System based tool for creating CDs
Summary(es):	Herramienta gráfica para crear CDs
Summary(pl):	Narzêdzie pod X do nagrywania p³yt CD
Summary(pt_BR):	Ferramenta gráfica para criação de CDs
Name:		xcdroast
Version:	%{ver}alpha14
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	c5f3f1ab6ff6d286bd984def54ef0c54
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-cdrtools_201a18.patch
Patch3:		%{name}-error_write_tracks.patch
URL:		http://www.xcdroast.org/
BuildRequires:	XFree86-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
Requires:	cdrtools >= 2.01a18
Requires:	cdrtools-cdda2wav >= 2.01a18
Requires:	cdrtools-mkisofs >= 2.01a18
Requires:	cdrtools-readcd >= 2.01a18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-CD-Roast provides a GUI interface for commands like cdrecord and
mkisofs. X-CD-Roast includes a self-explanatory X11 user interface,
automatic SCSI and IDE hardware setup, support for mastering of new
ISO9660 data CDs, support for production of new audio CDs, fast
copying of CDs without hard disk buffering, and a logfile option.

%description -l es
X-CD-Roast suministra una interfaz gráfica para las órdenes mkisofs y
cdrecord. Su interfaz es autoexplicativa. Proporciona detección
automática del hardware SCSI y IDE, soporte para crear nuevos CDs de
datos ISO9660, soporte para producción de CDs de sonido, copia rápida
de CDs sin grabación en el discoduro y opción para generar archivo de
log.

%description -l pl
X-CD-Roast dostarcza graficznego interfejsu do komend takich jak
cdrecord oraz mkisofs. X-CD-Roast zawiera samo-wyja¶niaj±cy siê
interfejs u¿ytkownika pod X11, automatyczn± konfiguracjê urz±dzeñ SCSI
oraz IDE itp.

%description -l pt_BR
O X-CD-Roast fornece uma interface gráfica para os comandos mkisofs e
cdrecord. Sua interface é auto-explicativa. Provê detecção automática
do hardware SCSI e IDE, suporte para criar novos CDs de dados ISO9660,
suporte para produção de CDs de áudio, cópia rápida de CDs sem
gravação no disco rígido e opção para gerar arquivo de log.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

install extra/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}-%{ver}
%dir %{_libdir}/%{name}-%{ver}/bin/
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/cddbtool
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/rmtool
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/vrfytool
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/wavplay
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/xcdrwrap
%{_libdir}/%{name}-%{ver}/icons
%{_libdir}/%{name}-%{ver}/sound
%{_desktopdir}%{name}.desktop
%{_mandir}/man1/*
