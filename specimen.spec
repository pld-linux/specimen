#
# Conditional build
%bcond_with	ladcca	# build with LADCCA support
#
Summary:	MIDI controlled audio sampler
Summary(pl):	Kontrolowany przez MIDI sampler d�wi�kowy
Name:		specimen
Version:	0.4.5
Release:	3
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://www.gazuga.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	5eea21c579d24b825f7a77c3988c9eec
Source1:	%{name}.desktop
Patch0:		%{name}-64bit.patch
URL:		http://www.gazuga.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	jack-audio-connection-kit-devel >= 0.90.0
%{?with_ladcca:BuildRequires:	ladcca-devel >= 0.4.0}
BuildRequires:	libgnomecanvas-devel >= 2.0
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	perl-base
BuildRequires:	phat-devel >= 0.2.2
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2:2.4
Requires:	jack-audio-connection-kit >= 0.90.0
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
%patch0 -p1

%{__perl} -pi -e 's/CFLAGS="-O3"/:/' configure.ac

%build
%{__aclocal} -I .
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
