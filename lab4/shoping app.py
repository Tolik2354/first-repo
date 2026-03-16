store = []
cart = []


def addClothingItem(name, price):
    item = {"name": name, "price": price}
    store.append(item)


def addToCart(name):
    for item in store:
        if item["name"] == name:
            cart.append(item)
            print(name, "додано в кошик")
            return
    print("Товар не знайдено")


def calculateTotalPrice():
    total = 0
    for item in cart:
        total += item["price"]
    return total


addClothingItem("Футболка", 500)
addClothingItem("Джинси", 1200)
addClothingItem("Куртка", 2500)

addToCart("Футболка")
addToCart("Джинси")

total = calculateTotalPrice()
print("Загальна сума покупки:", total, "грн")
