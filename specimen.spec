Summary:	MIDI controlled audio sampler
Summary(pl):	Kontrolowany przez MIDI sampler d¼wiêkowy
Name:		specimen
Version:	0.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.gazuga.net/%{name}-%{version}.tar.gz
# Source0-md5:	a629126c0921cdf952554af4a884ea1c
Source1:	%{name}.desktop
URL:		http://www.gazuga.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Specimen is a MIDI controlled audio sampler for GNU/Linux systems. It
allows to create music using various sound files, or "samples", in
tandem with a midi sequencer.

%description -l pl
Specimen jest kontrolowanym z poziomu MIDI samplerem d¼wiêkowym dla
sytemów GNU/Linux. Pozwala na tworzenie muzyki z przeró¿nych plików
d¼wiêkowych czy te¿ "próbek", w po³±czeniu z sekwencerem MIDI.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%{_pixmapsdir}/%{name}
%{_desktopdir}/*.desktop
