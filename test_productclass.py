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

class ProdSell:
    def sellprompt():
        selection = input("[Case Sensitive] Select Product: ")
        match selection:
            case 'Juice':
                quant = int(input("How many do you want? "))
                left = product1.quantity-quant
                print(f"That would be {product1.quantity*product1.price} P and {left} remaining")
            case 'Chips':
                quant = int(input("How many do you want? "))
                left = product2.quantity-quant
                print(f"That would be {product2.quantity*product2.price} P and {left} remaining")
            case 'Hotdog':
                quant = int(input("How many do you want? "))
                left = product3.quantity-quant
                print(f"That would be {product3.quantity*product3.price} P and {left} remaining")
            case 'Hamburger':
                quant = int(input("How many do you want? "))
                left = product4.quantity-quant
                print(f"That would be {product4.quantity*product4.price} P and {left} remaining")

sl = ProdSell
sl.sellprompt()