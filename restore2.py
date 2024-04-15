import os
from time import sleep

title=r"""
 ___   ____  __  _____   __    _     ___    __    ___   ___   ___  
| |_) | |_  ( (`  | |   / /\  | | | | |_)  / /\  | | \ / / \ | |_) 
|_| \ |_|__ _)_)  |_|  /_/--\ \_\_/ |_| \ /_/--\ |_|_/ \_\_/ |_| \
"""
print(title)
sleep(2)

backups_dir='backups'

carpetas=sorted(os.listdir(backups_dir))

for i,c in enumerate(carpetas):
	fecha=c.split("data_")[1].split(".db")[0]
	print(i,"fecha:",fecha)

decision=input('¿Qué backup quieres restaurar?: ')
print("︵‿︵‿୨♡୧‿︵‿︵")
print("Muy bien, vamos a restaurar el archivo ",carpetas[int(decision)])
print("︵‿︵‿୨♡୧‿︵‿︵")

