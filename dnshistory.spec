Summary:	dnshistory - storing a history of DNS/Name changes
Name:		dnshistory
%define		_beta	beta1
Version:	1.3
Release:	0.1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.stedee.id.au/files/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	c9843e87412c1bdf8fb2ec5983f0c9c4
URL:		http://www.stedee.id.au/dnshistory/
BuildRequires:	db-devel
BuildRequires:	pcre-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dnshistory provides a means for storing a history of DNS/Name changes
for the IP Addresses extracted from web log files. The major target
being that multiple analyses of older log files do not require
re-lookups of IP Address to FQDNs, and additionally maintain the
accuracy of the lookup as it was then and not as it is now.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*.1*
