import csv
import numpy as np
import api

csv_path = './investment.csv'
with open(csv_path) as f:
    reader = csv.reader(f, delimiter=',')
    headers = next(reader)
    investments = np.array(list(reader)).astype(str)




def show_invest():
    for row in investments:
        print("On the date of {}, you purchased {} Bitcoin for the amount of ${}".format(row[0], row[1], row[2]))



def show_gains():
    amount = 0
    price = api.value
    for row in investments:
        amount += float(row[1])
        value = amount * price
    print(f"Your total portfolio value is {value}, with a total of {amount} BTC")

show_invest()
show_gains()