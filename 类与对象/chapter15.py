'''
1.根据姓名查看学生所有成绩
2.查看所有人的某学科成绩
3.查看总平均分
4.查看某人的某学科成绩
5.根据姓名删除学生信息
'''
class student:
    school = 'SYSU'
    def __init__(self,name,Math,Chinese,English):
        self.name = name
        self.Math = Math
        self.Chinese = Chinese
        self.English = English
 
    def show_name(self):
        return self.name
 
    def show_math(self):
        return self.Math
 
    def show_Chinese(self):
        return self.Chinese
 
    def show_English(self):
        return self.English
 
    def print_all_score(self):
        print('%s的数学成绩：%3d,语文成绩：%3d,英语成绩：%3d'%(self.name,
                                      self.Math,
                                      self.Chinese,self.English))
 
    def print_one_score(self,subject):
        if subject == 'Math':
            print ('%s的数学成绩：%3d'%(self.name,
                                  self.Math))
        elif subject == 'Chinese':
            print('%s的语文成绩：%3d'%(self.name,
                                 self.Chinese))
        elif subject == 'English':
            print('%s的英语成绩：%3d'%(self.name,
                                 self.English))
        
 
 
stu1 = student('张三',85,100,90)
stu2 = student('李四',76,90,100)
stu = {stu1, stu2}
print (type(stu))
 
#查看所有成绩
for astu in stu:
    astu.print_all_score()
print ('='*20)
 
# 查看所有人的某学科成绩
for astu in stu:
    astu.print_one_score('Chinese')
print ('='*20)
# .查看总平均分
total = 0
num = 0
for astu in stu:
    total += astu.show_math()
    total += astu.show_Chinese()
    total += astu.show_English()
    num += 2
print('总平均分',total/num)
print ('='*20)
#4.查看某人的某学科成绩
name = '张三'
xueke = 'ShuXue'
for astu in stu:
    if name == astu.show_name():
        astu.print_one_score(xueke)