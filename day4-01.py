
name = input('name')
age = input('age')#这里输入的age是数字还是字符串？——字符串
job = input('job')
hometown = input('hometown')

info= """
-------info of %s-------
Name: %s
Age:  %s #当改为%d的时候，上面的input用int()包起来 井号在解释语句内也同样会被翻译成字符串
Job:  %s
Hometown:  %s
-------end-------
""" % (name, name, age, 22, job, hometown)

print(info)