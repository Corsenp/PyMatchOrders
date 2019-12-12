import csv
import sys

class Order:
    def __init__(self, id, account, pair, action, price):
        self.id = id
        self.account = account
        self.pair = pair
        self.action = action
        self.price = price
        self.match = ""

def init_order(row):
    '''
    Will create a Order object with the data from @row
    '''
    try:
        id = row[0].replace(" ", "")
        account = row[1].replace(" ", "")
        pair = row[2].replace(" ", "")
        action = row[3].replace(" ", "")
        price = row[4].replace(" ", "")

        order = Order(id, account, pair, action, price)
        return order
    except:
        print("Error while creating Order object")

def open_csv(csv_name):
    '''
    Open the @csv_name and fill orders with data
    '''
    orders = []
    try:
        with open(csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                new_order = init_order(row)
                orders.append(new_order)
        return orders
    except csv.Error:
        print("Error while opening the csv file")
        sys.exit(-1)

def parse_orders(orders):
    '''
    Function that will parse @orders and match the trades
    '''
    try:
        i = 1
        order_len = len(orders) - 1
        while i <= order_len:
            y = 1
            while y <= order_len:
                if (orders[y].price == orders[i].price and\
                    orders[y].pair == orders[i].pair and\
                    orders[y].action != orders[i].action and\
                    orders[y].account != orders[i].account and\
                    orders[y].match == "" and orders[i].match == ""):
                        orders[i].match = orders[y].id
                        orders[y].match = orders[i].id
                y += 1
            i += 1
    except:
        print("Error while parsing orders")
        sys.exit(-1)

def reject_undone_trade(orders):
    '''
    Function that will put REJECTED inside the @orders that didn't matched
    '''
    try:
        i = 1
        order_len = len(orders) - 1
        while i <= order_len:
            if orders[i].match == "":
                orders[i].match = "REJECTED"
            i = i + 1
    except:
        print("Error while Rejecting undone trades")
        sys.exit(-1)

def prompt_orders(orders):
    '''
    Function to prompt the @orders in the terminal
    '''
    orders_number = len(orders) - 1
    i = 0
    while i <= orders_number:
        if (i == 0):
            print('\n{},{},{},{},{}, match'.format(orders[i].id, orders[i].account, orders[i].pair, orders[i].action, orders[i].price))
        else:
            print('{}, {}, {}, {}, {}, {}'.format(orders[i].id, orders[i].account, orders[i].pair, orders[i].action, orders[i].price, orders[i].match))
        i += 1

def ask_user_csv(orders):
    answer = input("Do you want the result exported to a csv (y/n) ?\n")
    if answer == 'y' or answer == 'yes':
        print("must be exported to a csv")
        return 1
    elif answer == 'n' or answer == 'no':
        prompt_orders(orders)
        return 0
    else:
        ask_user_csv(orders)

def main():
    '''
    Main function
    '''
    orders = open_csv(".//orders.csv")
    parse_orders(orders)
    reject_undone_trade(orders)
    ask_user_csv(orders)
    
main()