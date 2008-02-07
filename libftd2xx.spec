Summary:	D2XX direct drivers for FTDI devices
Summary(pl.UTF-8):	Sterowniki bezpośrednie D2XX dla urządzeń FTDI
Name:		libftd2xx
Version:	0.4.13
Release:	1
License:	as is
Group:		Libraries
Source0:	http://www.ftdichip.com/Drivers/D2XX/Linux/%{name}%{version}.tar.gz
# Source0-md5:	6c06de2b4771e6cd67b9fe2054ec8a4d
Patch0:		%{name}-Ever.patch
URL:		http://www.ftdichip.com/Drivers/D2XX.htm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D2XX drivers allow direct access to the USB device through a DLL.
Application software can access the USB device through a series of
library function calls. This library supports FT232R, FT245R, FT2232,
FT232B, FT245B, FT8U232AM, FT8U245AM.

NOTE: this library is released without source code. It's meant
primarily to ease porting of Windows applications. For your projects
use Open Source libftdi instead.

%description -l pl.UTF-8
Sterowniki D2XX pozwalają na bezpośredni dostęp do urządzeń USB
poprzez dynamicznie ładowaną bibliotekę. Aplikacje mogą odwoływać się
do urządzeń poprzez serie wywołań funkcji bibliotecznych. Ta
biblioteka obsługuje układy FT232R, FT245R, FT2232, FT232B, FT245B,
FT8U232AM, FT8U245AM.

UWAGA: ta biblioteka została wydana bez kodu źródłowego. Jest
przeznaczona głównie dla ułatwienia portowania aplikacji z Windows. We
własnych projektach lepiej używać biblioteki libftdi z otwartymi
źródłami.

%package devel
Summary:	Header files for ftd2xx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ftd2xx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ftd2xx library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ftd2xx.

%package static
Summary:	Static ftd2xx library
Summary(pl.UTF-8):	Statyczna biblioteka ftd2xx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ftd2xx library.

%description static -l pl.UTF-8
Statyczna biblioteka ftd2xx.

%prep
%setup -q -c
%patch0 -p1

# kill precompiled objects which have sources included
rm lib_table/{*.o,*.so} sample/Simple/simple

%build
%{__make} -C lib_table \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DLINUX -D_RELEASE"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/ftd2xx}

install libftd2xx.so.0.4.13 $RPM_BUILD_ROOT%{_libdir}
ln -s libftd2xx.so.0.4.13 $RPM_BUILD_ROOT%{_libdir}/libftd2xx.so.0
ln -s libftd2xx.so.0.4.13 $RPM_BUILD_ROOT%{_libdir}/libftd2xx.so
install lib_table/libd2xx_table.so $RPM_BUILD_ROOT%{_libdir}
install static_lib/libftd2xx.a.0.4.13 $RPM_BUILD_ROOT%{_libdir}/libftd2xx.a
install WinTypes.h ftd2xx.h $RPM_BUILD_ROOT%{_includedir}/ftd2xx

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Config.txt FAQ.txt README.dat ftd2xx.cfg
%attr(755,root,root) %{_libdir}/libftd2xx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libftd2xx.so.0
%attr(755,root,root) %{_libdir}/libd2xx_table.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libftd2xx.so
%{_includedir}/ftd2xx

%files static
%defattr(644,root,root,755)
%{_libdir}/libftd2xx.a
