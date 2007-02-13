%define		_ver	1_32
Summary:	Squid statistic tool
Summary(pl.UTF-8):	Narzędzie do statystyki squida
Name:		prostat
Version:	1.32
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.serveurs-nationaux.jussieu.fr/cache/prostat/%{name}_%{_ver}.tar.gz
# Source0-md5:	757b39c69e0dc66a169c23dcc25db560
Patch0:		%{name}-paths.patch
URL:		http://cache.cnrs.fr/prostat/
BuildRequires:	gd-devel
Requires:	/etc/mime.types
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Prostat is a squid statistic tool.

%description -l pl.UTF-8
Prostat jest narzędziem do statystyk squida.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LIBS="-lm -lgd"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_datadir}/prostat}

install prostat $RPM_BUILD_ROOT%{_bindir}
install prostat.conf $RPM_BUILD_ROOT%{_sysconfdir}
install domains.tab $RPM_BUILD_ROOT%{_datadir}/prostat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGE
%lang(fr) %doc LISEZ_MOI
%attr(755,root,root) %{_bindir}/prostat
%dir %{_datadir}/prostat
%{_datadir}/prostat/domains.tab
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/prostat.conf
