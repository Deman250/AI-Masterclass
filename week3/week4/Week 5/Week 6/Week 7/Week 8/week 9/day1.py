from gtts import gTTS

text = "Hello world! I am a certified Python developer. I love coding and creating amazing applications."
tts = gTTS(text=text, lang='en')
tts.save("hello_world.mp3")
print("Audio file saved as hello_world.mp3")

from gtts import gTTS

text = "I am the best. Today is my  day. I can do it alone. GOD is always with me. I am a winner."
tts = gTTS(text=text, lang='en')
tts.save("i_am_a_winner.mp3")
print("Audio file saved as i_am_a_winner.mp3")
