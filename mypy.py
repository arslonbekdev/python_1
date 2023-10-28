def summa(*numbers):
    """A function that returns calculated the sum of the input number"""
    total_number =0
    for number in numbers:
        total_number +=number
    return total_number

print(summa(11,132))


def summa(*good_heards):
    """A function that returns calculated the sum of the input number"""
    total =0
    for good_heard in good_heards:
        total +=good_heard
    return total

print(summa(1,12,13))

def summa(*love_birds):
    """A function that returns calculated the sum of the input number"""
    limitless =1
    for love_bird in love_birds:
        limitless +=love_bird
    return limitless
print(summa(1,12,13,14))

def summa(*goats):
    """A function that reveals calculated the sum of the input number"""
    limits =10
    for a in goats:
        limits+=a
    return a
print(summa(9,9,9,9))


def summa(*mice):
    """A function that reveals calculated the sum of the input number"""
    bag = 0
    for mouse in mice :
        bag +=mouse
    return bag
print(summa(9,9,8,7))


def summa(*geese):
    """A function that calculates the sum of the input numbers"""
    sack = 0
    for goose in geese:
        sack+=goose
    return sack
print(summa(800,100,200,250))

def summa(*men):
    """A function that calculates the sum of the input numbers"""
    cap =0
    for man in men:
        cap+=man
    return cap
print(summa(50,300,100,100,))

def summa(*women):
    """A function that calculates the sum of the input number"""
    copybook = 0
    for woman in women:
        copybook+=woman
    return copybook
print(summa(1,2,3,4,5,6,7,8,9))

def summa(*junk_food):
    """A function that calculates the sum of the input number"""
    light_meal =0
    for hearty_breakfast in junk_food:
        light_meal +=hearty_breakfast
    return light_meal
print(summa(1,1,2,2,3,34,4,))

def summa(*substantial_meal):
    """A function that calculates the sum of the input number"""
    mentor =0
    for food_additives in substantial_meal:
        mentor +=food_additives
    return mentor
print(summa(1,3,4,5))


def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4,5,6,7))


def summa(*incomes):
    """A function that calculates the sum of the input number"""
    return sum(incomes)

print(summa(9999,9999))


def summa(*benefits):
    """A finction that calculate the sum of the input numbers"""
    return sum(benefits)
print(summa(1,2,3,4,5,67,78))


def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)
print(summa(2,2,2))

def summa(a,d,f,*you):
    """A function that calculates the sum of the input number"""
    return a,d-f,sum(you)
print(summa(1,20,3,4,5,5))

def avto_info(kompaniya,model,**malumotlar):
    """"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
print(avto2)


def avto_info(company,model,**valued_information):
    """What is the function of viewing information about the car in a dictionary"""
    valued_information['company'] = company
    valued_information['model'] = model
    return valued_information


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        if matnlar[i] == 'vali':
            matnlar[i] = matnlar[i].title()
            print(f"Salom, {matnlar[i]} ")
        else:
            matnlar[i] = matnlar[i].upper()


ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)






def my_func():
    print("Hello Arslonbek")

my_func()


def my_func(abc=None,*args,**kwargs ):
    print("Hello Arslonbek",args,**kwargs)

my_func("abc","abc",'iasdu',19782,key=123,abs = 4523)



def my_random_django_view(request,**kwargs):
    print(kwargs)

# path('my_product/:id')
my_random_django_view("request",id='some_id')


def add(a,b):
    return  a + b

print(add(12,76))


def add(*args):
    print(type(args))
add(12,76)


def add(*args):
    total = 0
    for arg in args:
        total +=arg
    return total

print(add(1,2,3))


def display_name(*args):
    for arg in args:
        print(arg,end="")

display_name("Arslonbek", "Arslon" ,"Arapov")


def print_address(**kwargs):
    print(type(kwargs))
print_address(street="Muhammad Yusuf ",
              city="boston",
              state="uzbekistan")


def print_address(**kwargs):
    for value in kwargs.keys():
        print(value)
print_address(street="Muhammad Yusuf ",
              city="boston",
              state="uzbekistan")


def print_address(**kwargs):
    for value in kwargs.values():
        print(value)
print_address(street="Muhammad Yusuf ",
              city="boston",
              state="uzbekistan")



def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="Muhammad Yusuf ",
              city="boston",
              apt ="40",
              state="uzbekistan")

def add_items(*args,**kwargs):
    print(args)
    result = sum(args)
    print(result)

add_items(1,2,3,4,5,6,6,7)
add_items(1,2,3,4,54,6,7,8,
1,2,3,4,5,6,7,7,8,9,112,34567)
add_items()
add_items(-2,-3,-46,67)
add_items(1,2,34,k=3,a=3)


