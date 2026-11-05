Name:		kokoro-voices
Version:	1.0
Release:	1
Summary:	Official Kokoro-82M voice packs
License:	Apache-2.0
Group:		System/Multimedia
URL:		https://huggingface.co/hexgrad/Kokoro-82M
# voices/*.pt only. The checkpoint is kokoro-model.
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch
Requires:	%{name}-en = %{EVRD}
Requires:	%{name}-es = %{EVRD}
Requires:	%{name}-fr = %{EVRD}
Requires:	%{name}-hi = %{EVRD}
Requires:	%{name}-it = %{EVRD}
Requires:	%{name}-pt = %{EVRD}
Requires:	%{name}-ja = %{EVRD}
Requires:	%{name}-zh = %{EVRD}

%description
All official Kokoro-82M voice packs: English, Spanish, French, Hindi,
Italian, Brazilian Portuguese, Japanese and Mandarin. Each language
can also be installed on its own. The shared checkpoint is kokoro-model.

%package -n %{name}-en
Summary:	English voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-en
American and British English Kokoro voices. Pronunciation uses the
misaki English lexicon. spaCy is not required.

%package -n %{name}-es
Summary:	Spanish voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-es
Spanish Kokoro voices. Pronunciation uses espeak-ng.

%package -n %{name}-fr
Summary:	French voice for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-fr
French Kokoro voice. Pronunciation uses espeak-ng.

%package -n %{name}-hi
Summary:	Hindi voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-hi
Hindi Kokoro voices. Pronunciation uses espeak-ng.

%package -n %{name}-it
Summary:	Italian voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-it
Italian Kokoro voices. Pronunciation uses espeak-ng.

%package -n %{name}-pt
Summary:	Brazilian Portuguese voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-pt
Brazilian Portuguese Kokoro voices. Pronunciation uses espeak-ng.

%package -n %{name}-ja
Summary:	Japanese voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-ja
Japanese Kokoro voice packs. The weights are installed. Japanese
grapheme-to-phoneme support is not part of python-misaki yet, so
synthesis with these voices stops until that support is packaged.

%package -n %{name}-zh
Summary:	Mandarin voices for Kokoro
Group:		System/Multimedia
Requires:	kokoro-model >= 1.0
Requires:	python-kokoro >= 0.9.4

%description -n %{name}-zh
Mandarin Kokoro voice packs for the Kokoro-82M checkpoint. The weights
are installed. Mandarin grapheme-to-phoneme support is not part of
python-misaki yet, so synthesis with these voices stops until that
support is packaged.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -m 644 voices/*.pt %{buildroot}%{_datadir}/kokoro/voices/

%files
%doc VOICES.md

%files -n %{name}-en
%{_datadir}/kokoro/voices/a*.pt
%{_datadir}/kokoro/voices/b*.pt

%files -n %{name}-es
%{_datadir}/kokoro/voices/e*.pt

%files -n %{name}-fr
%{_datadir}/kokoro/voices/f*.pt

%files -n %{name}-hi
%{_datadir}/kokoro/voices/h*.pt

%files -n %{name}-it
%{_datadir}/kokoro/voices/i*.pt

%files -n %{name}-ja
%{_datadir}/kokoro/voices/j*.pt

%files -n %{name}-pt
%{_datadir}/kokoro/voices/p*.pt

%files -n %{name}-zh
%{_datadir}/kokoro/voices/z*.pt
