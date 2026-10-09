

class Transaction:

    def __init__(self, id, data, sender, recipient, amount, currency, status):
        self.id = id
        self.data = data
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.currency = currency
        self.status = status