import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_DHT

import time

#Funcao para acionamento do servo
#Possui como padrao o angulo zero para o
#servo e o coloca em 90 graus quando 
#chamada pela condicao feita
def acionamento_servo(angulo=0):
    GPIO.output(ledServoPin, GPIO.HIGH) 
    print('\n ESTOU NO SERVO!!! {}'.format(angulo))
    dutyCycle=1./18.*angulo + 2
    PWM.set_duty_cycle(servoPin,dutyCycle)
    time.sleep(3)
    GPIO.output(ledServoPin, GPIO.LOW)
    
#Funcao para acionamento do motor dc do
#do cooler
#recebe como parametro a variavel x
#que determinara velocidade maxima, ou
#minima de acordo com a condicao que chamou
#a funcao
def acionamento_motor(x):
    GPIO.output(ledMotorPin, GPIO.HIGH) 
    if x == 0:
        PWM.set_duty_cycle(motorPin, 30)
        print('\n Cooler 1/10 Velocidade')
    else:
        PWM.set_duty_cycle(motorPin, 100)
        print('\n Cooler 10/10 Velocidade')

#Funcao para acionamento do rele que
#controla a bomba
#recebe como parametro a humidade lida
#que determinara bomba ligada, ou
#desligada de acordo com a condicao 
#definida como humidade 58%
def acionamento_rele(humidity):
    if (humidity < 58):
        print('\n Umidade abaixo de 58! Iniciando rele')
        GPIO.output(relePin, GPIO.LOW) #Liga rele
        time.sleep(20)
        print('\n Umidade ok! Desligando rele')
        GPIO.output(relePin, GPIO.HIGH) #Desliga rele

# --------- Seta Pinos ----------------
ledServoPin = 'P8_16'
ledMotorPin = 'P8_18'

servoPin = "P9_14"
motorPin ="P8_13"
out = "P9_12" 
GPIO.setup(out,GPIO.OUT)
GPIO.output(out,GPIO.HIGH)
sensorPin = 'P8_11'
relePin = "P8_10"

print('Pinos configurados!')

# --------- Configura Sensor de Temperatura----------------
sensor_DHT = Adafruit_DHT.DHT11

print('Sensor configurados!')
temperatura_inicial = None

while temperatura_inicial == None :
    umidade , temperatura_inicial = Adafruit_DHT.read_retry(sensor_DHT, sensorPin)
    print('x')


print('Essa e a temperatura inicial {}'.format(temperatura_inicial))

print('Temperatudra configurados!')

# --------- Seta pinos rele----------------
GPIO.setup(relePin, GPIO.OUT)   #Seta pino do rele 
GPIO.output(relePin, GPIO.LOW) #Estado inicial rele desligado
GPIO.setup(ledServoPin, GPIO.OUT)  
GPIO.output(ledServoPin, GPIO.LOW) 
GPIO.setup(ledMotorPin, GPIO.OUT)  
GPIO.output(ledMotorPin, GPIO.LOW) 

print('Pinos setados')

# --------- Seta saidas PWM motor e servo----------------
PWM.start(motorPin, 0, 100) # Seta PWM do motor
PWM.start(servoPin, 2, 65) #Seta PWM do servo

while(True):
    
    print('entramos na funcao')
    umidade, temperatura_lida = Adafruit_DHT.read_retry(sensor_DHT, sensorPin)
    print('TEMPERATURA:{} ----- UMIDADE:{}' .format(temperatura_lida,umidade))
    variacao = temperatura_lida - temperatura_inicial
    print('\n Delta de Temperatura {}'.format(variacao))
    acionamento_rele(umidade)
    
    #Abaixo seguem todas as condicoes que
    #regem o comportamento do cooler e do
    #servo 
    if(variacao < 2 and variacao > 0.1):
        print('\n Variacao entre 0 -- 2')
        print('\n A porta sera fechada e o motor acionado!')
        #acionamento_servo(0)
        acionamento_motor(1)

    elif(variacao >= 2):
        print('\n Variacao maior que 2')
        print('\n A porta sera aberta e o motor acionado!')
        #acionamento_servo(90)
        acionamento_motor(1)

    elif(variacao <= 0.1):
        print('\n Nao ha variacao !')
        print('\n A porta sera aberta e o motor acionado!')
        #acionamento_servo(0)
        acionamento_motor(0)
    
    print('\n------------------Restart do Loop-------------------------')
    
    time.sleep(10)
  
PWM.cleanup()
GPIO.cleanup()