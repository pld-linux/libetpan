Summary:	Portable mail access library
Summary(pl.UTF-8):	Przenośna biblioteka dostępu do poczty
Name:		libetpan
Version:	1.9.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/dinhviethoa/libetpan/archive/%{version}.tar.gz
# Source0-md5:	42462e839b7d78c057e485dcb80d7d1c
Patch0:		%{name}-link.patch
Patch1:		%{name}-db.patch
URL:		https://github.com/dinhviethoa/libetpan
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	cyrus-sasl-devel >= 2
BuildRequires:	db-devel >= 4
BuildRequires:	docbook-style-dsssl
BuildRequires:	expat-devel
BuildRequires:	gnutls-devel
BuildRequires:	liblockfile-devel
BuildRequires:	libtool
BuildRequires:	openjade
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
SSL/TCP/IP), obsługę lokalnych zasobów (mbox/MH/maildir), a także
analizę wiadomości MIME.

%package devel
Summary:	Header files for libEtPan
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libEtPan
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	cyrus-sasl-devel >= 2
Requires:	db-devel >= 4
Requires:	expat-devel
Requires:	liblockfile-devel
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
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ipv6 \
	--with-gnutls=yes \
	--with-openssl=no
%{__make}
%{__make} -C doc doc \
	DSL=%{_datadir}/sgml/docbook/dsssl-stylesheets/html/docbook.dsl

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
%doc COPYRIGHT ChangeLog NEWS
%attr(755,root,root) %{_libdir}/libetpan.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libetpan.so.20

%files devel
%defattr(644,root,root,755)
%doc doc/API/*.htm
%attr(755,root,root) %{_bindir}/libetpan-config
%attr(755,root,root) %{_libdir}/libetpan.so
%{_libdir}/libetpan.la
%{_includedir}/libetpan
%{_includedir}/libetpan.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libetpan.a
