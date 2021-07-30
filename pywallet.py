import json
from web3 import Web3

#ganache_url = "http://127.0.0.1:7545"
ganache_url = "https://ropsten.infura.io/v3/ea36089880524f8ca0cfe20ee4443b70"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')

address = '0x24E087F615c0d0BB8f85e04c57ea1734E608FB1c'

print(Web3.toChecksumAddress(address))

contract = web3.eth.contract(address=address,abi=abi)
total_supply = contract.functions.totalSupply().call()

total_supply = contract.functions._totalSupply().call()
print(total_supply)

balance = contract.functions.balanceOf('0xa335d52202efCF56E353AF004B88cd5096204229').call()

print(web3.fromWei(balance,'ether'))


account_2 = "0x36C96281AD544561D5323706A1Dfc953901e2FfA"
account_1 = "0x020592611055440119C441e654d6389754042a83"

private_key_account_1 = "2be96f9334820723c1005f386c110bd6798c4079028420764b23df2df7131f3a"



nonce = contract.getTransactionCount(account_1)

print(nonce)
"""
tx = {
    'nonce':nonce,
    'to':account_2,
    'value':web3.toWei(0.0001,'ether'),
    'gas':2000000,
    'gasPrice': web3.toWei('50','gwei')
}

signed_tx = contract.account.signTransaction(tx, private_key_account_1)
print(signed_tx)"""
"""
balances = web3.eth.get_balance(account_2)
print(contract.functions.symbol().call())
print(web3.fromWei(balances,'ether'))


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
    'value':web3.toWei(0.0001,'ether'),
    'gas':2000000,
    'gasPrice': web3.toWei('50','gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key_account_1)
print(signed_tx)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))"""