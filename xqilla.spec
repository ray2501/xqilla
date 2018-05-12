#
# RPM spec for XQilla
#

Summary:	XQilla - C++ implementation of XQuery and XPath 2.0 based on Xerces-C
Name:		xqilla
Version:	2.3.4
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/xqilla/XQilla-%{version}.tar.gz
URL:		http://xqilla.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libxerces-c-devel >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XQilla - C++ implementation of XQuery and XPath 2.0 based on Xerces-C.

%package devel
Summary:	Header files for XQilla library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
BuildRequires:	libxerces-c-devel >= 3.2

%description devel
Header files for XQilla library.

%prep
%setup -q -n XQilla-%{version}

%build
%configure \
	--with-xerces=/usr --enable-static=no

%{__make}

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
make clean

%post	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xqilla
%{_libdir}/libxqilla.so.*.*.*
%ghost %{_libdir}/libxqilla.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libxqilla.so
%{_libdir}/libxqilla.la
%{_includedir}/xqilla
%{_includedir}/xqc.h
