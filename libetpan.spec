Summary:	Portable mail access library
Summary(pl.UTF-8):   Przenośna biblioteka dostępu do poczty
Name:		libetpan
Version:	0.49
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libetpan/%{name}-%{version}.tar.gz
# Source0-md5:	f6c973ea1aa53d947f034e093960da10
Patch0:		%{name}-db.patch
URL:		http://www.etpan.org/
BuildRequires:	autoconf
BuildRequires:	db-devel >= 4
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The purpose of this mail library is to provide a portable, efficient
middleware for different kinds of mail access. It will be used for
low-level mail handling: network protocols (IMAP/NNTP/POP3/SMTP over
TCP/IP and SSL/TCP/IP, already implemented), local storage
(mbox/MH/maildir), message / MIME parser.

%description -l pl.UTF-8
Celem biblioteki jest udostępnienie przenośnego, efektywnego
pośrednika dla różnych metod dostępu do poczty. Pozwala na: obsługę
różnych protokołów sieciowych (IMAP/NNTP/POP3/SMTP przez TCP/IP oraz
SSL/TCP/IP), obsługę lokalnych zasobów (mbox/MH/maildir) czy
parsowanie wiadomości MIME.

%package devel
Summary:	Header files for libEtPan
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libEtPan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	db-devel >= 4
Requires:	openssl-devel

%description devel
Header files for libEtPan library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libEtPan.

%package static
Summary:	Static libEtPan library
Summary(pl.UTF-8):   Statyczna biblioteka libEtPan
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libEtPan library.

%description static -l pl.UTF-8
Statyczna biblioteka libEtPan.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO NEWS
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/API/*.htm
%attr(755,root,root) %{_bindir}/libetpan-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
