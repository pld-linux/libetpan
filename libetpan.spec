Summary:	Portable mail access library
Summary(pl.UTF-8):	Przenośna biblioteka dostępu do poczty
Name:		libetpan
Version:	0.57
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://dl.sourceforge.net/libetpan/%{name}-%{version}.tar.gz
# Source0-md5:	8ce8c6c071e81884a475b12b7f9a9cc0
Patch0:		%{name}-ac.patch
URL:		http://www.etpan.org/libetpan/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4
BuildRequires:	libtool
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
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libEtPan
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
Summary(pl.UTF-8):	Statyczna biblioteka libEtPan
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
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
%doc ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libetpan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libetpan.so.13

%files devel
%defattr(644,root,root,755)
%doc doc/API/*.htm
%attr(755,root,root) %{_bindir}/libetpan-config
%attr(755,root,root) %{_libdir}/libetpan.so
%{_libdir}/libetpan.la
%{_includedir}/libetpan
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libetpan.a
