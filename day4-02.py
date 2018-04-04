#.__author__.=,"JerseyHg"

name = input("name")   #给变量赋值必须用等于号= 不能用冒号否则会NOT defined
job = input("job")
age = input("age")

info = """
----info of %s----
name = %s
age = %s
job = %s
"""%(name, name, age, job)
print(info)