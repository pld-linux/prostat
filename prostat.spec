%define		_ver	1_32

Summary:	Squid statistic tool
Summary(pl):	Narzêdzie do statystyki squida
Name:		prostat
Version:	1.32
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.serveurs-nationaux.jussieu.fr/cache/prostat/%{name}_%{_ver}.tar.gz
# Source0-md5:	757b39c69e0dc66a169c23dcc25db560
URL:		http://cache.cnrs.fr/prostat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/ldconfig

%description
Prostat is a squid statistic tool.

%description -l pl
Prostat jest narzêdziem do statystyk squida.

%prep
%setup -q -n prostat_%{version}

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}" LIBS="-lm -lgd -lpng -lttf -ljpeg"

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
