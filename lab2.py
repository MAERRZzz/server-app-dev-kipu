class Toy:
    def __init__(self, name, size, category, price):
        self.name = name
        self.size = size
        self.category = category
        self.price = price


class Playroom:
    def __init__(self, budget):
        self.budget = budget
        self.toys = []

    def add_toy(self, toy):
        if toy.price <= self.budget:
            self.toys.append(toy)
            self.budget -= toy.price
        else:
            print(f'Недостаточно средств для добавления "{toy.name}"')

    def sort_toys_by_price(self):
        self.toys.sort(key=lambda toy_object: toy_object.price)

    def find_toys_in_price_range(self, min_value, max_value):
        result = []
        for toy in self.toys:
            value = toy.price

            if min_value <= value <= max_value:
                result.append(toy)

        return result

    @staticmethod
    def print_toys():
        for toy in playroom.toys:
            print(f"\n{toy.name} - Размер: {toy.size}, Категория: {toy.category}, Цена: {toy.price} руб.")


playroom = Playroom(600)

car = Toy("Машина", "малый", "машины", 50)
car2 = Toy("Машина2", "малый", "машины", 55)
doll = Toy("Барби", "средний", "куклы", 200)
ball = Toy("Футбольный мяч", "большой", "мячи", 250)

playroom.add_toy(car)
playroom.add_toy(car2)
playroom.add_toy(doll)
playroom.add_toy(ball)
playroom.print_toys()

playroom.sort_toys_by_price()
print("-------------------\nСортировка:")
playroom.print_toys()

in_range = playroom.find_toys_in_price_range(100, 300)
print("-------------------\nПоиск в диапазоне:")

for toy in in_range:
    print(f"{toy.name} - {toy.price} руб.")
