import pyautogui
import webbrowser
import  time 

print( "Made by Jampa_was_here on TikTok")

message = input("What Message do you wanna spam?")
repeat = int(input("How many messages do you wanna get send?"))
delay = int(input(" How many seconds between each message? "))

isloaded = input ("press enter if ur discord is loaded")
print(" u got 5 seconds til the spammer starts")

time.sleep(5)

for i in range(0, repeats):
   if message != "":
      pyautogui.typewrite(message)
      pyautogui.press("enter")
   else 
      pyautogui.hotkey('ctr', 'v'')
      pyautogui.press("enter")
   time.sleep(delay/1000)  
    
    
print("Done\n")    
