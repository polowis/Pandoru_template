from web3 import Web3
from app.framework.util import *
from flask import jsonify
import json
from app import app
from app.framework.controller import *
from app.framework.requests.request import request
from app.configuration.web3_config import *


def get_provider():
    return IPC_PROVIDER or HTTP_PROVIDER or WS_PROVIDER

infura_url = HTTP_PROVIDER + PROJECT_ID
web3 = Web3(Web3.HTTPProvider(infura_url))


balance = web3.fromWei(web3.eth.getBalance(address_server), 'ether')

class TransactionController(Controller):
    def construct(cls):
        TransactionController.register(app)

    
    @route('/api/ethereum/send')
    def send_ethereum_transaction(self):
        private_key = data['privateKey']
        nonce = web3.eth.getTransactionCount(address_server)
        address_server= data['address']
        balance = web3.fromWei(web3.eth.getBalance(address_server), 'ether')
        address_destination = data['address_destination']
        value = data['value']
        tx = {
            'nonce': nonce,
            'to': address_destination,
            'value': web3.toWei(value, 'ether'),
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
        }
        signed_tx = web3.eth.account.signTransaction(tx, private_key)
        tx_hash = web3.toHex(web3.eth.sendRawTransaction(signed_tx.rawTransaction))

        balance_server = web3.fromWei(web3.eth.getBalance(address_server), 'ether')
        return jsonify(message="Success")