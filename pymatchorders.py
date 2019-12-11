import csv
import sys

def init_dictionnary():
    data = {
        "id": [],
        "account": [],
        "pair": [],
        "action": [],
        "price": [],
    }
    return data

def clean_dictionnary(data):
    try:
        data["id"].pop(0)
        data["account"].pop(0)
        data["action"].pop(0)
        data["pair"].pop(0)
        data["action"].pop(0)
        data["price"].pop(0)
    except IndexError:
        print("Error while cleaning Data")
        sys.exit(-1)

def open_csv(csv_name, data):
    try:
        with open(csv_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data["id"].append(row[0].replace(" ", ""))
                data["account"].append(row[1].replace(" ", ""))
                data["pair"].append(row[2].replace(" ", ""))
                data["action"].append(row[3].replace(" ", ""))
                data["price"].append(row[4].replace(" ", ""))

    except csv.Error:
        print("Error while opening the csv file")
        sys.exit(-1)

def main():
    '''
    Main function
    '''
    print("main")
    data = init_dictionnary()
    open_csv(".//orders.csv", data)
    clean_dictionnary(data)
    print(data)

main()