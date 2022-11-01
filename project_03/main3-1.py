from gtts import gTTS

text = "뽀리 뒤지고 싶습니까? 어디 가셨습니까"

tts = gTTS(text=text, lang="ko")
tts.save(r"./record.mp3")
