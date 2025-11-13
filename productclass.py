class Product:
    def __init__(prod, name: str, price: float, quanitity: int):
        prod.name = name
        prod.price = price
        prod.quantity = quanitity
    
    def prodlist(prod):
        print(f"{prod.name:=^10}{prod.price:=^10}{prod.quantity:=^10}")

class MenCol:
    col1 = "Item"
    col2 = "Price"
    col3 = "Qty"

Columns = MenCol
print(f"{Columns.col1:=^10}{Columns.col2:=^10}{Columns.col3:=^10}")

product1 = Product("Juice", 10.0, 35)
product2 = Product("Chips", 15.0, 20)
product3 = Product("Hotdog", 25.0, 10)
product4 = Product("Hamburger", 30.0, 15)

product1.prodlist()
product2.prodlist()
product3.prodlist()
product4.prodlist()

selection = input("[Case Sensitive] Select Product: ")

if selection == "Juice":
    print("You've selected Juice: 10.0 P - 35x")
    quant = int(input("How many do you want? "))
    qtotal = quant-35+35
    qresult = qtotal*10
    print(f"That would be {qresult} P total for your {selection}")
    print(f"There are still {35-qtotal} left for {selection}")
elif selection == "Chips":
    print("You've selected Chips: 15.0 P - 20x")
    quant = int(input("How many do you want? "))
    qtotal = quant-20+20
    qresult = qtotal*15
    print(f"That would be {qresult} P total for your {selection}")
    print(f"There are still {20-qtotal} left for {selection}")
elif selection == "Hotdog":
    print("You've selected Hotdog: 25.0 P - 10x")
    quant = int(input("How many do you want? "))
    qtotal = quant-10+10
    qresult = qtotal*25
    print(f"That would be {qresult} P total for your {selection}")
    print(f"There are still {10-qtotal} left for {selection}")
else:
    print("You've selected Hamburger: 30.0 P - 15x")
    quant = int(input("How many do you want? "))
    qtotal = quant-15+15
    qresult = qtotal*30
    print(f"That would be {qresult} P total for your {selection}")
    print(f"There are still {15-qtotal} left for {selection}")
