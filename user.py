class User:
    def __init__(self):
        pass
    def describe_user(self):
        print("Имя", self.first_name)
        print("Фамилия", self.last_name)
        print("Хобби", self.hobby)
        print("Возраст", self.status)
    def greet_user(self):
        print("Добро пожаловать",self.last_name, self.first_name, "!")
a = User()
print("Регистрация:")
a.first_name = str(input("Ваше имя: "))
a.last_name = str(input("Ваша фамилия: "))
a.hobby = str(input("Ваше хобби: "))
a.status = str(input("Сколько вам лет: "))
print("-------------------------------------------------")
print("Выполнен автоматический вход!\nИнформация о себе:")
a.describe_user()
a.greet_user()