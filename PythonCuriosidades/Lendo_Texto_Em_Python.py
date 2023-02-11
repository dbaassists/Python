#importando o módulo pyttsx3
import pyttsx3

#iniciando pyttsx3
motor = pyttsx3.init()

#passando pra ele o texto que gostamos de ouvir
motor.say("""Bom Dia!!!""")

# text o texto
motor.runAndWait()