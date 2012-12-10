Name:		hexglass
Version:	1.2.1
Release:	%mkrel 1
Summary:	Block falling puzzle game based on a hexagonal grid 
Group:		Games/Puzzles
License:	GPLv3+
URL:		http://code.google.com/p/hexglass
Source0:	http://hexglass.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
# Let the application search for locale files in
# /usr/share/hexglass/translations/
Patch0:		hexglass-1.2.1-locale-path.patch
BuildRequires:	qt4-devel

%description
HexGlass is a Tetris-like puzzle game. Ten different types of blocks
continuously fall from above and you must arrange them to make horizontal
rows of hexagonal bricks. Completing any row causes those hexagonal blocks
to disappear and the rest above move downwards. The blocks above gradually
fall faster and the game is over when the screen fills up and blocks can
no longer fall from the top.

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4 hexglass.pro
%make

%install
%__rm -rf %{buildroot}
%__install -D hexglass %{buildroot}%{_bindir}/hexglass
%__install -d %{buildroot}%{_datadir}/%{name}/translations
%__install -m 644 -p translations/*.qm %{buildroot}%{_datadir}/%{name}/translations
%__install -D -m 644 -p resources/about_icon.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# menu-entry
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=HexGlass
Comment=Tetris-like puzzle game based on a hexagonal grid
Comment[de]=Tetris-ähnliches Puzzlespiel auf einem sechseckigen Raster
Exec=hexglass
Icon=hexglass
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc CHANGES COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm



%changelog
* Tue Mar 27 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2.1-1mdv2011.0
+ Revision: 787382
- imported package hexglass

