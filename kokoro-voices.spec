Name:		kokoro-voices
Version:	1.0
Release:	1
Summary:	All official Kokoro voices
URL:		https://huggingface.co/hexgrad/Kokoro-82M
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Requires:	kokoro-voice-af_alloy
Requires:	kokoro-voice-af_aoede
Requires:	kokoro-voice-af_bella
Requires:	kokoro-voice-af_heart
Requires:	kokoro-voice-af_jessica
Requires:	kokoro-voice-af_kore
Requires:	kokoro-voice-af_nicole
Requires:	kokoro-voice-af_nova
Requires:	kokoro-voice-af_river
Requires:	kokoro-voice-af_sarah
Requires:	kokoro-voice-af_sky
Requires:	kokoro-voice-am_adam
Requires:	kokoro-voice-am_echo
Requires:	kokoro-voice-am_eric
Requires:	kokoro-voice-am_fenrir
Requires:	kokoro-voice-am_liam
Requires:	kokoro-voice-am_michael
Requires:	kokoro-voice-am_onyx
Requires:	kokoro-voice-am_puck
Requires:	kokoro-voice-am_santa
Requires:	kokoro-voice-bf_alice
Requires:	kokoro-voice-bf_emma
Requires:	kokoro-voice-bf_isabella
Requires:	kokoro-voice-bf_lily
Requires:	kokoro-voice-bm_daniel
Requires:	kokoro-voice-bm_fable
Requires:	kokoro-voice-bm_george
Requires:	kokoro-voice-bm_lewis
Requires:	kokoro-voice-ef_dora
Requires:	kokoro-voice-em_alex
Requires:	kokoro-voice-em_santa
Requires:	kokoro-voice-ff_siwis
Requires:	kokoro-voice-hf_alpha
Requires:	kokoro-voice-hf_beta
Requires:	kokoro-voice-hm_omega
Requires:	kokoro-voice-hm_psi
Requires:	kokoro-voice-if_sara
Requires:	kokoro-voice-im_nicola
Requires:	kokoro-voice-jf_alpha
Requires:	kokoro-voice-jf_gongitsune
Requires:	kokoro-voice-jf_nezumi
Requires:	kokoro-voice-jf_tebukuro
Requires:	kokoro-voice-jm_kumo
Requires:	kokoro-voice-pf_dora
Requires:	kokoro-voice-pm_alex
Requires:	kokoro-voice-pm_santa
Requires:	kokoro-voice-zf_xiaobei
Requires:	kokoro-voice-zf_xiaoni
Requires:	kokoro-voice-zf_xiaoxiao
Requires:	kokoro-voice-zf_xiaoyi
Requires:	kokoro-voice-zm_yunjian
Requires:	kokoro-voice-zm_yunxi
Requires:	kokoro-voice-zm_yunxia
Requires:	kokoro-voice-zm_yunyang

%description
Metapackage that installs every official Kokoro-82M voice.
Each voice is also available on its own as kokoro-voice-*.
Those voices use the checkpoint in kokoro-model.
The German Thorsten fine-tune is kokoro-voice-thorsten and is not included here.

%install
mkdir -p %{buildroot}
echo 'Each voice is a separate kokoro-voice-* package.' > README-voices

%files
%doc README-voices
