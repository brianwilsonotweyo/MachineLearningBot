import pyautogui as pt
import pyperclip as pc

from pynput.mouse import Controller, Button
from time import sleep 
from responses import response

mouse = Controller()


class WhatsApp:
    def __init__(self,speed=0.5, click_speed=0.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ""
        self.lastMessage = ""
    def nav_greendot(self):
        try:
            position = pt.locateOnScreen('message.PNG', confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(-100,0, duration = self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Exception @ Message dot", e)
    # Navigating to the Input Box.
    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('pin.PNG', confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(100,10, duration = self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print("Exception @ Input dot", e)
    # Navigates to the message, that we would like to respond to.
    def nav_message(self):
        try:
            position = pt.locateOnScreen('pin.PNG', confidence=0.7)
            pt.moveTo(position[0:2],duration=self.speed)
            pt.moveRel(60,-85, duration = self.speed)
        except Exception as e:
            print("Exception @ Message", e)

    # Function that gets the message and copies it.
    def getMessage(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right,1)
        sleep(self.speed)
        pt.moveRel(60,-300, duration=self.speed)
        mouse.click(Button.left, 1)
        sleep(1)

        self.message = pc.paste()
        print("User says: ", self.message)

    # Sending a message to the user
    def send_Message(self):
        try:
            # Check whether the last message is the same as the one youve just sent preventing sending the same message.
            # to the same question.

            if self.message != self.last_message:
                bot_response = response(self.message)
                print("You say:", bot_response)
                pt.typewrite(bot_response, interval=0.1)
                pt.typewrite("\n")

                # Assign them to same message
                self.last_message =self.message

            else:
                print("no new messages")
        except Exception as e:
            print("Exception @ send Message", e)




WhatsAppBot = WhatsApp(speed = 0.5, click_speed =0.4)
sleep(10)
# WhatsAppBot.nav_greendot()
WhatsAppBot.nav_message()
WhatsAppBot.getMessage()
WhatsAppBot.nav_input_box()
WhatsAppBot.send_Message()