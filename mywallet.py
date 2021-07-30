from web3 import Web3

#ganache_url = "http://127.0.0.1:7545"
ganache_url = "https://ropsten.infura.io/v3/ea36089880524f8ca0cfe20ee4443b70"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_2 = "0x36C96281AD544561D5323706A1Dfc953901e2FfA"
account_1 = "0x020592611055440119C441e654d6389754042a83"

private_key_account_1 = "2be96f9334820723c1005f386c110bd6798c4079028420764b23df2df7131f3a"

nonce = web3.eth.getTransactionCount(account_1)

balance = web3.eth.get_balance(account_1)
balance_decimal = web3.fromWei(balance, 'ether')
print(balance_decimal)

tx = {
    'nonce':nonce,
    'to':account_2,
    'value':web3.toWei(0.000001,'ether'),
    'gas':2000000,
    'gasPrice': web3.toWei('50','gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key_account_1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))