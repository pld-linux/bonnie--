Summary:	A program for benchmarking hard drives and filesystems
Summary(pl):	Program mierz±cy wydajno¶æ twardych dysków i systemów plików
Name:		bonnie++
Version:	1.01d
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://www.coker.com.au/bonnie++/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of
simple tests of hard drive and file system performance.

%description -l pl
Bonnie++ jest zestawem benchmarków, których celem jest przeprowadzenie
prostych testów wydajno¶ci twardego dysku i systemu plików.

%prep
%setup -q

%build
autoconf
./configure --prefix=${RPM_BUILD_ROOT}
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/{man1,man8}}
install bonnie++ zcav $RPM_BUILD_ROOT%{_sbindir}
install bon_csv2html bon_csv2txt $RPM_BUILD_ROOT%{_bindir}
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/changelog readme.html

%attr(755,root,root) %{_sbindir}/bonnie++
%attr(755,root,root) %{_sbindir}/zcav
%attr(755,root,root) %{_bindir}/bon_csv2html
%attr(755,root,root) %{_bindir}/bon_csv2txt
%{_mandir}/man*/*
