Summary:	Squid statistic tool
Name:		prostat
%define version 1.3
Version:	%{version}
Release:	5
Group:		Utilities
######		Unknown group!
Copyright:	GNU
URL:		http://cache.cnrs.fr/prostat/

Source0:	%{name}_%{version}.tar.gz
Patch0:		%{name}-%{version}-megaloman.patch
Patch1:		%{name}-%{version}-confix.patch
Patch2:		%{name}-%{version}-png.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/ldconfig

%description
Prostat is a squid statistic tool.

%prep
%setup -q -n prostat_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" LIBS="-lm -lgd -lpng -lttf -ljpeg"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

#%post
#ldconfig

#%postun
#ldconfig

%files
%defattr(644,root,root,755)
%dir %{_prefix}/local/prostat/
%{_prefix}/local/bin/prostat
%{_prefix}/local/prostat/domains.tab
%{_prefix}/local/prostat/mime.types
%config(noreplace) %{_prefix}/local/prostat/prostat.conf
%doc README LISEZ_MOI CHANGE
