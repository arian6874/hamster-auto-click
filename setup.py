
import pyautogui
from icecream import ic
from datetime import datetime
#1395 558
class Hamster:
    def __init__(self,energy=6500,earn_by_taps=11):
        self.ENERGY = energy
        self.EARN_BY_TAPS = earn_by_taps
        self.count=0
    def taps(self):
        for i in range(int(self.ENERGY/self.EARN_BY_TAPS)+35):
            pyautogui.sleep(0.02)
            pyautogui.click()
    def run(self):
        pyautogui.moveTo(213,567)
        while True:
            ic('Tapping . . .')
            self.taps()
            ic(f"Waiting for {int((self.ENERGY/4)+5)/60} minute.")
            pyautogui.sleep(int(self.ENERGY/500)*165+20)
            self.count+=1
            ic("Starting to Tap again")
            print(f"Count: {self.count}")

class TapSwap:
    def __init__(self,energy=7500,earn_by_taps=13):
        self.ENERGY = energy
        self.EARN_BY_TAPS = earn_by_taps
        self.count=0
    def taps(self):
        for i in range(int(self.ENERGY/self.EARN_BY_TAPS)+160):
            # pyautogui.sleep(0.02)
            pyautogui.click()
    def run(self):
        pyautogui.moveTo(276,446)
        while True:
            ic('Tapping . . .')
            self.taps()
            ic(f"Waiting for {int((self.ENERGY/5)+5)/60} minute.")
            pyautogui.sleep(int(self.ENERGY/4)+5)
            ic("Starting to Tap again")
            self.count +=1
            print(f"Count: {self.count}")


if __name__ == '__main__':
    def time_format(): 
        now = datetime.now() 
        return f'{now.strftime("%H:%M:%S")} --> '
    ic.configureOutput(prefix=time_format) 
    pyautogui.FAILSAFE = True
    choice = pyautogui.confirm('Choose!!', buttons =['TapSwap', 'HamesterCombat']) 

    print(choice)
    if choice == 'HamesterCombat':
        pyautogui.countdown(5)
        ic('starting the Hamster . . .')
        hamster = Hamster()
        ic("Running the hamster . . .")
        hamster.run()
    elif choice == 'TapSwap':
        pyautogui.countdown(5)
        tap_swap = TapSwap()
        tap_swap.run()

    elif choice == None:
        quit()