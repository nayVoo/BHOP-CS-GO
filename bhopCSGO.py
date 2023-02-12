import pymem
from pymem import process
import keyboard
import time


dwLocalPlayer = (0xDEA964)
dwForceJump = (0x52BBC7C)
m_fFlags = (0x104)

pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

def BHOP():
	while True:
		if keyboard.is_pressed('end'):
				exit (0)
		try:
			if keyboard.is_pressed('space'):		
				player = pm.read_int(client + dwLocalPlayer)
				jump = client + dwForceJump
				player_state = pm.read_int(player + m_fFlags)

				if player_state == 257 or player_state == 263: #pl on ground
					pm.write_int(jump, 5)
					time.sleep(0.1)
					pm.write_int(jump, 4)
		except:
			pass
		
BHOP()