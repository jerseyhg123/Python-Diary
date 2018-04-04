#.__author__.=,"JerseyHg"

Username_list = ['Jersey', 'Zoe', 'Peter', 'Angela']
Password_list = ['123', '5486', 'ssw5e4', 'sie32n32se24']

p = 0
n = 0
while p <= 2:
    Username = input("Username:")
    Password = input("Password:")
    while n <= 3:
        if Username == Username_list[n] and Password == Password_list[n]:   #比较用户名和密码是否相等，如果相等打出Welcome，否则将n+1且小于等于4的时候，重新进入到循环当中；
            print('Welcome!')
        else:
            n += 1
            continue
    else:
        print("WRONG!")
        p += 1
    break

