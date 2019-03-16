import keyboard 
import time
alpha="a b c d e f g h i j k l m n o p q r s t u v w x y z"
l=alpha.split(" ")
while True:
    for i in l:
        try:
            if keyboard.is_pressed(i):
                print(i.upper(),end="")
                time.sleep(0.5)
                break  
            else:
                pass
        except:
            break 