#homework

# Voris klasslardan yana boshqa voris klass yaratib ko'ring. Misol uchun Foydalanuvchi klassidan Admin klassini yarating.
# Admin klassiga foydalanuvchida yo'q yangi metodlar yozing, masalan, ban_user() metodi konsolga "Foydalanuvchi bloklandi" degan matn chiqarsin.



class User():
    """A class that provides data about user"""
    def __init__(self,name,b_age,position):
        self.name = name
        self.b_age = b_age
        self.position = position
    def get_info(self):
        """Information about a person"""
        info = f"{self.name}"
        info += f"{self.b_age} ,{self.position}"
        return info
    def get_age(self,year):
        """A method that returns a person's age"""
        return year - self.b_age

person = User('Arslopnbek',2006,'student')
print(f"{person.get_info()} . At the age of {person.get_age(2023)}:")


class Admin(User):
    """Student class"""
    def __init__(self,name,b_age,position,limit):
        """Characteristics of a student"""
        super().__init__(name,b_age,position)
        self.limit = limit
    def get_age(self,year):
        """A person's age """
        return year - self.b_age
    def ban_user(self):
        """A method that show why a person limited"""
        return self.limit
admin= Admin('Arslonbek' ,2006,'student','limit')
print(admin.get_info())
print(admin.ban_user())

























































