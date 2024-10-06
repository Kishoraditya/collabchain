from flask import Flask, request, render_template, jsonify
from web3 import Web3
import json

app = Flask(__name__)

# Connect to Base Sepolia testnet
w3 = Web3(Web3.HTTPProvider('https://sepolia.base.org'))

# Load EventContract ABI
with open('event_contract_abi.json', 'r') as f:
    event_abi = json.load(f)
event_contract_address = '0xYOUR_EVENT_CONTRACT_ADDRESS'

event_contract = w3.eth.contract(address=event_contract_address, abi=event_abi)

# Load DataAgreementContract ABI
with open('data_agreement_abi.json', 'r') as f:
    agreement_abi = json.load(f)
agreement_contract_address = '0xYOUR_AGREEMENT_CONTRACT_ADDRESS'

agreement_contract = w3.eth.contract(address=agreement_contract_address, abi=agreement_abi)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        tx_hash = event_contract.functions.createEvent(name, description).transact({'from': w3.eth.accounts[0]})
        return jsonify({'status': 'Event created', 'tx_hash': tx_hash.hex()})
    return render_template('create_event.html')

@app.route('/view_event/<int:event_id>')
def view_event(event_id):
    event = event_contract.functions.getEvent(event_id).call()
    return render_template('view_event.html', event=event)

@app.route('/create_agreement', methods=['GET', 'POST'])
def create_agreement():
    if request.method == 'POST':
        acceptor = request.form['acceptor']
        terms = request.form['terms']
        tx_hash = agreement_contract.functions.proposeAgreement(acceptor, terms).transact({'from': w3.eth.accounts[0]})
        return jsonify({'status': 'Agreement proposed', 'tx_hash': tx_hash.hex()})
    return render_template('create_agreement.html')

@app.route('/view_agreement/<int:agreement_id>')
def view_agreement(agreement_id):
    agreement = agreement_contract.functions.getAgreement(agreement_id).call()
    return render_template('view_agreement.html', agreement=agreement)

if __name__ == '__main__':
    app.run(debug=True)
