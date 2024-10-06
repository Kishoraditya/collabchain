import pytest
from brownie import EventContract, DataAgreementContract, accounts

def test_create_event():
    account = accounts[0]
    event_contract = EventContract.deploy({'from': account})
    tx = event_contract.createEvent("Launch", "Product launch event", {'from': account})
    assert tx.events["EventCreated"]["name"] == "Launch"
