from web3 import Web3

node_url = 'YOUR NODE URL'                                          # mainnet endpoint URL
web3 = Web3(Web3.HTTPProvider(node_url))                            # establish connection to a ETH mainnet node

# verify the connection is successful (will return true)
if web3.isConnected():                                                          
    print('Connection Succsessful')
else:
    print('Connection Failed')

# print the latest block
print('The latest block number is: ', web3.eth.blockNumber)                     

# return an address balance in wei
balance = web3.eth.get_balance('0x88E0204C86ddA961dAcC231Ec275ad095382d61B')    #random address found on BSCScan

# converts from wei to eth
weiToEth = web3.fromWei(balance , 'ether')                              
print('BNB balance: ' , weiToEth)

# retrive transactions hash
pending_tx_filter = web3.eth.filter('pending')       # can use 'latest' to get the latest transactions
pending_tx = pending_tx_filter.get_new_entries()     # this is a list object
#print(pending_tx)

# loop through the list of transcations and displays the tx hash
for hash in pending_tx:
    print('Hash of a Pending Transaction:' , web3.toHex(hash))      # web3.toHex converts from bytes to hex

#  extract data from the hash                                                         
details = web3.eth.getTransaction('0x0572d76caf0b37be8021d84d6fccdcc466824b8e9dce68eef079f5e5d055139e')         #random hash found on BSCScan
#print(details)

# convert the web3 object into a dictionary that python can read
# convert any 'AttributeDict' type found to 'dict' and extract data

info = ['from','to', 'gas','value']                  # value is printed in wei, we need to add this: web3.fromWei(val , 'ether')
parsedDict = dict(details)    
for key, val in parsedDict.items():
    for word in info:
        if key == word:
            print(key , val)
