import base64

class SezarX:
    #Data Should Be Short Like "2000" character

    def __init__(self,key) -> None:
        self.key = key
        pass

    def encrypt(self,data):
        dataIDs = []
        encryptedData = ""
        

        for i in data:
            dataIDs.append(ord(i))
            pass

        for index,item in enumerate(dataIDs):
            encryptedData += chr(item + self.key)
            pass

        return encryptedData

    def decrypt(self,data):
        dataIDs = []
        decryptedData = ""

        for index,item in enumerate(data):
            id = ord(item)
            dataIDs.append(id - self.key)
            
            pass

        for i in dataIDs:
            decryptedData += chr(i)

        return decryptedData
        pass

    def encryptImage(self,data):
        byteFormat = base64.b64encode(data)
        return self.encrypt(byteFormat.decode())
        pass

    def decryptImage(self,data):
        decryptedData = self.decrypt(data)
        decryptedData = base64.b64decode(decryptedData)
        return decryptedData
            
        pass

