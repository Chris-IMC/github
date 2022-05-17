import pyautogui as robot
import time 

respuestap2 = ["el que se fue ala villa perdió su silla"]
respuestap4 = ["estudiante.unal@gmail.com"]

google = -1296,1194
seleccionar_ventana = -1216,1113
nueva_pestaña = -769,119
barra_de_busqueda = -1326,167
seleccionar_respuesta1 = -1286,574
seleccionar_respuesta2 = -1262,759
seleccionar_respuesta3 = -1021,884
seleccionar_respuesta31 = -1106,930
seleccionar_respuesta4 = -944,1012
enviar = -1239,1094
duracion = 10


def abrir(pos,click=1):
    robot.moveTo(pos)
    robot.click(clicks=click)

abrir(google,click=1)  

time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

abrir (seleccionar_ventana,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(nueva_pestaña,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(barra_de_busqueda, click=1)
robot.typewrite("https://forms.office.com/r/S8Jy6Jsvmh")
robot.hotkey("enter")
time.sleep(4)

abrir(seleccionar_respuesta1,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(seleccionar_respuesta2,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(seleccionar_respuesta2, click=1)
robot.typewrite(respuestap2)
robot.hotkey("enter")
time.sleep(4)

time.sleep(3)
abrir(seleccionar_respuesta3,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(seleccionar_respuesta31,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(seleccionar_respuesta4,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")

time.sleep(3)
abrir(seleccionar_respuesta2, click=1)
robot.typewrite(respuestap4)
robot.hotkey("enter")
time.sleep(4)

time.sleep(3)
abrir(enviar,click=1)
time.sleep(2)
robot.hotkey("alt","space")
time.sleep(1)
robot.typewrite("x")