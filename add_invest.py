import api


datein = input("What is todays date: ")
amtin = input("How much Bitcoin did you buy today: ")

def add_invest(date,amt):
    price = api.value
    with open('./investment.csv', 'a') as f:
        entry = "\n{},{},{}".format(date,amt,price)
        f.write(entry)

add_invest(datein, amtin)