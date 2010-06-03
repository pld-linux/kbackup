%define		qtver		4.6.2
%define		kdever		4.4.4

Summary:	kbackup
Summary(pl.UTF-8):	kbackup
Name:		kbackup
Version:	0.6.4
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/44998-%{name}-%{version}.tar.bz2
# Source0-md5:	a28f3e548f52f8396235f3b2fdcb2275
URL:		http://members.aon.at/m.koller/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBackup is a program that lets you back up any directories or files,
whereby it uses an easy to use directory tree to select the things to
back up. It lets you save your settings in so called "profile" files,
where a profile is a simple textfile containing definitions for
directories and files to be included or excluded from the backup
process. Also, it lets you define where the backup shall be saved to.
The target can be either a local directory (e.g. a local mounted
device like a ZIP drive, USB stick, etc.) but it can also be any
remote URL (e.g. smb://remote/some_path) to back up your data to some
central server, etc.

%description -l pl.UTF-8

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackup
%{_desktopdir}/kde4/kbackup.desktop
%{_datadir}/apps/kbackup
%{_datadir}/mime/packages/kbackup.xml
%{_iconsdir}/hicolor/*x*/apps/kbackup.png
%{_iconsdir}/hicolor/*x*/mimetypes/text-x-kbp.png
%lang(de) %{_kdedocdir}/de/kbackup
%lang(en) %{_kdedocdir}/en/kbackup
%lang(fr) %{_kdedocdir}/fr/kbackup
%lang(ru) %{_kdedocdir}/ru/kbackup
