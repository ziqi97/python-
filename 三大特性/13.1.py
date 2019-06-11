class Course:
    def __init__(self,course_name,course_price):
        self.course_name = course_name
        self.course_price = course_price
    def show_class(self):
        print(self.course_name)
        print(self.course_price)
        
class DeepsharePeople:
    school = 'deepshare'
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        

class DeepshareTeacher(DeepsharePeople):
    def __init__(self,name,age,gender,level,salary):
        super().__init__(name,age,gender)  # 这里调用的是父类的init，super()是一个对象
        self.level = level
        self.salary = salary
        

class DeepshareStudent(DeepsharePeople):
    def __init__(self,name,age,gender,level):
        super().__init__(name,age,gender)  # 这里调用的是父类的init，super()是一个对象
        self.level = level
        


tea1 = DeepshareTeacher('albert', 18, 'male','10 ','3.1')
tea1.course = Course('math',12)
tea1.course.show_class()

stu1 = DeepshareStudent('ziqi',15,'female',two)
stu1.course = Course('cs',360)
stu1.course.show_class()