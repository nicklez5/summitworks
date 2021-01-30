class Room:
    def __init__(self,room_number, bedtype, smoking_type, price):
        self.__room_number = room_number
        self.__bedtype = bedtype
        self.__smoking_type = smoking_type 
        self.__price = price
        self.__occupantName = "Not Occupied"
        self.__occupied = False
    
    def getBedType(self):
        return self.__bedtype

    def getSmoking(self):
        return self.__smoking_type

    def getRoomNum(self):
        return self.__room_number

    def getRoomRate(self):
        return self.__price

    def getOccupant(self):
        return self.__occupantName

    def setOccupied(self,occupied):
        self.__occupied = occupied

    def setOccupant(self, name):
        self.__occupantName = name

    def setRoomNum(self, room_num):
        self.__room_number = room_num

    def setBedType(self, bed_type):
        self.__bedtype = bed_type

    def setRate(self, bed_rate):
        self.__price = bed_rate

    def setSmoking(self, smoking_char):
        self.__smoking_type = smoking_char

    def isOccupied(self):
        if(self.__occupied == True):
            return True
        else:
            return False
    
    def __str__(self):
        return "Room Number: {}\nOccupant name: {}\nSmoking room: {}\nBed Type: {}\nRate : {}\n\n".format(self.__room_number,self.__occupantName,self.__smoking_type, self.__bedtype , self.__price)          
