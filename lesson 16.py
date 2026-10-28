class Book:
    def __init__(self, title, author, pages):
            self.title = title
            self.author = author
            self.pages = pages
    def info(self):
        print(f"{self.title} — {self.author}, {self.pages} გვ.")

book3 = Book("კადმოსის მემკვიდრენი","ჯემალ ქარჩხაძე", 320)
book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 250)
book2 = Book("ბახტრიონი", "ილია ჭავჭავაძე", 180)
book2.info()
book1.info()
book3.info()

class Car:
    def __init__(self, brand,color,year):
            self.brand = brand
            self.color = color
            self.year = year
    wheels = 4
car1 = Car("BMW", 'შავი', 2020)
car2 = Car("Toyota", "თეთრი", 2018)
print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)
car2.wheels = 3
# car2.wheels = 3 მხოლოდ მეორე მანქანას შეუქმნა საკუთარი მნიშვნელობა.
# Car.wheels ისევ 4 დარჩა.
# car1 მნიშვნელობას კვლავ კლასიდან იღებს — 4
print(car1.wheels)
print(car2.wheels)
print(Car.wheels)

class Player:
    players_count = 0
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

        Player.players_count += 1
print(Player.players_count)  # შექმნამდე: 0

player1 = Player("ანა")
player2 = Player("დავითი", 5)
player3 = Player(name="მარიამი", level=3)

print("სულ მოთამაშე:", Player.players_count)
print(player1.name, player1.level)
print(player2.name, player2.level)
print(player3.name, player3.level)




