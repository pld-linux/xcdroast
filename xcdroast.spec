%define		ver	0.98
Summary:	An X Window System based tool for creating CDs
Summary(es):	Herramienta gráfica para crear CDs
Summary(pl):	Narzêdzie pod X do nagrywania p³yt CD
Summary(pt_BR):	Ferramenta gráfica para criação de CDs
Name:		xcdroast
Version:	%{ver}alpha15
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	2a9c1d9f2ef58713c453e674b989be3e
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.xcdroast.org/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
Requires:	cdrtools >= 2.01a18
Requires:	cdrtools-cdda2wav >= 2.01a18
Requires:	cdrtools-mkisofs >= 2.01a18
Requires:	cdrtools-readcd >= 2.01a18
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	%{_prefix}/lib

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

sed -e 's/zh_TW\.Big5/zh_TW/;s/zh_CN\.GB2312/zh_CN/;s/\<no\>/nb/;s/el_GR/el/;s/sq_AL/sq/' \
	po/LINGUAS > l.tmp
mv -f l.tmp po/LINGUAS
mv -f po/{zh_TW.Big5,zh_TW}.po
mv -f po/{zh_CN.GB2312,zh_CN}.po
mv -f po/{no,nb}.po
mv -f po/{el_GR,el}.po
mv -f po/{sq_AL,sq}.po

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-gtk2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install extra/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/*
%dir %{_ulibdir}/%{name}-%{ver}
%dir %{_ulibdir}/%{name}-%{ver}/bin
%attr(755,root,root) %{_ulibdir}/%{name}-%{ver}/bin/cddbtool
%attr(755,root,root) %{_ulibdir}/%{name}-%{ver}/bin/rmtool
%attr(755,root,root) %{_ulibdir}/%{name}-%{ver}/bin/vrfytool
%attr(755,root,root) %{_ulibdir}/%{name}-%{ver}/bin/wavplay
%attr(755,root,root) %{_ulibdir}/%{name}-%{ver}/bin/xcdrwrap
%{_ulibdir}/%{name}-%{ver}/icons
%{_ulibdir}/%{name}-%{ver}/sound
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/*
