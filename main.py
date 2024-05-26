from Libs.Cryptology import SezarX
import json
import os

class Program:
    def __init__(self) -> None:
        self.crypter = SezarX(key=20)
        self.config = json.loads(self.readFile("./.locker/config.json","r"))
        self.currentPath = os.path.abspath(__file__)
        self.inputStarter = ">"
        pass
    
    def printMenu(self):
        self.clearTerminal()

        print("1-Encrypt (Lock) ")
        print("2-Descrypt (UnLock)")
        print("")

        userInput = self.getUserInput()
        self.executeMenu(userInput)

        pass

    def run(self):
        self.printMenu()
        
        pass

    def executeMenu(self,choice):
        if(choice == 1):
            self.encryptFolder()
            pass
        elif(choice == 2):
            self.decryptFolder()
            pass
        pass

    def encryptFolder(self):
        
        pass
    def decryptFolder(self):
        pass
    def getUserInput(self):
        userInput = input(self.inputStarter)
        return userInput
    
    def clearTerminal(self):
        if(self.config["Platform"]=="Mac" or self.config["Platform"]=="Linux"):
            os.system("clear")
            pass
        elif(self.config["Platform"] == "Windows"):
            os.system("cls")
            pass
        pass

    def readFile(self,path,type):
        with open(path,type) as f:
            return f.read()


app = Program()

app.run()