%define version	0.0.12
%define release	%mkrel 2

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
%makeinstall_std

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/hangul
%{_datadir}/libhangul

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/hangul-1.0/hangul.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libhangul.pc


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.12-2mdv2011.0
+ Revision: 661472
- mass rebuild

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 0.0.12-1
+ Revision: 634084
- New version 0.0.12

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 0.0.11-1mdv2011.0
+ Revision: 598570
- new version 0.0.11

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 0.0.10-1mdv2010.1
+ Revision: 460612
- fix file list
- New version 0.0.10

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.0.9-2mdv2010.0
+ Revision: 425564
- rebuild

* Sun Jan 18 2009 Funda Wang <fwang@mandriva.org> 0.0.9-1mdv2009.1
+ Revision: 330952
- New version 0.0.9

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.0.8-2mdv2009.0
+ Revision: 264805
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 23 2008 Funda Wang <fwang@mandriva.org> 0.0.8-1mdv2009.0
+ Revision: 196706
- New version 0.0.8
- split data files into main package

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 0.0.7-1mdv2008.1
+ Revision: 161669
- New version 0.0.7

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.0.6-2mdv2008.1
+ Revision: 150690
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.0.6-1mdv2008.0
+ Revision: 80138
- do not harcode library minor in file list
- new release


* Wed Feb 21 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.0.4-1mdv2007.0
+ Revision: 123184
- new release (utumi)

* Fri Nov 24 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.0.3-1mdv2007.1
+ Revision: 87010
- Import libhangul

* Tue Nov 07 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.0.3-1mdv2007.1
- first spec for Mandriva

