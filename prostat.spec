Summary:	Squid statistic tool
Summary(pl):	Narzędzie do statystyki squida
Name:		prostat
Version:	1.3
Release:	5
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	http://www.serveurs-nationaux.jussieu.fr/cache/prostat/%{name}_%{version}.tar.gz
Patch0:		%{name}-%{version}-megaloman.patch
Patch1:		%{name}-%{version}-confix.patch
Patch2:		%{name}-%{version}-png.patch
URL:		http://cache.cnrs.fr/prostat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/ldconfig

%description
Prostat is a squid statistic tool.

%description -l pl
Prostat jest narzędziem do statystyk squida.

%prep
%setup -q -n prostat_%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} CFLAGS="%{rpmcflags}" LIBS="-lm -lgd -lpng -lttf -ljpeg"

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
