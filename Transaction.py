#   transcation format
#   {
#       "from": "<public-key>"
#       "to": "<public-key>"
#       "amount" : value
#   }
import Blockchain
from flask import Flask
from flask import request

node = Flask(__name__)

#Store transactions
transcation_list = []

@node.route('/transact', methods=['POST'])
def transaction():
    if request.method == 'POST':
        #get all the data from transaction
        new_transaction = request.get_json()

        #add transaction to the list
        transcation_list.append(new_transaction)
        print("Transcaction included")
        print("Sender:   ", str(new_transaction['from']))
        print("Receiver: ", str(new_transaction['to']))
        print("Amount:   ", str(new_transaction['amount']))

        return "Submition successful\n"

node.run()
