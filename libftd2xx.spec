Summary:	D2XX direct drivers for FTDI devices
Summary(pl.UTF-8):	Sterowniki bezpośrednie D2XX dla urządzeń FTDI
Name:		libftd2xx
Version:	1.4.27
Release:	1
License:	as is
Group:		Libraries
Source0:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-x86_32-1.4.27.tgz
# Source0-md5:	2948931d8ee6dc0222220cccd733b807
Source1:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-x86_64-1.4.27.tgz
# Source1-md5:	1480b8dc98b3bb3361edab57c0ebd034
Source2:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-arm-v7-sf-1.4.27.tgz
# Source2-md5:	5daae1c2c0c48fd82317250f6c73e843
Source3:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-arm-v6-hf-1.4.27.tgz
# Source3-md5:	91f92a0d2060083ce46d6bbbb605f8ee
Source4:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-arm-v7-hf-1.4.27.tgz
# Source4-md5:	d63bbb651a1ce1baa47658e3a0c2814f
Source5:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-arm-v8-1.4.27.tgz
# Source5-md5:	07d3466c98fd7926d6639d7bc17ec71d
Source6:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-mips-eglibc-sf-1.4.27.tgz
# Source6-md5:	7487e27ab7a07c80532ee69ae318fec1
Source7:	https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-mips-eglibc-hf-1.4.27.tgz
# Source7-md5:	e8f86c34dab76ad9feef62100d26b4a0
URL:		https://ftdichip.com/drivers/d2xx-drivers/
ExclusiveArch:	%{ix86} %{x8664} armv6hl armv7hl armv7l aarch64 mips
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
%ifarch %{ix86}
%setup -q -c
%endif
%ifarch %{x8664}
%setup -q -c -T -a1
%endif
%ifarch armv7l
%setup -q -c -T -a2
%endif
%ifarch armv6hl
%setup -q -c -T -a3
%endif
%ifarch armv7hl
%setup -q -c -T -a4
%endif
%ifarch aarch64
%setup -q -c -T -a5
%endif
%ifarch mips
%if 0
# FIXME: condition for soft-float on mips?
%setup -q -c -T -a6
%else
%setup -q -c -T -a7
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/ftd2xx}

install -m755 release/build/libftd2xx.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s libftd2xx.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libftd2xx.so
cp -p release/build/libftd2xx.a $RPM_BUILD_ROOT%{_libdir}/libftd2xx.a
cp -p release/{WinTypes.h,ftd2xx.h} $RPM_BUILD_ROOT%{_includedir}/ftd2xx

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libftd2xx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libftd2xx.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/ftd2xx

%files static
%defattr(644,root,root,755)
%{_libdir}/libftd2xx.a
