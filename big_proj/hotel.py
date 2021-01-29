class Hotel:
    def __init__(self,hotel_name,hotel_location):
        self.__hotel_name = hotel_name
        self.__hotel_location = hotel_location
        self.__numOfRooms = 0
        self.occupiedCnt = 0
        self.__listRooms = [Room() for i in range(10)]

    def isFull(self):
        if(self.occupiedCnt >= self.__numOfRooms):
            return True
        return False

    def isEmpty(self):
        if(self.occupiedCnt == 0):
            return True
        return False

    def addRoom(self, roomnumber, bedtype , smoking, price):
        xyz = Room(roomnumber,bedtype,price,smoking)
        self.__listRooms.append(xyz)
        self.__numOfRooms += 1

    def addReservation(self,occupantName, smoking, bedtype):
        success = 0
        for i in self.__listRooms:
            if((i.occupied == False) and (i.getBedType == bedtype) and (i.getSmoking == smoking)):
                i.setOccupant(occupantName)
                i.setOccupied(True)
                print("Reservation was made for: ", occupantName)
                success = 1

        if(success == 0):
            print("Reservation was not completed for: ", occupantName)


    def cancelReservation(self,occupantName):
        index_attendant = self.cancelReservation(occupantName)
        if(index == -1):
            print("Reservation is was not successfully canceled")
        else:
            self.__listRooms[index_attendant].setOccupied(False)
            print("Reservation is canceled")

    def findReservation(self,occupantName):
        index = 0
        for i in self.__listRooms:
            if(i.getOccupant() == occupantName):
                return index
            index += 1
        
        return -1

    def printReservationList(self):
        for i in self.__listRooms:
            print("Room Number: ",i.getRoomNum())
            print("Occupant name: ",i.getOccupant())
            print("Smoking room: ",i.getSmoking())
            print("Bed Type: ", i.getBedType())
            print("Rate: ", i.getRoomRate())

    def getDailySales(self):
        total_sale = 0
        for i in self.__listRooms:
            if(i.isOccupied() == True):
                total_sale += i.getRoomRate()

        return total_sale
    
    def occupanyPercentage(self):
        return self.occupiedCnt/self.__numOfRooms

    def __str__(self):
        return "Hotel Name : {}\nNumber of Rooms : {}\nNumber of Occupied Rooms: : {}\n\n\nRoom Details are:\n\n\n{}".format(self.__hotel_name, self.__numOfRooms, self.occupiedCnt, print[str(x) for x in self.__listRooms])
    
