import math, pyautogui, time

msg = input("Enter the message: ")
n = input("How many times?: ")
ent = input("How many enter?: ")
count = 0

time.sleep(5)
try:
  print("Fire in the hole!!!")
  for i in range(0,int(n)):
    pyautogui.typewrite(msg)
    for i in range(0, int(ent or 1)):
      pyautogui.press('enter')
    count+=1
    
    perc=math.floor(int(count)/int(n)*100)
    prst = "▌"*math.floor(perc/10) + "          "
    pr = prst[0:10]
    c = 50*(math.floor(int(count)/50))
    print(f"({c}/{n}) [{pr}] {perc}%", end="\r")
  
except KeyboardInterrupt:
  print("Operation Interrupted!")
  exit()