# Import the Gtts module for text  
# to speech conversion 
from gtts import gTTS 
  
# import Os module to start the audio file
import os

#อ่านtextจากfile
file = open("./gTTS/input/interview_emma watson.txt", "r").read().replace("\n", " ")

# Language
language = 'en'

output = gTTS(text=str(file), lang=language, slow=False)

output.save("./gTTS/output/output.mp3")

file.close()

# Play the converted file 
os.system("start output.mp3")