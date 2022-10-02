# Se importan bibliotecas para la comunicación con la Raspberry y manejar las fechas.
from nbformat import write
from setuptools import setup
import RPi.GPIO as GPIO  #Biblioteca para manejo de pines
import time              #Biblioteca para funciones de tiempo
from datetime import datetime   #Biblioteca para manejo de fechas

#Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER,False)

sFileStamp = time.strftime("%Y%m%d%H")  #Se define el formato de fecha
sFileName = "\out" + sFileStamp + ".txt" #Se genera un archivo donde se almacena el nombre que tendrá el archibo

f = open(sFileName, "a")    #Se abre el archivo dándole como argumento la variable que se creó para almacenar el nombre del archivo
f.write("TimeStamp, Value" + "\n")  #Se imprime una primera líena en el documento
print("Inicia la toma de datos") #Se envía un mensaje en cosola que indica que se inicia la toma de datos

try:
    while True:
        print("Acerque el objeto para medir la distancia")
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER,False)
        start = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()
        elapsed = stop-start
        distancia = (elapsed*343000)/2
        sTimeStamp = time.strftime("%Y%m%d%H%M%S")
        f.write(sTimeStamp + "," + str(distancia) + "\n")
        print(sTimeStamp + " " + str(distancia))
        time.sleep(1)
        if sTmpFileStamp != sFileStamp:
            f.close
            sFileName = "out/" + sTmpFileStamp + ".txt"
            f = open(sFileName, "a")
            sFileStamp = sTmpFileStamp
            print("Creando el archivo")
except KeyboardInterrupt:
    print("\n" + "Termina la captura de datos" + "\n")
    f.close
    GPIO.cleanup()

