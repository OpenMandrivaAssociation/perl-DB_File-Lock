%define real_name DB_File-Lock

Summary:	DB_File-Lock module for perl 
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel, perl-DB_File
BuildArch:	noarch

%description
This module provides a wrapper for the DB_File module, adding locking.

When you need locking, simply use this module in place of DB_File and
add an extra argument onto the tie command specifying if the file should
be locked for reading or writing.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/DB_File/Lock.pm
%{_mandir}/*/*


