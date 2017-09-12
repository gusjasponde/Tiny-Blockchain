#   transcation formattranscation_list
#   {
#       "sender": "<public-key>"
#       "receiver": "<public-key>"
#       "amount" : value
#   }
import Blockchain
from flask import Flask
from flask import request
from flask import Blueprint
from flask import json
from flask import jsonify
from Util import ComplexEncoder

#Exporting blueprint
transact_api = Blueprint('transact_api', __name__)

#Store transactions
transaction_list = []

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def reprJSON(self):
        return dict(sender=self.sender, receiver=self.receiver, amount=self.amount)

@transact_api.route('/transact', methods=['POST'])
def transaction():
    if request.method == 'POST':
        #get all the data from transaction
        new_transaction = request.get_json()
        #add transaction to the list
        transaction_list.append(
        json.dumps(
            Transaction(
                new_transaction["sender"], new_transaction["receiver"], new_transaction["amount"]
                ).reprJSON(),
            cls=ComplexEncoder)
        )

        print("Transcaction included")
        print("Sender:   ", str(new_transaction['sender']))
        print("Receiver: ", str(new_transaction['receiver']))
        print("Amount:   ", str(new_transaction['amount']))

        return "Submition successful\n"
