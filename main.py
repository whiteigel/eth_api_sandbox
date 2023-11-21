from web3 import Web3
from address_dict import *
from ids import *

INFURA_ID = INFURA_ID

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_ID}'))

# This function checks the balances of your accounts
def check_balance_names(address_dict):
    for account, address in address_dict.items():
        balance_request = w3.eth.get_balance(address)
        balance = w3.from_wei(balance_request, 'ether')
        print(f'The balance on Etherium for {account} is {balance} eth')

# This function counts number of transactions of your accounts
def transaction_count(address_dict):
    for account, address in address_dict.items():
        transaction_number = w3.eth.get_transaction_count(address)
        if transaction_number == 0:
            print(f'There is no transaction on Etherium for {account}')
        else:
            print(f'You have {transaction_number} transactions on Etherium for {account}')

# This function checks current gas price and shows it in gwei
def get_gas_price():
    gas_price_wei = w3.eth.gas_price
    gas_gwei = round(w3.from_wei(gas_price_wei, 'gwei'),1)
    print(f'Current gas is {gas_gwei} gwei')


get_gas_price()
#check_balance_names(ADDRESS_DICT)
#transaction_count(ADDRESS_DICT)
