from pyautogui import *
from time import sleep


# function to find the search bar location
def click_search_name(name):
    sleep(5)
    x1, y1 = [149,363]
    moveTo(x1, y1)
    click()
    typewrite(name, interval=0.2)
    sleep(2)
    press('enter')

# function to find and send message
def click_send_message(message): 
    x3, y3 = [746,967] 
    moveTo(x3, y3) 
    click() 
    sleep(2)
    for x in range(10):
        typewrite('You have ' + message) 
        press('enter')


if __name__ == '__main__':
    name = "Maxim"
    message = 'new message'
    #iterating through the contact list
    try:
        click_search_name(name)
    except:
        print("Unable to locate search bar or name")
    try:
        click_send_message(message)
    except:
        print("Unable to locate message bar")
