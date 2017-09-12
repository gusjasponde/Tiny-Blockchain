from Transaction import transact_api
from Mining import mining_api
from Consensus import consensus_api
from flask import Flask

#Creating node variable that will be
#passed to other modules in the blockchain application

app = Flask(__name__)

#adding routes defined in other modules

app.register_blueprint(transact_api)
app.register_blueprint(mining_api)
app.register_blueprint(consensus_api)

@app.route("/")
def response():
    return "Welcome to Tiny-Blockchain!"

if __name__ == "__main__":
    app.run()
