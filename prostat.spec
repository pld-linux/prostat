Summary: Squid statistic tool
Name: prostat
%define version 1.3
Version: %{version}
Release: 5
Group: Utilities
Copyright: GNU
URL: http://cache.cnrs.fr/prostat/

Source: prostat_%{version}.tar.gz
Patch0: prostat-%{version}-megaloman.patch
Patch1: prostat-%{version}-confix.patch
Patch2: prostat-%{version}-png.patch
BuildRoot: /var/tmp/prostat-root
Prereq: /sbin/ldconfig

%description
Prostat is a squid statistic tool.

%prep
%setup -n prostat_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS" LIBS="-lm -lgd -lpng -lttf -ljpeg"

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#ldconfig

#%postun
#ldconfig

%files
%defattr(-,root,root)
%dir /usr/local/prostat/
/usr/local/bin/prostat
/usr/local/prostat/domains.tab
/usr/local/prostat/mime.types
%config(noreplace) /usr/local/prostat/prostat.conf
%doc README LISEZ_MOI CHANGE

%changelog
* Thu Mar 16 2000 Peter Hanecak <hanecak@megaloman.sk>
- rebuild against gd-1.8.1

* Mon Mar 13 2000 Peter Hanecak <hanecak@megaloman.sk>
- rebuild against gd-1.7.3

* Mon Sep 13 1999 Peter Hanecak <hanecak@megaloman.sk>
- rebuild against gd-1.6.3 (now PNG images are used)
- added URL
- %config(noreplace) /usr/local/prostat/prostat.conf

* Tue Mar  2 1999 Peter Hanecak <hanecak@megaloman.sk>
- fixed error in specification of prostat.conf location in analhead.h

* Tue Mar  2 1999 Peter Hanecak <hanecak@megaloman.sk>
- initial spec
- included gd library is not used
