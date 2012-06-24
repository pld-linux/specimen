#
# Conditional build
%bcond_with ladcca	# build with LADCCA support
#
Summary:	MIDI controlled audio sampler
Summary(pl):	Kontrolowany przez MIDI sampler d�wi�kowy
Name:		specimen
Version:	0.2.9
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.gazuga.net/%{name}-%{version}.tar.gz
# Source0-md5:	86faf7a9c6a62e079e47107be9529f7c
Source1:	%{name}.desktop
URL:		http://www.gazuga.net/
%{?with_ladcca:BuildRequires:	ladcca-devel >= 0.4.0}
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libgnomecanvas-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Specimen is a MIDI controlled audio sampler for GNU/Linux systems. It
allows to create music using various sound files, or "samples", in
tandem with a midi sequencer.

%description -l pl
Specimen jest kontrolowanym z poziomu MIDI samplerem d�wi�kowym dla
sytem�w GNU/Linux. Pozwala na tworzenie muzyki z przer�nych plik�w
d�wi�kowych czy te� "sampli" w po��czeniu z sekwencerem MIDI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ladcca=%{?with_ladcca:yes}%{!?with_ladcca:no}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/specimen
%{_datadir}/specimen/pixmaps
%{_desktopdir}/*.desktop
