def hello():
    print('Hello baby!!!')
    print('Hello momy!!!')
    print('Hello darly!!!')
    print('******************')

def hello2(name):
    print("Hello "+ name)

def hello3(name, age):
    print('Hello {} you are {} years old.'.format(name, age))

def hello4(name="Safa", age=39):
    print("Hello {} you are {} years old.".format(name, age))

def hello5(name, age):
    return "Hello {} you are {} years old.".format(name, age)

hello()
hello2('Safa')
hello3('Safa', 39)
hello4()

sentence = hello5('Safa', 42)
print(sentence)
