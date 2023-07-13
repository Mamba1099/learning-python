selling_price =  int(input("Enter the selling price: "))
buying_price =int(input("Enter the buying price: "))     


profit = selling_price  - buying_price
percentage_profit = ((selling_price - buying_price) * 100) / selling_price
loss = buying_price - selling_price
percentage_loss = ((buying_price - selling_price) * 100) / selling_price

def my_profit():
  if selling_price > buying_price:
    print("profit = ", + profit)
    print("percentage profit = ", + percentage_profit)
  else:
    print("loss = ", + loss)
    print("percentage loss = ", + percentage_loss)

my_profit()




