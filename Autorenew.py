import pyautogui as pa
import subprocess as sp
import password
import os
import pyscreeze
import time

path = "C:\\Program Files\\PuTTY\\Putty.exe"
sp.Popen(path)
time.sleep(.5)
x,y = pa.locateCenterOnScreen('Images\\ESXi.png')
pa.doubleClick(x,y)
pa.typewrite("root")
pa.press('enter')
pa.typewrite('' + os.environ.get(password.rootpw)
pa.press('enter')
time.sleep(.2)
pa.typewrite("rm -r /etc/vmware/license.cfg")
pa.press('enter')
pa.typewrite('y')
pa.press('enter')
pa.typewrite("cp /etc/vmware.#license.cfg /etc/vmware/license.cfg")
pa.press('enter')
pa.typewrite("/etc/init.d/vpxa restart")
pa.hotkey('alt', 'F4')
pa.press('enter')
time.sleep(1)