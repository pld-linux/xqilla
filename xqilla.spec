#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	XQilla - C++ implementation of XQuery and XPath 2.0 based on Xerces-C
Summary(pl.UTF-8):	XQilla - implementacja C++ XQuary i XPath 2.0 oparta na bibliotece Xerces-C
Name:		xqilla
Version:	2.3.0
Release:	3
License:	Apache v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/xqilla/XQilla-%{version}.tar.gz
# Source0-md5:	7261c7b4bb5a45cbf6270073976a51ce
Patch0:		%{name}-link.patch
URL:		http://xqilla.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	faxpp-devel
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	tidy-devel
BuildRequires:	xerces-c-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XQilla - C++ implementation of XQuery and XPath 2.0 based on Xerces-C.

%description -l pl.UTF-8
XQilla - implementacja C++ XQuary i XPath 2.0 oparta na bibliotece
Xerces-C.

%package devel
Summary:	Header files for XQilla library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XQilla
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	faxpp-devel
Requires:	libstdc++-devel
Requires:	tidy-devel
Requires:	xerces-c-devel >= 3

%description devel
Header files for XQilla library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XQilla.

%package static
Summary:	Static XQilla library
Summary(pl.UTF-8):	Statyczna biblioteka XQilla
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XQilla library.

%description static -l pl.UTF-8
Statyczna biblioteka XQilla.

%package apidocs
Summary:	XQilla API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki XQilla
Group:		Documentation

%description apidocs
API and internal documentation for XQilla library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki XQilla.

%prep
%setup -q -n XQilla-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-faxpp=/usr \
	--with-xerces=/usr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/xqilla
%attr(755,root,root) %{_libdir}/libxqilla.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxqilla.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxqilla.so
%{_libdir}/libxqilla.la
%{_includedir}/xqilla
%{_includedir}/xqc.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libxqilla.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc docs/{dom3-api,simple-api,xqc-api,*.html}
%endif
