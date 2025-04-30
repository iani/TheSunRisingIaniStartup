import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# voice = "Busy old fool, unruly sun, Why dost thou thus, Through windows, and through curtains call on us? Must to thy motions lovers' seasons run? Saucy pedantic wretch, go chide Late school boys and sour prentices, Go tell court huntsmen that the king will ride, Call country ants to harvest offices, Love, all alike, no season knows nor clime, Nor hours, days, months, which are the rags of time"

# voice = "Busy old fool, unruly sun, Why dost thou thus, Through windows, and through curtains call on us?"

# voice = "Busy old fool, unruly sun, Why dost thou thus, Through windows, and through curtains call on us? Must to thy motions lovers' seasons run? Saucy pedantic wretch, go chide Late school boys and sour prentices, Go tell court huntsmen that the king will ride, Call country ants to harvest offices, Love, all alike, no season knows nor clime, Nor hours, days, months, which are the rags of time. Thy beams, so reverend and strong. Why shouldst thou think? I could eclipse and cloud them with a wink, But that I would not lose her sight so long; If her eyes have not blinded thine, Look, and tomorrow late, tell me, Whether both th' Indias of spice and mine. Be where thou leftst them, or lie here with me. Ask for those kings whom thou saw'st yesterday, And thou shalt hear, All here in one bed lay. She's all states, and all princes, I, Nothing else is. Princes do but play us; compared to this,All honor's mimic, all wealth alchemy. Thou, sun, art half as happy as we, In that the world's contracted thus. Thine age asks ease, and since thy duties be. To warm the world, that's done in warming us. Shine here to us, and thou art everywhere; This bed thy center is, these walls, thy sphere."



# https://ubu.com/sound/schwitters.html
# https://ubu.com/media/sound/schwitters_kurt/ursonate/Schwitters-Kurt_Ursonate_03_Dritter_Teil.mp3
# https://ubu.com/media/sound/schwitters_kurt/ursonate/Schwitters-Kurt_Ursonate_01_Einleitung_Und_Erster_Teil.mp3
# https://ubu.com/media/sound/schwitters_kurt/ursonate/Schwitters-Kurt_Ursonate_02_Zweiter_Teil.mp3
# https://ubu.com/media/sound/schwitters_kurt/ursonate/Schwitters-Kurt_Ursonate_04_Vierter_Teil.mp3


voice = [
    "Busy old fool, unruly sun,",
    "Why dost thou thus,",
    "Through windows, and through curtains call on us?",
    "Must to thy motions lovers' seasons run?",
    "Saucy pedantic wretch, go chide",
    "Late school boys and sour prentices,",
    "Go tell court huntsmen that the king will ride,",
    "Call country ants to harvest offices,",
    "Love, all alike, no season knows nor clime,",
    "Nor hours, days, months, which are the rags of time.",

    "Thy beams, so reverend and strong",
    "Why shouldst thou think?",
    "I could eclipse and cloud them with a wink,",
    "But that I would not lose her sight so long;",
    "If her eyes have not blinded thine,",
    "Look, and tomorrow late, tell me,",
    "Whether both th' Indias of spice and mine",
    "Be where thou leftst them, or lie here with me.",
    "Ask for those kings whom thou saw'st yesterday,",
    "And thou shalt hear, All here in one bed lay.",

    "She's all states, and all princes, I,",
    "Nothing else is.",
    "Princes do but play us; compared to this,",
    "All honor's mimic, all wealth alchemy.",
    "Thou, sun, art half as happy as we,",
    "In that the world's contracted thus.",
    "Thine age asks ease, and since thy duties be",
    "To warm the world, that's done in warming us.",
    "Shine here to us, and thou art everywhere;",
    "This bed thy center is, these walls, thy sphere."
]

# Kurt.mp3
# Schwitters-four-clips.mp3
for i in range(0, len(voice)):
    wav = tts.tts(text=voice[i], speaker_wav="/root/audio/Schwitters-four-clips.mp3", language="en")
    # Text to speech to a file
    tts.tts_to_file(text=voice[i], speaker_wav="/root/audio/Schwitters-four-clips.mp3", language="en", file_path="rising-sun-" + str(i) + ".wav")
