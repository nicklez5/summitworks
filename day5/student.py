import re
class Person:
    def __init__(self,name,addr,num,email):
        if(name != ""):
            self.name = str(name)
        else:
            raise Exception("Sorry, name must be not empty")
        if(addr != ""):
            self.addr = str(addr)
        else:
            raise Exception("Sorry, addr must not be empty")
        x = re.search(r"^\d{10}",num)
        y = re.search(r"^[()]*\d{3}.\d{3}-\d{4}",num)
        z = re.search(r"^\d{3}-\d{3}-\d{4}",num)
        if( x != None or y != None or z != None):
            self.num = num
        else:
            raise Exception("Sorry format must either be 3234445555 or (323)444-5555 or 323-444-5555")
    
        match2 = re.search(r"^[\w]+@{1}[\w]+.{1}[\w]+", email)
        if match2:
            self.email = email
        else:
            raise Exception("Sorry format must be either abcdefg@yahoo.com")

    def __repr__(self):
        return 'Person(' + str(self.name) + ',' + str(self.addr) + ',' + str(self.num) + ',' + str(self.email) + ')'

class Student(Person):
    def __init__(self,name,addr,num,email,status):
        super().__init__(name,addr,num,email)
        self.status = status

    def __repr__(self):
        token = ""
        if(self.status == '1'):
            token = "Freshmen"
        elif(self.status == '2'):
            token = "Sophomore"
        elif(self.status == '3'):
            token = "Junior"
        elif(self.status == '4'):
            token = "Senior"
        return 'Student(' + self.name + ',' + self.addr + ',' + self.num + ',' + self.email + ',' + token + ')'

class Employee(Person):
    def __init__(self,name,addr,num,email,office,salary,date_hired):
        super().__init__(name,addr,num,email)
        self.office = office
        self.salary = salary
        self.date_hired = date_hired

    def __repr__(self):
        return 'Employee(' + str(self.name) + ',' + self.addr + ',' + self.num + ',' +  str(self.office) + ',' + str(self.salary) + ',' + str(self.date_hired) + ')'

class Faculty(Employee):
    def __init__(self,name,addr,num,email,office,salary,date_hired,office_hours,rank):
        super().__init__(name,addr,num,email,office,salary,date_hired)
        self.office_hours = office_hours
        self.rank = rank

    def __repr__(self):
        return 'Faculty(' + str(self.name) + ',' + self.addr + ',' + self.num + ',' + self.email + ',' + self.office + ',' + self.salary + ',' + self.date_hired + ','  + str(self.office_hours) + ',' + str(self.rank) + ')' 

class Staff(Employee):
    def __init__(self,name,addr,num,email,office,salary,date_hired,title):
        super().__init__(name,addr,num,email,office,salary,date_hired)
        self.title = title

    def __repr__(self):
        return 'Staff(' + str(self.name) + ',' + self.addr + ',' + self.num + ',' + self.email + ',' + self.office + ',' + self.salary + ',' + self.date_hired + ',' +  str(self.title) + ')'

def create_Person(name,addr,phone,email):
    temp_person = Person(name,addr,phone,email)
    print(repr(temp_person))

def create_Student(name,addr,phone,email,status):
    temp_student = Student(name,addr,phone,email,status)
    print(repr(temp_student))

def create_Employee(name,addr,phone,email,office,salary,date_hired):
    temp_employee = Employee(name,addr,phone,email,office,salary,date_hired)
    print(repr(temp_employee))

def create_Faculty(name,addr,phone,email,office,salary,date_hired,office_hours,rank):
    temp_faculty = Faculty(name,addr,phone,email,office,salary,date_hired,office_hours,rank)
    print(repr(temp_faculty))

def create_Staff(name,addr,phone,email,office,salary,date_hired,title):
    temp_staff = Staff(name,addr,phone,email,office,salary,date_hired,title)
    print(repr(temp_staff))

def create_all():
    person = create_Person("Jackson","143 chapo ave.", "434-443-0921", "jlu080@ucr.edu")
    student = create_Student("David Zobrik", "921 el molino ave" , "933-332-2121" , "davidzobrik@yahoo.com","4")
    employee = create_Employee("Mr.Stark", "231 n. new ave", "123-345-3431" , "stark@hoodsite.com", "hoodsite" , "$850,000" , "6/23/18")
    faculty = create_Faculty("Aaron", "312 commonwealth", "432-999-0901", "lospolos@yahoo.com" , "Microsoft", "$90,000", "9/19/20" , "9am-5pm" , "gardener")
    staff = create_Staff("Megan Fox", "hollywood hills", "009-332-2231", "meganfox@yahoo.com" , "internet" , "$3.2mil", "9/16/12", "actor")

#create_all()
