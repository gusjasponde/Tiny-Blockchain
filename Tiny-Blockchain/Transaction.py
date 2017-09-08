#   transcation formattranscation_list
#   {
#       "from": "<public-key>"
#       "to": "<public-key>"
#       "amount" : value
#   }
import Blockchain
from flask import Flask
from flask import request
from flask import Blueprint

#Exporting blueprint
transact_api = Blueprint('transact_api', __name__)

#Store transactions
transaction_list = []

@transact_api.route('/transact', methods=['POST'])
def transaction():
    if request.method == 'POST':
        #get all the data from transaction
        new_transaction = request.get_json()

        #add transaction to the list
        transaction_list.append(new_transaction)
        print("Transcaction included")
        print("Sender:   ", str(new_transaction['from']))
        print("Receiver: ", str(new_transaction['to']))
        print("Amount:   ", str(new_transaction['amount']))

        return "Submition successful\n"
