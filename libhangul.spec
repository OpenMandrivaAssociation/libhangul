%define major	0
%define libname %mklibname hangul %{major}
%define devname %mklibname -d hangul

Summary:	A generalized and portable library for hangul
Name:		libhangul
Version:	0.0.12
Release:	2
Group:		System/Internationalization
License:	LGPLv2+
Url:		http://kldp.net/projects/hangul/
Source0:	http://kldp.net/frs/download.php/4618/%{name}-%{version}.tar.gz

%description
libhangul is a generalized and portable library for 
processing hangul.

%package -n	%{libname}
Summary:	Main libhangul library
Group:		System/Internationalization

%description -n %{libname}
libhangul library.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/hangul
%{_datadir}/libhangul

%files -n %{libname}
%{_libdir}/libhangul.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/hangul-1.0/hangul.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libhangul.pc

