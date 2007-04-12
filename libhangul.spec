%define version	0.0.4
%define release	%mkrel 1

%define libname %mklibname hangul 0

Name:		libhangul
Summary:	A generalized and portable library for hangul
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	LGPL
URL:		http://kldp.net/projects/hangul/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
libhangul is a generalized and portable library for 
processing hangul.


%package -n	%{libname}
Summary:	Main libhangul library
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libhangul library.

%package -n	%{libname}-devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Headers of %{name} for development.


%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_datadir}/libhangul/hanja/hanja.txt
%{_libdir}/*.so.0.0.0

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/hangul-1.0/hangul.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.so.0
%{_libdir}/pkgconfig/libhangul.pc


