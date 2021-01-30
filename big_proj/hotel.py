import re
from room import *
class Hotel:
    def __init__(self,hotel_name,hotel_location):
        if(hotel_name != ""):
            self.__hotel_name = hotel_name
        else:
            raise Exception("Sorry, hotel name must not be empty")
        if(hotel_location != ""):
            self.__hotel_location = hotel_location
        else:
            raise Exception("Sorry, hotel location must not be empty")
        self.__numOfRooms = 0
        self.occupiedCnt = 0
        self.__listRooms = []

    def isFull(self):
        if(self.occupiedCnt >= self.__numOfRooms):
            return True
        return False

    def isEmpty(self):
        if(self.occupiedCnt == 0):
            return True
        return False

    def addRoom(self, roomnumber, bedtype , smoking, price):
        if(not isinstance(roomnumber,int)):
            raise Exception("Room number must be a integer")
        if(bedtype != "king" or bedtype != "queen" or bedtype != "twin"):
            raise Exception("Bed type must be a king,queen or twin")
        if(smoking != "S" or smoking != "s" or smoking != "n" or smoking != "N"):
            raise Exception("Hotel type must be s|S|n|N")
        if(re.search(r"^[$][0-9]+",price) == None):
            raise Exception("Price must be $100 format")
        xyz = Room(roomnumber,bedtype,smoking,price)
        self.__listRooms.append(xyz)
        self.__numOfRooms += 1

    def addReservation(self,occupantName, smoking, bedtype):
        success = 0
        if(re.search
        for i in self.__listRooms:
            if((i.isOccupied() == False) and (i.getBedType() == bedtype) and (i.getSmoking() == smoking)):
                i.setOccupant(occupantName)
                i.setOccupied(True)
                self.occupiedCnt += 1
                print("Reservation was made for: ", occupantName)
                success = 1

        if(success == 0):
            print("Reservation was not completed for: ", occupantName)


    def cancelReservation(self,occupantName):
        index = self.findReservation(occupantName)
        if(index == -1):
            print("Reservation is was not successfully canceled")
        else:
            self.occupiedCnt -= 1
            self.__listRooms[index].setOccupied(False)
            print("Reservation is canceled for ", occupantName)

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
            print("Bed Type: ", i.getBedType())
            print("Occupant name: ",i.getOccupant())
            print("Smoking room: ",i.getSmoking())
            print("Rate: ", i.getRoomRate())
            print("\n")

    def getDailySales(self):
        total_sale = 0
        for i in self.__listRooms:
            if(i.isOccupied() == True):
                temp_price = i.getRoomRate()
                xyz = temp_price.replace('$','')
                xyz = int(xyz)
                total_sale += xyz

        return total_sale
    def getName(self):
        return self.
    def occupanyPercentage(self):
        return (self.occupiedCnt/self.__numOfRooms)*100

    def __str__(self):
        xyz = ""
        for i in self.__listRooms:
            xyz += i.__str__()
        return "Hotel Name : {}\nNumber of Rooms : {}\nNumber of Occupied Rooms: : {}\n\n\nRoom Details are:\n\n\n{}".format(self.__hotel_name, self.__numOfRooms, self.occupiedCnt, xyz)

temp_hotel = Hotel("Hilton Hotel","356 pasadena ave")
temp_hotel.addRoom(101,"queen","s","$100")
temp_hotel.addRoom(102,"king","n","$110")
temp_hotel.addRoom(103,"king","s","$88")
temp_hotel.addRoom(104,"twin","s","$100")
temp_hotel.addRoom(105,"queen","n","$99")
#temp_hotel.printReservationList()
#print("is the hotel empty: ", temp_hotel.isEmpty())
#print("is the hotel full: ", temp_hotel.isFull())
temp_hotel.addReservation("Jackson Lu", "s" , "queen")
temp_hotel.printReservationList()
temp_hotel.addReservation("Janet Jackson","n","king")
temp_hotel.printReservationList()
temp_hotel.addReservation("Jamie Fox","s","king")
temp_hotel.addReservation("Pop smoke","s","twin")
temp_hotel.addReservation("Ashley Tisdale","n","queen")
print("Daily Sales:$",str(temp_hotel.getDailySales()))
print("Occupancy Percentage:%",temp_hotel.occupanyPercentage())
print("\n")
print(temp_hotel)
print("Is the hotel full?", temp_hotel.isFull())
print("Is the hotel empty?", temp_hotel.isEmpty())

