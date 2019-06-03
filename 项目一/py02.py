#### lock.txt 用来存储连续三次输错了密码的用户####
#### a.txt 用来存储用户信息
count = 0 #有连续输错三次密码的机会
info = []
old_user = False
login = False
money = 0 #最后用户可以使用来购物的钱
shopping_mail = [
  ('Iphone',5800),
  ('Mac Pro',9800),
  ('Bike',800),
  ('Watch',10600),
  ('Coffee',31),
  ('Alex Python',120),
]


#############用户登陆注册模块###########

user_name = input('\n用户名：')
#该用户名已进入黑名单
with open('lock.txt','r') as lock_file:
    for lock_name in lock_file:
        if user_name == lock_name.strip():
            exit('\n用户名%s已被加入黑名单'%user_name)
user_file = open('a.txt','r')
for user_info in user_file:
    info = [user,passwd,balance] = user_info.strip('\n').split('|')
    money = balance
    if user_name == user:
        old_user = True
        while count<3:
            password = input('密码： ')
            if passwd == password:
                print('\n欢迎 %s 登录商城，祝您购物愉快！\n' % user)
                login = True  # 登录标志赋值为True
                break
            else:
                if count != 2: 
                    print('\n密码错误，请重新输入，您还有 %d 次机会\n' % (2-count))
                    count = count+1
                else :
                    open('lock.txt', 'w').write(user_name + '\n')
                    exit('\n错误次数过多，账户已被锁定...') 
        if login :break
user_file.close()


###如果是未注册用户，则写入文件进行注册
if old_user == False:
    new_passwd = input("你是新用户，请输入你的登陆密码：")
    last_passwd = input("请再次输入你的登陆密码：")
    while True:
        if new_passwd ==last_passwd:
            print("注册成功")
            balance = input("请输入你的薪水：")
            money = balance
            temp = open('a.txt','a')
            temp.write('\n'+user_name+'|'+new_passwd+'|'+balance+'\n')
            temp.close()
            break
        else :
            last_passwd = input("与第一次输入密码不符，请再次输入密码")

######物品购买模块######
print ("%s,您好！现在可以开始购物！\n"%user_name)
while True:
    for index,item in enumerate(shopping_mail):
        print(index,item)
    enter_number=input("请输入您要购买的商品编号：")
    if enter_number.isdigit():
        enter_number=int(enter_number)
        if enter_number>-1 and enter_number<len(shopping_mail):
            p_item=shopping_mail[enter_number]
            if int(p_item[1])<=int(money):
                money = int(money) - p_item[1]
                print("您选购的商品金额是：\033[31m%s\033[0m，您的工资余额为：\033[31m%s\033[0m" % (p_item, money))
                # 将修改写回文件 
                lines = open('a.txt', 'r').readlines()
                # 修改用户余额
                for line in lines: 
                    if user_name in line.split('|'):  # 定位到用户名所在行
                        j = lines.index(line)   # 获取用户名所在行的行号索引
                        select = line.split('|')  # 分割用户名所在行赋值给列表select
                        select[-1] = str(money) # 修改用户余额
                        lines[j] = '|'.join(select)+'\n' # 修改后的列表拼接成字符串，覆盖用户名所在行
                        open('a.txt', 'w').writelines(lines) # 将修改写回文件
                break
            else:
                print("您的余额不足，无法继续购买！")
                break
        else:
            print("您输入的商品编号不存在：")

    elif enter_number=="q":
        print("您的余额为：\033[31m%s\033[0m"%(money))
        break

