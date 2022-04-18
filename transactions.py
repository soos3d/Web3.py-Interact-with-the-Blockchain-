from web3 import Web3
import json

node_url = 'YOUR NODE URL'    # mainnet endpoint URL
web3 = Web3(Web3.HTTPProvider(node_url))                                           # establish connection to a ETH mainnet node

# verify the connection is successful (will return true)
if web3.isConnected():                                                          
    print('Connection Succsessful')
else:
    print('Connection Failed')

# send currency (blockchain currency, eth, bnb etc)
account_1 = "address sending"                               # account sending crypto
account_2 = "address receiving"                             # account receving crypto

privateKey = "ACCOUNT SENDING PRIVATE KEY"     # private key of the account sending crypto

# get the nonce, account sending
nonce = web3.eth.getTransactionCount(account_1) 

# Build the transaction
tx = {
    'nonce': nonce,                                 # ensures the transaction is only sent once
    'to': account_2,                                # account receiving
    'value': web3.toWei(0.1, 'ether'),              # amount to send 
    'gas' : 200000,                                 # max gas allocated
    'gasPrice' : web3.toWei(7 , 'gwei')          
}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, privateKey)    # use the private key to sign the transaction

# send transaction and get transaction hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)     
print(web3.toHex(tx_hash))                                          

# monitor pending transactions

new_transaction_filter = web3.eth.filter('pending')
print(new_transaction_filter.get_new_entries())         # tx hash
