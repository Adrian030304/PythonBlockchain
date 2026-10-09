
import json
import csv
from datetime import date

from Transaction import Transaction

transaction = Transaction(id=1,
                          data=date(2020, 1,1),
                          sender="SC Alfa SRL",
                          recipient="SC Beta SRL",
                          amount=100,
                          currency="EUR",
                          status="pending"
                          )

nodes = ["node1.csv","node2.csv", "node3.csv", "node4.csv", "node5.csv"]

def tranzactii():
    pass

def citesteCSV():
    data = []
    with open("transactions.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)



if __name__ in "__main__":
    citesteCSV()

