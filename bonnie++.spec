Summary:	A program for benchmarking hard drives and filesystems
Summary(es):	Benchmark (prueba de desempeño) Bonnie para Sistemas de Archivos Unix
Summary(pl):	Program mierz±cy wydajno¶æ twardych dysków i systemów plików
Summary(pt_BR):	Benchmark (teste de performance) Bonnie para Sistemas de Arquivos Unix
Name:		bonnie++
Version:	1.02
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.coker.com.au/bonnie++/%{name}-%{version}.tgz
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bonnie++ is a benchmark suite that is aimed at performing a number of
simple tests of hard drive and file system performance.

%description -l es
Bonnie es un benchmark (prueba de desempeño) popular que verifica
varios aspectos de sistemas de archivos Unix.

%description -l pl
Bonnie++ jest zestawem benchmarków, których celem jest przeprowadzenie
prostych testów wydajno¶ci twardego dysku i systemu plików.

%description -l pt_BR
Bonnie é um benchmark (teste de performance) popular que verifica
vários aspectos de sistemas de arquivos Unix.

%prep
%setup -q

%build
autoconf
%configure
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
