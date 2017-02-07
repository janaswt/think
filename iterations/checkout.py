def checkout():
    total = 0
    count = 0
    more_items = True
    while more_items:
        price = float(int(input("Enter price of item (0 when done): ")))
        if price > 0:
            count = count + 1
            total = total + price
            print("Subtotal: $", total)
        elif price < 0:
            print("Cena nie może być ujemna")
        else:
            print("Koniec")
            more_items = False
    if count > 0:
        average = total / count
        print('Total items:', count)
        print('Total $', total)
        print('Average price per item: $', average)
        
checkout()
