%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.50-1

%define languageenglazy Interlingua
%define languagecode ia
%define lc_ctype ia_XX

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Version:	0.50.1
Release:	17
Group:		System/Internationalization
Url:		http://aspell.net/
License:	LGPLv2
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50
# Mandriva Stuff
#there is currently no interlingua locale
#Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	aspell-%{lc_ctype}
Provides:	spell-%{languagecode}
Autoreqprov:	no

%description
An %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
%makeinstall_std

chmod 644 Copyright README* doc/*

%files
%doc README* Copyright 
%doc doc/*
%{_libdir}/aspell-*/*

