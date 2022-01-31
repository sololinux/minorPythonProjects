import os
import gtts
from playsound import playsound

print('''
	Select the way to input: 
	------------------------
	[1] Type 
	[2] File
''')
type = int(input('\nEnter your choice (1 or 2): '))

#convert text to speech
def speak(data):
        tts = gtts.gTTS(data, lang = 'en-us')
        tts.save('file.mp3')

        print('''
                +---------------------------------------+
                |                                       |
                |       Playing audio .........         |
                |                                       |
                +---------------------------------------+
        ''')
        #play sound
        playsound('file.mp3')

        #comment this to save the file as .mp3
        os.remove('file.mp3')

#take text to make speech according to choice
if type == 1:
	text = input('\nEnter the text (type): ')
	speak(text)
	
elif type == 2:
	file= input('\nEnter the path of the file (with extention): ')
	text = open(file,'r').read()
	speak(text)	

else:
	print('Invalid input\nExiting program')
