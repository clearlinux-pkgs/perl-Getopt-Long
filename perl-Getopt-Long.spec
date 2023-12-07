#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: c1050fe40c24
#
Name     : perl-Getopt-Long
Version  : 2.57
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/J/JV/JV/Getopt-Long-2.57.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JV/JV/Getopt-Long-2.57.tar.gz
Summary  : 'Module to handle parsing command line options'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0+
Requires: perl-Getopt-Long-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Examples (skeletons) for applications that use Getopt::Long.
skel1.pl: simple, straightforward use of Getopt::Long.

%package dev
Summary: dev components for the perl-Getopt-Long package.
Group: Development
Provides: perl-Getopt-Long-devel = %{version}-%{release}
Requires: perl-Getopt-Long = %{version}-%{release}

%description dev
dev components for the perl-Getopt-Long package.


%package perl
Summary: perl components for the perl-Getopt-Long package.
Group: Default
Requires: perl-Getopt-Long = %{version}-%{release}

%description perl
perl components for the perl-Getopt-Long package.


%prep
%setup -q -n Getopt-Long-2.57
cd %{_builddir}/Getopt-Long-2.57

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Getopt::Long.3
/usr/share/man/man3/Getopt::Long::Parser.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
