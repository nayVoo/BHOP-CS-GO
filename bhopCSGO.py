import pymem
from pymem import process
import keyboard
import time
#OFFSETS (REMEMBER, THIS MAY NOT WORK BECAUSE EVERY UPDATE OFFSETS CHANGES AND U CAN GET BAN IF U USE OLD OFFSETS)
dwLocalPlayer = (0xDEA964) #-->dwLocalPlayer offset 
dwForceJump = (0x52BBC7C) #-->dwForceJump offset
m_fFlags = (0x104) #--> m_fFlags offset

pm = pymem.Pymem('csgo.exe') #here we give to pm characteristic
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll #then we call client_server.dll

def BHOP(): 
	while True:
		if keyboard.is_pressed('end'): #if something went wrong press 'end'
				exit (0)
		try:
			if keyboard.is_pressed('space'):		
				player = pm.read_int(client + dwLocalPlayer) #player its you
				jump = client + dwForceJump # we analize the jump from server acording to our place
				player_state = pm.read_int(player + m_fFlags) 

				if player_state == 257 or player_state == 263: #257 ->pl on ground, 263 -> pl crouch
					pm.write_int(jump, 5)
					time.sleep(0.1) #the lower delay, the more chance for lags
					pm.write_int(jump, 4)
		except:
			pass
		
BHOP()
