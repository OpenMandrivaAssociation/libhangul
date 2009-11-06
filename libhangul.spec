%define version	0.0.10
%define release	%mkrel 1

%define major 0
%define libname %mklibname hangul %major
%define develname %mklibname -d hangul

Name:		libhangul
Summary:	A generalized and portable library for hangul
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	LGPLv2+
URL:		http://kldp.net/projects/hangul/
Source0:	http://kldp.net/frs/download.php/4618/%name-%version.tar.gz
Conflicts:	%{libname} < 0.0.8
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
libhangul is a generalized and portable library for 
processing hangul.

%package -n	%{libname}
Summary:	Main libhangul library
Group:		System/Internationalization
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
libhangul library.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d hangul 0

%description -n %{develname}
Headers of %{name} for development.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_datadir}/libhangul

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/hangul-1.0/hangul.h
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libhangul.pc
