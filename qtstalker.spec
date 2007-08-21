%define Summary Stock market, commodity and technical analysis charting app

Name:       	qtstalker
Version:    	0.33
Release:    	%mkrel 1
Summary:    	%Summary
License:    	GPL
Group:      	Graphical desktop/Other
URL:        	http://qtstalker.sourceforge.net
Source:     	http://downloads.sourceforge.net/qtstalker/qtstalker-%version.tar.gz
Patch:  	qtstalker-0.33-build_fix_x86_64.patch
BuildRoot:  	%_tmppath/%name-buildroot
BuildRequires:	db4.2-devel
BuildRequires:	libqt-devel
Requires(post,postun): desktop-common-data

%description
Stock market, commodity and technical analysis charting app based on the Qt
toolkit. Extendible plugin system for quotes and indicators. Portfolio, back
testing, chart objects and many more features included.

%prep
%setup -q -n %name
%patch -p1 -b .build_fix_x86_64

sed -i 's|@@LIBDIR@@|%_libdir|g' lib/Config.cpp
sed -i 's|/usr/lib/qtstalker|%_libdir/qtstalker|g' \
	docs/install.html docs/faq.html

%build
./configure
make

%install
rm -rf %buildroot
make INSTALL_ROOT=%buildroot LIBDIR=%_libdir install

mkdir %buildroot/%_datadir/pixmaps
cp pics/%name.xpm %buildroot/%_datadir/pixmaps

mkdir -p %buildroot/%_datadir/applications
cat > %buildroot%_datadir/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Name=Qtstalker
Comment=%Summary
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Finances;Office;Finance;
Encoding=UTF-8
EOF

# Package with doc macro
mv %buildroot/%_datadir/doc/qtstalker/html .

%post
/sbin/ldconfig
%update_menus

%postun
/sbin/ldconfig
%clean_menus

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/qtstalker
%defattr(0644,root,root,0755)
%doc docs/{AUTHORS,BUGS,CHANGELOG,COPYING,TODO} html
%_datadir/applications/mandriva-%name.desktop
%_datadir/pixmaps/%name.xpm
%_datadir/qtstalker
%_libdir/libqtstalker.*
%_libdir/qtstalker
