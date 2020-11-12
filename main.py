import pyautogui, time, os, datetime

meeting_id = input('Please enter your meeting ID : ')
password = input('Please enter meeting password : ')
meeting_date = str(input('Enter the date of meeting : (DD:MM:YYYY) '))
meeting_date = meeting_date.split(':')
meeting_time = str(input('Enter meeting time : (24 hour format) '))
meeting_time = meeting_time.split(':')
meeting_length = int(input('Enter meeting length (in minutes) : '))
meeting_hour = meeting_time[0]
if meeting_hour[0] == "0":
    meeting_hour = meeting_hour[1]
meeting_min = meeting_time[1]
if meeting_min[0] == "0":
    meeting_min = meeting_min[1]
meeting_time_full = datetime.datetime(int(meeting_date[2]), int(meeting_date[1]), int(meeting_date[0]), int(meeting_hour), int(meeting_min))  
now = datetime.datetime.now()
diff = meeting_time_full - now
until_meeting = diff.total_seconds()
def attender():
    time.sleep(1)
    pyautogui.press('esc', interval=0.1) # escape current window
    time.sleep(0.5)
    pyautogui.press('win', interval=0.5) # open windows menu
    pyautogui.write('zoom') # type zoom in search bar
    pyautogui.press('enter') 

    time.sleep(5) # give time for zoom to open
    mouse_x, mouse_y = pyautogui.locateCenterOnScreen('joinbutton.png')
    print(mouse_x, mouse_y)
    pyautogui.click(mouse_x, mouse_y) # click join button
    pyautogui.press('enter', interval=5) # move to the input box
    pyautogui.write(meeting_id) 
    pyautogui.press('enter',interval=5)
    pyautogui.write(password)
    pyautogui.press('enter',interval = 10)
    pyautogui.press('enter') # join with computer audio
    time.sleep(5)
    pyautogui.hotkey('alt', 'a') # mute mic  
    print('Meeting joined ! ')
    time.sleep(meeting_length*60)
    os.system('TASKKILL /F /IM Zoom.exe')
    print('Meeting is over')


for i in range(int(until_meeting), 0, -1):
    print(f"Joining meeting in {i} seconds", "\r", end="")

attender()
