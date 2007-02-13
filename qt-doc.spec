
%define		_qt_ver		3.0
%define		_mirror_date	2002-06-20

%define		_dir		%{_qt_ver}-%{_mirror_date}
%define		_ver		%(echo %{_dir} | sed 's/-/_/g')

Summary:	Documentation for Qt
Summary(pl.UTF-8):	Dokumentacja Qt
Name:		qt-doc
Version:	%{_ver}
Release:	3
License:	distributable
Group:		Documentation
Source0:	%{name}-%{_dir}.tar.bz2
# Source0-md5:	2b930686d40f5316e95f90675218cf49
BuildRequires:	sed
URL:		http://doc.trolltech.com/3.0/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains mirror of doc.trolltech.com/3.0/ There are various
tutorials, APIs and other documents.

%description -l pl.UTF-8
Pakiet zawiera mirror doc.trolltech.com/3.0/ Znajdują się w nim różne
tutoriale, opisy API i inne dokumenty.

%prep
%setup -q -n %{name}-%{_dir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc .
