class Restaurant:
    def __init__(self):
        self.restaurant_name = "Вкусняшка"
        self.cuisine_type = "Русская"
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("Наш ресторан открыт!")
p = Restaurant()
p.describe_restaurant()
p.open_restaurant()