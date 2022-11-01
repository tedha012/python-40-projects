from gtts import gTTS

text = "안녕하세요. 인공지능 잘하고 싶죠오옹 입니다."

tts = gTTS(text=text, lang="ko")
tts.save(r"./record.mp3")
