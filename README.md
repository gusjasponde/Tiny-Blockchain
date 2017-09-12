# Tiny-Blockchain
Implementation of a simple blockchain for study purposes

# Installing dependencies
Tiny-Blockchain uses Python with flask:
    
    sudo apt-get update
    pip install flask
    
# Running the client

    cd Tiny-Blockchain
    python Run.py
    
The server should show the new blocks included:
    
    Block # 1  added
    Hash:  1437f0fb85bf7e072fa873c5ac45bb337d5f0bfc5df7d1d31fb559519077abc6
    Block # 2  added
    Hash:  2e0aa7de933155392141952cefc063422c596c5c5765a9df559ef0d5e9458b0f
    Block # 3  added
    Hash:  bb92efefc65f61c177719e94b055924fcfe7bce56117bcae58df0986e356de28
    Block # 4  added
    Hash:  03e0c42643a46538fc292d2df81fdc93c8b91e37ac7a05ce4d12e0352205a3ff
    Block # 5  added
    Hash:  c4214c0a90ff16bdc3d984612da4e702220766012d1d4f691c64a2e2e11aa252
    Block # 6  added
    Hash:  8741f80ca9967dcfb78a973b35938ff7f3072e8f214a65b1061706e0eaed1449
    Block # 7  added
    Hash:  f42837946df192496adeb83443bc4b3a093c69ca053ae11774fe456304049679
    Block # 8  added
    Hash:  33ae5efc145cdd55a8f7284674daf4d4db4f56abb5427a901855879d88315ce9
    Block # 9  added
    Hash:  f0c18ce3c290ab3c054750c1713dfc416eaeceba62260cacf44b35ce247aaa98
    Block # 10  added
    Hash:  764095a37fa38b3821ca0e7477468254388cecd0807c6576e0d29615226f1075

The default configuration will create 10 new empty blocks when starting, you can change this on Blockchain.py "genesis_blocks_qty" variable.

# Mining
You receive a json response of the new mined block:

    // http://localhost:5000/mine

    {
      "hash": "cf12930bc6671c9bce7f4bf9b47af835b1d9a32b667c8dda71e66f03470bca3e",
      "previous_hash": "dff02d66bbf353e61d5b4cc7c383d5cf78eab334b5bb524567fa5225b61645ba",
      "data": "{\"transactions\": \"[\\\"{
        \\\\\\\"amount\\\\\\\": 1,
        \\\\\\\"sender\\\\\\\": \\\\\\\"network-reward\\\\\\\",
        \\\\\\\"receiver\\\\\\\": \\\\\\\"d2958a8e0a1d2ff69c9c74c4e2e1467a3c157d926457345fa4ee2a39e909ba99\\\\\\\"
      }\\\"]\", \"proof-of-work\": 20}",
      "timestamp": "2017-09-12T02:59:32.121081",
      "index": 11
    }
    
Currently the JSON response is ugly, I'm working on it

# Getting the chain
    
    // http://localhost:5000/chain
    
    [
      {
        "hash": "7aa39862376ec633b0543c453b84f9c6bc3be8c1a0e9da4fd37f506449f94bf9",
        "previous_hash": "0",
        "data": "Genesis block",
        "timestamp": "2017-09-12T03:06:03.657429",
        "index": 0
      },
      {
        "hash": "8dee6e3c85cf1b4e204c447eaaef9f609f203d19093db44963b222f2c18f2a3c",
        "previous_hash": "7aa39862376ec633b0543c453b84f9c6bc3be8c1a0e9da4fd37f506449f94bf9",
        "data": "{\"transactions\": \"Initial block\", \"proof-of-work\": 1}",
        "timestamp": "2017-09-12T03:06:03.657717",
        "index": 1
      },
      {
        "hash": "87856f7a4d335d1a8db7166ea0c4274a320f957fa3d6a6781170ce4675eeb398",
        "previous_hash": "8dee6e3c85cf1b4e204c447eaaef9f609f203d19093db44963b222f2c18f2a3c",
        "data": "{\"transactions\": \"Initial block\", \"proof-of-work\": 2}",
        "timestamp": "2017-09-12T03:06:03.657883",
        "index": 2
      },

        ...

  # Posting a Transaction
  Send a Post request with the following body:
  
      //http://localhost:5000/transact
      
      curl "localhost:5000/transact" 
      -H "Content-Type: application/json"
      -d '{
            "sender": "60DF8FF16825FCE628555F6FA54F5CADAC5658A000189E0963FB174310005E70", 
            "receiver":"FF0A62F3F3CF3C6A792C008994CEB93BEC64E8FB97A56E2ABDD085D4AEE13B45", 
            "amount": 3
          }'
          
You should get the response:
      
      Submition successful
      
And the server will show the new transaction included:

      Transcaction included
      ('Sender:   ', '60DF8FF16825FCE628555F6FA54F5CADAC5658A000189E0963FB174310005E70')
      ('Receiver: ', 'FF0A62F3F3CF3C6A792C008994CEB93BEC64E8FB97A56E2ABDD085D4AEE13B45')
      ('Amount:   ', '3')
