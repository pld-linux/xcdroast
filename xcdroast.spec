%define		ver	0.98
Summary:	An X Window System based tool for creating CDs
Summary(pl):	Narzêdzie pod X do nagrywania p³yt CD
Name:		xcdroast
Version:	%{ver}alpha9
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.fh-muenchen.de/home/ze/rz/services/projects/xcdroast/src/%{name}-%{version}.tar.gz
URL:		http://www.xcdroast.org/
Requires:	cdrtools >= 1.10
Requires:	cdrtools-readcd >= 1.10
Requires:	cdrtools-mkisofs >= 1.10
Requires:	cdrtools-cdda2wav >= 1.10
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	XFree86-devel
BuildRequires:	glib-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-CD-Roast provides a GUI interface for commands like cdrecord and
mkisofs. X-CD-Roast includes a self-explanatory X11 user interface,
automatic SCSI and IDE hardware setup, support for mastering of new
ISO9660 data CDs, support for production of new audio CDs, fast
copying of CDs without hard disk buffering, and a logfile option.

%description -l pl
X-CD-Roast dostarcza graficznego interfejsu do komend takich jak
cdrecord oraz mkisofs. X-CD-Roast zawiera samo-wyja¶niaj±cy siê
interfejs u¿ytkownika pod X11, automatyczn± konfiguracjê urz±dzeñ SCSI
oraz IDE itp.

%prep
%setup -q

%build
%{__make} PREFIX="%{_prefix}" CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} PREFIX="%{_prefix}" DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf CHANGELOG DOCUMENTATION FAQ README TRANSLATION.HOWTO \
	  README.atapi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
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
