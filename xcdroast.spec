Summary:	An X Window System based tool for creating CDs.
Name:		xcdroast
Version:	0.98alpha6
Release:	1
Copyright:	GPL
Group:		X11/Applications/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source:		http://www.fh-muenchen.de/home/ze/rz/services/projects/xcdroast/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-rh.patch
URL:		http://www.xcdroast.org/
Requires:	cdrecord = 1.9
Requires:	cdrecord-readcd = 1.9
Requires:	mkisofs
Requires:	cdda2wav
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X-CD-Roast provides a GUI interface for commands like cdrecord and
mkisofs. X-CD-Roast includes a self-explanatory X11 user interface,
automatic SCSI and IDE hardware setup, support for mastering of new
ISO9660 data CDs, support for production of new audio CDs, fast
copying of CDs without hard disk buffering, and a logfile option.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__make} CC="gcc $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

ln -sf xcdrgtk $RPM_BUILD_ROOT/%{_bindir}/xcdroast

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG 
%doc DOCUMENTATION
%doc FAQ
%doc README
%doc TRANSLATION.HOWTO
%doc COPYING
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xcdroast-0.98/*
