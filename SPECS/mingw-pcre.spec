%?mingw_package_header

Name:		mingw-pcre
Version:	8.43
Release:	7%{?dist}
Summary:	MinGW Windows pcre library

License:	BSD
URL:		http://www.pcre.org/
Source0:	ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-%{version}.tar.bz2

# Refused by upstream, bug #675477
Patch1:     pcre-8.32-refused_spelling_terminated.patch
# Fix recursion stack estimator, upstream bug #2173, refused by upstream
Patch2:     pcre-8.41-fix_stack_estimator.patch
# Link applications to PCRE-specific symbols when using POSIX API, bug #1667614,
# upstream bug 1830, partially borrowed from PCRE2, proposed to upstream,
# This amends ABI, application built with this patch cannot run with
# previous libpcreposix builds.
Patch3:     pcre-8.42-Declare-POSIX-regex-function-names-as-macros-to-PCRE.patch
# Add (*LF) to a list of start-of-pattern options in the C++ wrapper,
# upstream bug #2400, in upstream after 8.43
Patch4:     pcre-8.43-Fix-omission-of-LF-from-list-in-the-C-wrapper.patch

BuildArch:	noarch

BuildRequires: make
BuildRequires:  git
BuildRequires:	redhat-rpm-config

BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils


%description
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.


# Win32
%package -n mingw32-pcre
Summary:	MinGW Windows pcre library
Requires:	pkgconfig

%description -n mingw32-pcre
Cross compiled Perl-compatible regular expression library for use with mingw32.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n mingw32-pcre-static
Summary:       Static version of the mingw32-pcre library
Requires:      mingw32-pcre = %{version}-%{release}
BuildArch:     noarch

%description -n mingw32-pcre-static
Static version of the mingw32-pcre library.

# Win64
%package -n mingw64-pcre
Summary:        MinGW Windows pcre library
Requires:       pkgconfig

%description -n mingw64-pcre
Cross compiled Perl-compatible regular expression library for use with mingw64.

PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package -n mingw64-pcre-static
Summary:       Static version of the mingw64-pcre library
Requires:      mingw64-pcre = %{version}-%{release}
BuildArch:     noarch

%description -n mingw64-pcre-static
Static version of the mingw64-pcre library.


%?mingw_debug_package


%prep
%autosetup -S git_am -n pcre-%{version}


%build
%mingw_configure --enable-utf8 --enable-unicode-properties --enable-static --enable-pcre8 --enable-pcre16 --enable-pcre32
%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/doc/*
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/man/*
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/man/*

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-pcre
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%{mingw32_bindir}/pcre-config
%{mingw32_bindir}/pcregrep.exe
%{mingw32_bindir}/pcretest.exe
%{mingw32_bindir}/libpcre-1.dll
%{mingw32_bindir}/libpcre16-0.dll
%{mingw32_bindir}/libpcre32-0.dll
%{mingw32_bindir}/libpcrecpp-0.dll
%{mingw32_bindir}/libpcreposix-0.dll
%{mingw32_libdir}/libpcre.dll.a
%{mingw32_libdir}/libpcre16.dll.a
%{mingw32_libdir}/libpcre32.dll.a
%{mingw32_libdir}/libpcrecpp.dll.a
%{mingw32_libdir}/libpcreposix.dll.a
%{mingw32_libdir}/pkgconfig/libpcre.pc
%{mingw32_libdir}/pkgconfig/libpcre16.pc
%{mingw32_libdir}/pkgconfig/libpcre32.pc
%{mingw32_libdir}/pkgconfig/libpcrecpp.pc
%{mingw32_libdir}/pkgconfig/libpcreposix.pc
%{mingw32_includedir}/pcre.h
%{mingw32_includedir}/pcre_scanner.h
%{mingw32_includedir}/pcre_stringpiece.h
%{mingw32_includedir}/pcrecpp.h
%{mingw32_includedir}/pcrecpparg.h
%{mingw32_includedir}/pcreposix.h

%files -n mingw32-pcre-static
%{mingw32_libdir}/libpcre.a
%{mingw32_libdir}/libpcre16.a
%{mingw32_libdir}/libpcre32.a
%{mingw32_libdir}/libpcrecpp.a
%{mingw32_libdir}/libpcreposix.a

# Win64
%files -n mingw64-pcre
%doc AUTHORS COPYING LICENCE NEWS README ChangeLog
%{mingw64_bindir}/pcre-config
%{mingw64_bindir}/pcregrep.exe
%{mingw64_bindir}/pcretest.exe
%{mingw64_bindir}/libpcre-1.dll
%{mingw64_bindir}/libpcre16-0.dll
%{mingw64_bindir}/libpcre32-0.dll
%{mingw64_bindir}/libpcrecpp-0.dll
%{mingw64_bindir}/libpcreposix-0.dll
%{mingw64_libdir}/libpcre.dll.a
%{mingw64_libdir}/libpcre16.dll.a
%{mingw64_libdir}/libpcre32.dll.a
%{mingw64_libdir}/libpcrecpp.dll.a
%{mingw64_libdir}/libpcreposix.dll.a
%{mingw64_libdir}/pkgconfig/libpcre.pc
%{mingw64_libdir}/pkgconfig/libpcre16.pc
%{mingw64_libdir}/pkgconfig/libpcre32.pc
%{mingw64_libdir}/pkgconfig/libpcrecpp.pc
%{mingw64_libdir}/pkgconfig/libpcreposix.pc
%{mingw64_includedir}/pcre.h
%{mingw64_includedir}/pcre_scanner.h
%{mingw64_includedir}/pcre_stringpiece.h
%{mingw64_includedir}/pcrecpp.h
%{mingw64_includedir}/pcrecpparg.h
%{mingw64_includedir}/pcreposix.h

%files -n mingw64-pcre-static
%{mingw64_libdir}/libpcre.a
%{mingw64_libdir}/libpcre16.a
%{mingw64_libdir}/libpcre32.a
%{mingw64_libdir}/libpcrecpp.a
%{mingw64_libdir}/libpcreposix.a


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 8.43-7
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 8.43-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.43-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 8.43-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Wed Aug 14 2019 Marc-André Lureau <marcandre.lureau@redhat.com> - 8.43-1
- New upstream release 8.43

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.38-1
- Update to 8.38
- Fixes various CVE's:
  RHBZ #1236660, #1249905, #1250947, #1256453, #1256454, #1287616,
  RHBZ #1287619, #1287626, #1287628, #1287631, #1287634, #1287640,
  RHBZ #1287642, #1287648, #1287650, #1287656, #1287658, #1287661,
  RHBZ #1287663, #1287668, #1287670, #1287673, #1287675, #1287692,
  RHBZ #1287694, #1287698, #1287700, #1287704, #1287706, #1287720,
  RHBZ #1287722

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 25 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 8.36-1
- Update to 8.36
- Add upstream patches from main pcre package

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.34-1
- Update to 8.34

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.33-2
- Added -static subpackages

* Wed Jul  3 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.33-1
- Update to 8.33
- Added the configure arguments --enable-pcre8 --enable-pcre16 --enable-pcre32
  (the pcre16 one is needed by mingw-qt5-qtbase)
- Use a more verbose filelist

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.32-1
- Update to 8.32

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.31-2
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.31-1
- Update to 8.31
- Dropped patch as it doesn't have any effect on the mingw target

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 14 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.30-9
- Update to 8.30
- Added win64 support

* Fri Mar 09 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.10-8
- Dropped .la files

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 8.10-7
- Renamed the source package to mingw-pcre (#801011)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 8.10-6
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 8.10-4
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 20 2010 Adam Stokes <astokes@redhat.com> - 8.10-2
- Restore changes from the native package to pass package review process

* Wed Jul 21 2010 Ryan O'Hara <rohara@redhat.com> - 8.10-1
- Initial spec file.
