%define		ver	0.98
Summary:	An X Window System based tool for creating CDs
Summary(es):	Herramienta gr�fica para crear CDs
Summary(pl):	Narz�dzie pod X do nagrywania p�yt CD
Summary(pt_BR):	Ferramenta gr�fica para cria��o de CDs
Name:		xcdroast
Version:	%{ver}alpha10
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
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
X-CD-Roast suministra una interfaz gr�fica para las �rdenes mkisofs y
cdrecord. Su interfaz es autoexplicativa. Proporciona detecci�n
autom�tica del hardware SCSI y IDE, soporte para crear nuevos CDs de
datos ISO9660, soporte para producci�n de CDs de sonido, copia r�pida
de CDs sin grabaci�n en el discoduro y opci�n para generar archivo de
log.

%description -l pl
X-CD-Roast dostarcza graficznego interfejsu do komend takich jak
cdrecord oraz mkisofs. X-CD-Roast zawiera samo-wyja�niaj�cy si�
interfejs u�ytkownika pod X11, automatyczn� konfiguracj� urz�dze� SCSI
oraz IDE itp.

%description -l pt_BR
O X-CD-Roast fornece uma interface gr�fica para os comandos mkisofs e
cdrecord. Sua interface � auto-explicativa. Prov� detec��o autom�tica
do hardware SCSI e IDE, suporte para criar novos CDs de dados ISO9660,
suporte para produ��o de CDs de �udio, c�pia r�pida de CDs sem
grava��o no disco r�gido e op��o para gerar arquivo de log.

%prep
%setup -q

%build
%{__make} PREFIX="%{_prefix}" CC="%{__cc} %{rpmcflags}"

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
