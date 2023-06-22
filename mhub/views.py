from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from web3 import Web3
from .forms import ContactForm
from .models import Airdrop, Contact, Roadmap, SmartContract
from web3.middleware import geth_poa_middleware


w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# ABI (Application Binary Interface) of the smart contract
contract_abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "nonce",
				"type": "uint256"
			},
			{
				"internalType": "address",
				"name": "referrer",
				"type": "address"
			}
		],
		"name": "claim",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_token",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_signer",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "user",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "nonce",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"indexed": False,
				"internalType": "address",
				"name": "referrer",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			}
		],
		"name": "Claim",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "disableClaiming",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "enableClaiming",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_newroute",
				"type": "uint256"
			}
		],
		"name": "routeUpdate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_newgen",
				"type": "uint256"
			}
		],
		"name": "setGeneral",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "val",
				"type": "address"
			}
		],
		"name": "setSigner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "_claimedUser",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "_usedNonce",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "claimedCount",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "claimedPercentage",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "claimedSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "GENERAL",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "inviteRewards",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "inviteUsers",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "isClaimingEnabled",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "path",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "referReward",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "REFFERALS",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "signer",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "token",
		"outputs": [
			{
				"internalType": "contract IERC20",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]

# Contract address
contract_address = '0x5481d02783Ac387d8E5af2064861eD8dE573c6Bc'

privateKey = '2e4fe09daab85f41489dad796408e7292045b3ce97071fdf46dd3a9664d76901'

def home(request):
    req = SmartContract().retrieve_data_from_contract() #getAirdrop


    # claimed_supply = int(SmartContract.objects.filter(id=5).first().claimedSupply) // 10**18
    return render(request, 'index.html', {
    # 'form': form,
    "roadmap_1": Roadmap.objects.filter(name='first').first(),
    "roadmap_2": Roadmap.objects.filter(name='second').first(),
    "roadmap_3": Roadmap.objects.filter(name='third').first(),
    "roadmap_4": Roadmap.objects.filter(name='fourth').first(),
    "roadmap_5": Roadmap.objects.filter(name='fifth').first(),
    "roadmap_6": Roadmap.objects.filter(name='six').first(),
    # 'claimed_supply': claimed_supply
})


def claim_airdrop(request):
    try:
        web3 = Web3()
        # Get the user's address and referral code from the request
        referral_code = request.POST.get('referral')
        if referral_code:
            referralCode = web3.to_checksum_address(referral_code)
        else:
            referralCode = web3.to_checksum_address('0x000000000000000000000000000000000000dEaD')
        user_address = request.POST.get('selectedAccount')
        userAddress = web3.to_checksum_address(user_address)

        print(referral_code)
        print(user_address)
        
        # Convert the referral code to bytes if necessary (check the contract's parameter type)
        # referral_bytes = referral_code.encode()  # Example: converting to UTF-8 bytes

        contract = w3.eth.contract(address=contract_address, abi=contract_abi)
        # Perform the claim function call on the Airdrop contract
        claim_txn = contract.functions.claim(1234, referralCode).build_transaction({
            'from': userAddress,
            'gas': 200000,  # Adjust the gas limit as needed
            'nonce': 1234,
            'gasPrice': w3.to_wei(5, 'gwei')  # Adjust the gas price as needed
        })

        # Send the transaction
        tx_hash = w3.eth.send_transaction(claim_txn)

        # signed_txn = web3.eth.account.sign_transaction(claim_txn, privateKey)

        # # Send the signed transaction
        # tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # Wait for the transaction to be mined and retrieve the transaction receipt
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(tx_receipt)
        return HttpResponse("Airdrop claim successful!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return HttpResponse("An error occurred during airdrop claim!")



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data['name']
            contact.email = form.cleaned_data['email']
            contact.message = form.cleaned_data['message']
            contact.save()
            ...
            # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})