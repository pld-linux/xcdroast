%define		ver	0.98
Summary:	An X Window System based tool for creating CDs
Summary(es):	Herramienta gráfica para crear CDs
Summary(pl):	Narzêdzie pod X do nagrywania p³yt CD
Summary(pt_BR):	Ferramenta gráfica para criação de CDs
Name:		xcdroast
Version:	%{ver}alpha10
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	6f9ffd30c7ba8f067c2f1bddcc83d7d8
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-home_etc.patch
URL:		http://www.xcdroast.org/
Requires:	cdrtools >= 1.11
Requires:	cdrtools-readcd >= 1.11
Requires:	cdrtools-mkisofs >= 1.11
Requires:	cdrtools-cdda2wav >= 1.11
BuildRequires:	XFree86-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%build
%{__make} \
    PREFIX="%{_prefix}" \
    CC="%{__cc} %{rpmcflags}" \
    CDRTOOLS_PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW

%{__make} PREFIX="%{_prefix}" DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG DOCUMENTATION FAQ README TRANSLATION.HOWTO README.atapi
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}-%{ver}
%dir %{_libdir}/%{name}-%{ver}/bin/
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/cddbtool
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/rmtool
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/vrfytool
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/bin/wavplay
%attr(2755,root,cdwrite) %{_libdir}/%{name}-%{ver}/bin/xcdrwrap
%dir %{_libdir}/%{name}-%{ver}/lang
%attr(755,root,root) %{_libdir}/%{name}-%{ver}/lang/*.sh
%{_libdir}/%{name}-%{ver}/lang/*.def
%{_libdir}/%{name}-%{ver}/icons
%{_libdir}/%{name}-%{ver}/sound
%{_applnkdir}/Utilities/CD-RW/%{name}.desktop
%{_pixmapsdir}/*
