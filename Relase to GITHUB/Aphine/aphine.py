import speech_recognition as sr 
import webbrowser
import pyaudio
import pyttsx3
import os
import pyowm
import random
from colorama import Fore, Back, Style
from colorama import init
init()
print(Style.BRIGHT)

answers_weather={
	1 : 'Сейчас узнаю...',
	2 : 'Уже узнаю...',
	3 : 'Я уже...',
	4 : 'хорошо узнаю...',
	5 : 'Ок...',
	6 : 'Афина узнает погоду в любом регионе...'
}
answers={
	1 : 'Уже открываю...',
	2 : 'Будет исполнено...',
	3 : 'Хорошо открываю...',
	4 : 'ок...',
	5 : 'хорошо',
	6 : 'ладно'
}
colors={
	1 : 'RED',
	2 : 'GREEN',
	3 : 'YELLOW',
	4 : 'BLUE',
	5 : 'MAGENTA',
	6 : 'CYAN'
}
def replace_path(path):
		list_path_raplaced=path.replace('\n','')
		path_use=list_path_raplaced
		return path_use
def read_path(index):
    file=open('setAphinePath.txt')    # 'r' не нужно
    for i in range(index - 1):       # __  значит, что имя переменной не важно
        file.readline()               # читаем, но не сохраняем
    content_no_use = file.readline() # теперь уже строку сохраним - в переменной content
    content=replace_path(content_no_use)
    file.close()
    # print(content)                  # это не нужно, но может выть для тестирования
    return content
		
owm= pyowm.OWM('8b5c6d0735747fd07560cac15b1e3609',language = "RU")
def randcolor():
	rand=random.randint(1, 6)
	color=colors.get(rand)
	return color 
def read_set_sys(types):
	FiCoAs=open('setAphineColorAsk.txt','r')
	FiCoAn=open('setAphineColorAnswer.txt','r')
	FiCoEr=open('setAphineColorError.txt','r')
	asRead=FiCoAs.read()
	anRead=FiCoAn.read()
	erRead=FiCoEr.read()
	FiCoAs.close()		
	FiCoAn.close()
	FiCoEr.close()
	if types=="ask":
		if asRead=='RANDOM':
			color=randcolor()	
			if color=='RED':
				print(Back.RED)
			elif color=='GREEN':
				print(Back.GREEN)
			elif color=='YELLOW':
				print(Back.YELLOW)
			elif color=='BLUE':
				print(Back.BLUE)
			elif color=='MAGENTA':
				print(Back.MAGENTA)
			elif color=='CYAN':
				print(Back.CYAN)
		elif asRead=='RED':
			print(Back.RED)
		elif asRead=='GREEN':
			print(Back.GREEN)
		elif asRead=='YELLOW':
			print(Back.YELLOW)
		elif asRead=='BLUE':
			print(Back.BLUE)
		elif asRead=='MAGENTA':
			print(Back.MAGENTA)
		elif asRead=='CYAN':
			print(Back.CYAN)	

	if types=='answer':
		if anRead=='RANDOM':
			color=randcolor()	
			if color=='RED':
				print(Back.RED)
			elif color=='GREEN':
				print(Back.GREEN)
			elif color=='YELLOW':
				print(Back.YELLOW)
			elif color=='BLUE':
				print(Back.BLUE)
			elif color=='MAGENTA':
				print(Back.MAGENTA)
			elif color=='CYAN':
				print(Back.CYAN)							
		elif anRead=='RED':
			print(Back.RED)
		elif anRead=='GREEN':
			print(Back.GREEN)
		elif anRead=='YELLOW':
			print(Back.YELLOW)
		elif anRead=='BLUE':
			print(Back.BLUE)
		elif anRead=='MAGENTA':
			print(Back.MAGENTA)
		elif anRead=='CYAN':
			print(Back.CYAN)
	if types=='error':
		if asRead=='RANDOM':
			color=randcolor()	
			if color=='RED':
				print(Back.RED)
			elif color=='GREEN':
				print(Back.GREEN)
			elif color=='YELLOW':
				print(Back.YELLOW)
			elif color=='BLUE':
				print(Back.BLUE)
			elif color=='MAGENTA':
				print(Back.MAGENTA)
			elif color=='CYAN':
				print(Back.CYAN)
		elif erRead=='RED':
			print(Back.RED)
		elif erRead=='GREEN':
			print(Back.GREEN)
		elif erRead=='YELLOW':
			print(Back.YELLOW)
		elif erRead=='BLUE':
			print(Back.BLUE)
		elif erRead=='MAGNETA':
			print(Back.MAGNETA)
		elif erRead=='CYAN':
			print(Back.CYAN)			
def answer():
	rand=random.randint(1, 6)
	answ=answers.get(rand)
	return answ
def talk(words):
	print(words)
	engine=pyttsx3.init()
	engine.say(words)
	engine.runAndWait()
talk('Привет меня зовут Афина')	
talk('я вас слушаю')
def user_command():
	r=sr.Recognizer()

	with sr.Microphone()as source:
		read_set_sys('ask')
		print('говорите')
		r.pause_threshold=0.5
		audio=r.listen(source)
	try:
		user_text=r.recognize_google(audio,language='ru-RU').lower()
		read_set_sys('ask')		
		print(user_text)
 			
	except sr.UnknownValueError:
		read_set_sys('error')
		print("Попал в except")
		user_text=user_command()	
	return user_text	
def answer_weather():
	randoming=random.randint(1, 6)
	ans=answers_weather.get(randoming)
	return ans
def command(user_text):
		sleep=0
		read_set_sys('answer');
		if 'браузер' in user_text: 
			talk(answer())
			os.startfile(r'C:/Program Files/Opera/launcher.exe')
		elif 'youtube'in user_text:
			talk(answer())
			webbrowser.open("https://www.youtube.com/?gl=IN&hl=en-GB")
		elif 'vk'in user_text:
			talk(answer())
			webbrowser.open("https://vk.com/feed")
		elif 'приложение 1' in user_text:
			talk(answer())
			print(read_path(1))
			os.startfile(read_path(1))
		elif 'приложение 2'in user_text:
			talk(answer())
			print(read_path(2))
			os.startfile(read_path(2))		
		elif 'приложение 3'in user_text:
			talk(answer())
			print(read_path(3))
			os.startfile(read_path(3))		
		elif 'пока'in user_text:
			talk('Хорошо,До скорых встреч')
			quit()
		elif 'погоду' in user_text:
			talk("введите город(Например:Москва)")
			place=input('Введи город(с заглавной буквы)')
			observation=owm.weather_at_place(place)
			w=observation.get_weather()
			temp=w.get_temperature('celsius')['temp']
			hum=w.get_humidity()
			talk(answer_weather())
			talk(w.get_detailed_status())
			talk('Температура в городе ' + place + str(temp)+' цельсий')
			talk('влажность равна:'+str(hum))
		elif 'найди в интернете' in user_text:
			talk('что ищем')
			query=input('введите запрос: ')
			webbrowser.open('https://www.google.ru/search?q='+query)
		elif 'пробей номер' in user_text :
			talk('Введите номер ниже')
			number_car=input(': ')
			number_car=number_car.upper()
			webbrowser.open('https://avtocod.ru/proverkaavto/'+number_car+'?rd=GRZ')
		elif 'войти в спящий режим' in user_text:
			sleep=1
			talk('Ложусь спать')			
		else:
			read_set_sys('error')
			talk('я не поняла повторите')
		return sleep;	
def command_sleep(user_text):
		sleep=1
		if 'браузер' in user_text: 

			os.startfile(r'C:/Program Files/Opera/launcher.exe')
		elif 'youtube'in user_text:

			webbrowser.open("https://www.youtube.com/?gl=IN&hl=en-GB")
		elif 'vk'in user_text:

			webbrowser.open("https://vk.com/feed")
		elif 'приложение 1' in user_text:
			print(read_path(1))
			os.startfile(read_path(1))
		elif 'приложение 2'in user_text:
			print(read_path(2))
			os.startfile(read_path(2))
		elif 'приложение 3'in user_text:
			print(read_path(3))
			os.startfile(read_path(3))		
		elif 'пока'in user_text:
			quit()
		elif 'погоду' in user_text:
			place=input('Введи город(с заглавной буквы)')
			observation=owm.weather_at_place(place)
			w=observation.get_weather()
			temp=w.get_temperature('celsius')['temp']
			hum=w.get_humidity()
			print(answer_weather())
			print(w.get_detailed_status())
			print('Температура в городе ' + place + str(temp)+' цельсий')
			print('влажность равна:'+str(hum))
		elif 'найди в интернете' in user_text:
			query=input('введите запрос: ')
			webbrowser.open('https://www.google.ru/search?q='+query)
		elif 'пробей номер' in user_text:
			number_car=input(': ')
			number_car=number_car.upper()
			webbrowser.open('https://avtocod.ru/proverkaavto/'+number_car+'?rd=GRZ')
		elif 'выйти из спящего режима' in user_text:
			sleep=0
			talk('я проснулась и готова к работе')				
		else:
			pass
		return sleep	
while True:
	sleep1=command(user_command())

	print(str(sleep1))
	if sleep1==1:
		while sleep1==1:
			sleep1=command_sleep(user_command())
	