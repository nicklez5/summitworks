from num1 import *

person_list = []
a = Person("Jill","310 new ave", "332-330-3321", "craigmyers@ucr.edu")
b = Person("Rose","237 massachusetts ave", "133-442-3994", "rose@yahoo.com")
person_list.append(a)
person_list.append(b)
student_list = []

c = Student("Ruby Rose", "237 compton st", "943-332-2321", "rubyrose@entertainment.edu", "3")
d = Student("Amy Truong", "341 n. 2nd st.", "188-033-3210", "amytruong@uci.edu","2")
e = Student("Kali Muscle", "209 w. valencia st.", "941-321-6656", "kalimuscle@bodybuilding.edu", "4")
student_list.append(c)
student_list.append(d)
student_list.append(e)

f = Faculty("Thomas Hill", "942 s. hoover st", "442-300-7904", "jesuschrist@aol.com", "South", "$45,000", "9/10/21", "9am-4pm", "Assistant TA")
g = Faculty("Alex Ken", "321 n. graveyard st", "788-323-3093", "alexken@aol.com" , "North", "$90,000", "1/23/19", "10am-2pm", "Professor")
faculty_list = []
faculty_list.append(f)
faculty_list.append(g)

staff_list = []
h = Staff("Jenny Hamstring", "301 commonwealth ave", "999-444-3333", "jenny@ucr.edu", "west", "$90,000", "06/15/19", "chem ta")
k = Staff("Kevin Ortega", "943 westminister ave", "909-323-0041", "kevin_ortega@ucla.edu", "south", "$146,000", "4/21/19", "textbook guy")
staff_list.append(h)
staff_list.append(k)

employee_list = []
l = Employee("Abraham Park" , "909 megan street", "1-800-idonthavenumbers", "abrahampark@cc.edu", "west innercircle" , "$90,000" , "8/13/20")
m = Employee("Jessica Park", "910 megan street", "1-800-idonthavenumbers2", "jessicapark@cc.edu", "north innercircle", "$450,000", "9/02/19")
n = Employee("Zavier Henry", "323 august st.", "930-332-3310", "zavierhenry@ucr.edu", "south innercircle", "$330,000", "6/14/18")
o = Employee("Kevin Franklin", "231 2nd st.", "1-800-332franklin", "kevinfranklin@ucr.edu", "west innercircle", "$500,000", "2/19/21")
p = Employee("Jesus Henry", "324 august st.", "433-231-0001" , "jesushenry@ucr.edu", "south innercircle" , "$300,000", "6/16/19")
employee_list.append(l)
employee_list.append(m)
employee_list.append(n)
employee_list.append(o)
employee_list.append(p)
print("")
class iter_n(object):
    def __init__(self,n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        if(self.num < len(self.n)):
            i = self.n[self.num]
            self.num += 1
            return i
        else:
            raise StopIteration()
        

data = {'Person' : person_list , 'Student' : student_list, 'Faculty' : faculty_list, 'Staff' : staff_list, 'Employee' : employee_list}
def loop_through_all(data):
    for k in data:
        xyz = iter_n(data[k])
        for i in xyz:
            print(repr(i))

loop_through_all(data)
