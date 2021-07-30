from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

def transaction_init(sender_account, sender_private_key, reciever_account,token):
    #account_1 = "0x36C96281AD544561D5323706A1Dfc953901e2FfA"
    #account_2 = "0x020592611055440119C441e654d6389754042a83"

    #private_key_account_1 = "314db87f6b53ee2c0222afe57e5a44f9c856f75109384e8053050d08f565d693"

    nonce = web3.eth.getTransactionCount(sender_account)

    tx = {
        'nonce':nonce,
        'to':reciever_account,
        'value':web3.toWei(token,'ether'),
        'gas':2000000,
        'gasPrice': web3.toWei('50','gwei')
    }

    signed_tx = web3.eth.account.signTransaction(tx, sender_private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(web3.toHex(tx_hash))
    return web3.toHex(tx_hash)


def get_balance(account):
    balance = web3.eth.get_balance(account)
    balance_decimal = web3.fromWei(balance, 'ether')
    return balance_decimal