class Car():
    brand = ""
    model = ""
    color = ""
    speed = ""
    def __init__(self):
        print("Object Created!")

    def change_details(self):
        self.brand = input("Name of brand: ")
        self.model = input("Name of model: ")
        self.color = input("Color: ")
        self.speed = input("Maximum speed: ")

    def show_details(self):
        print(self.brand)
        print(self.model)
        print(self.color)
        print(self.speed)
Mercedes = Car()
Mercedes.show_details()