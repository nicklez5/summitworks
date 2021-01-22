purchase = [4.95, 9.95, 14.95 , 19.95 , 24.95]
def func(list_me):
    for i in list_me:
        print("Original price:$ ",i)
        x = 0.6*i
        x = round(x,2)
        print("Discount Amount:$ ",x)
        x = i - x
        x = round(x,2)
        print("New Price: $ ", x)
func(purchase)
