import microbit
from microbit import Image
import time
from det_key import PressKey, ReleaseKey, W, A, S, D , SHF
#Function for Changing a Key
def update_press(key, value):
	global keyboard_keys
	if value!=keyboard_keys.get(key, False):
		if value:
			PressKey(key)
		else:
			ReleaseKey(key)

	keyboard_keys[key] = value
	
previous_values = microbit.accelerometer.get_values()
keyboard_keys = {}

stable = Image("00000:"
              "00900:"
              "09990:"
              "00900:"
              "00000:")
init_img = Image("90009:"
              "09990:"
              "09990:"
              "09990:"
              "90009:")
image_N = Image("00900:"
              "09990:"
              "99999:"
              "00000:"
              "00000:")
image_NE = Image("00999:"
              "00099:"
              "00009:"
              "00000:"
              "00000:")
image_NW = Image("99900:"
              "99000:"
              "90000:"
              "00000:"
              "00000:")
image_SE = Image("00000:"
              "00000:"
              "00009:"
              "00099:"
              "00999:")
image_SW = Image("00000:"
              "00000:"
              "90000:"
              "99000:"
              "99900:")
image_E = Image("00990:"
              "00090:"
              "00009:"
              "00090:"
              "00990:")
image_W = Image("09900:"
              "09000:"
              "90000:"
              "09000:"
              "09900:")
image_S = Image("00000:"
              "00000:"
              "99999:"
              "09990:"
              "00900:")
images = {"N": image_N,
          "NE": image_NE,
          "NW": image_NW,
          "SE": image_SE,
          "SW": image_SW,
          "E":image_E,
          "W": image_W,
          "S": image_S,
          "": stable}

#Wait for User to Press a Button
while 1:
	#Blink
	microbit.display.show(init_img)
	time.sleep(0.5)
	microbit.display.clear()

	#Start the Program if a Button is Pressed
	if microbit.button_a.was_pressed() or microbit.button_b.was_pressed():
		break
	time.sleep(0.5)

#Start the Loop
while 1:
    #Get Accelerometer Values
    accelerometer_values = microbit.accelerometer.get_values()
    x,y,z = accelerometer_values
    
    #Calculate Avarege Motion in X,Y,Z Directions
    motion = sum(map(lambda x:abs(accelerometer_values[x]-previous_values[x]),range(3)))/3
    print("Motion: ",motion,accelerometer_values)
    #Change Direction
    update_press(W, y<-400)
    update_press(S, y>400)
    update_press(D, x>60)
    update_press(A, x<-60)
    direction = ""
    if y<-400:
        direction += "N"
    elif y>400:
        direction += "S"
    if x>60:
        direction += "E"
    elif x<-60:
        direction += "W"
    microbit.display.show(images[direction])
    previous_values = accelerometer_values
