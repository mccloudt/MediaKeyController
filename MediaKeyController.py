from inputs import get_gamepad
import win32api
from win32con import VK_MEDIA_PLAY_PAUSE, KEYEVENTF_EXTENDEDKEY, VK_MEDIA_NEXT_TRACK, VK_MEDIA_PREV_TRACK, VK_MEDIA_PLAY_PAUSE

#Blacklist array appending which will miss inputs
blacklist = ['ABS_Y', 'ABS_X', 'ABS_RY', 'SYN_REPORT', 'ABS_RX', 'ABS_RZ', 'ABS_Z']
lastTwo = []

while 1:
    events = get_gamepad()
    for event in events:
        #If the array somehow retains it's value, clear it
        if len(lastTwo) == 2:
            lastTwo.clear()
            #if the event isn't in the blacklist and the state is '1' i.e. down 
        if event.code not in blacklist and event.state == 1:
            #execute corresponding commnands on matching inputs
            lastTwo.append(event.code)
            if 'BTN_THUMBL' in lastTwo and 'BTN_THUMBR' in lastTwo:
                #next track
                win32api.keybd_event(VK_MEDIA_NEXT_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                lastTwo.clear()
            if 'BTN_TR' in lastTwo and 'BTN_TL' in lastTwo:
                #previous track
                win32api.keybd_event(VK_MEDIA_PREV_TRACK, 0, KEYEVENTF_EXTENDEDKEY, 0)
                lastTwo.clear()
            if 'BTN_WEST' in lastTwo:
                #play/pause
                win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENDEDKEY, 0)
                lastTwo.clear()
    
