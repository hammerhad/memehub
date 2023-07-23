from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from web3 import  Web3
from .forms import ContactForm
from .models import Contact, Roadmap, SmartContract, Airdrop2
from web3.middleware import geth_poa_middleware
import time
from decouple import config

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# ABI (Application Binary Interface) of the smart contract
# contract_abi = [
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "nonce",
# 				"type": "uint256"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "referrer",
# 				"type": "address"
# 			}
# 		],
# 		"name": "claim",
# 		"outputs": [],
# 		"stateMutability": "payable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "disableClaiming",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "_token",
# 				"type": "address"
# 			},
# 			{
# 				"internalType": "address",
# 				"name": "_signer",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "nonpayable",
# 		"type": "constructor"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "user",
# 				"type": "address"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "uint256",
# 				"name": "nonce",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "uint256",
# 				"name": "amount",
# 				"type": "uint256"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "address",
# 				"name": "referrer",
# 				"type": "address"
# 			},
# 			{
# 				"indexed": False,
# 				"internalType": "uint256",
# 				"name": "timestamp",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "Claim",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "enableClaiming",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"anonymous": False,
# 		"inputs": [
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "previousOwner",
# 				"type": "address"
# 			},
# 			{
# 				"indexed": True,
# 				"internalType": "address",
# 				"name": "newOwner",
# 				"type": "address"
# 			}
# 		],
# 		"name": "OwnershipTransferred",
# 		"type": "event"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "renounceOwnership",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "newGeneral",
# 				"type": "uint256"
# 			}
# 		],
# 		"name": "setGeneral",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "val",
# 				"type": "address"
# 			}
# 		],
# 		"name": "setSigner",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "newOwner",
# 				"type": "address"
# 			}
# 		],
# 		"name": "transferOwnership",
# 		"outputs": [],
# 		"stateMutability": "nonpayable",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "claimedCount",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "claimedSupply",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "general",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "account",
# 				"type": "address"
# 			}
# 		],
# 		"name": "inviteRewards",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "account",
# 				"type": "address"
# 			}
# 		],
# 		"name": "inviteUsers",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "isClaimingEnabled",
# 		"outputs": [
# 			{
# 				"internalType": "bool",
# 				"name": "",
# 				"type": "bool"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "bytes",
# 				"name": "signature",
# 				"type": "bytes"
# 			}
# 		],
# 		"name": "isValidSignature",
# 		"outputs": [
# 			{
# 				"internalType": "bool",
# 				"name": "",
# 				"type": "bool"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "owner",
# 		"outputs": [
# 			{
# 				"internalType": "address",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [
# 			{
# 				"internalType": "address",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"name": "path",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "referrals",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "referReward",
# 		"outputs": [
# 			{
# 				"internalType": "uint256",
# 				"name": "",
# 				"type": "uint256"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "signer",
# 		"outputs": [
# 			{
# 				"internalType": "address",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	},
# 	{
# 		"inputs": [],
# 		"name": "token",
# 		"outputs": [
# 			{
# 				"internalType": "contract IERC20",
# 				"name": "",
# 				"type": "address"
# 			}
# 		],
# 		"stateMutability": "view",
# 		"type": "function"
# 	}

# ]

# Contract address
contract_address = "0x4488032cbeDE1d0481aCB000dD98c0d804c80655"

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

def send(request):
    if request.method == 'POST':
        user_address = request.POST.get('selectedAccount')
        referral_address = request.POST.get('referral')

        # Check if user_address already exists in the database
        if Airdrop2.objects.filter(user_address=user_address).exists():
            return HttpResponse('User has already taken the Airdrop')
        
        # Save the user_address and referral_address in the database
        airdrop = Airdrop2(user_address=user_address, referral_address=referral_address)
        time.sleep(2)
        airdrop.save()

        return ('success')  # Redirect to a success page or another URL
    
    return render(request, 'send.html')

def checkAirdropStatus(request):
    if request.method == 'GET':
        selected_account = request.GET.get('selectedAccount')

        # Check if user_address already exists in the database
        if Airdrop2.objects.filter(user_address=selected_account).exists():
            return HttpResponse('already_taken')
        
        return HttpResponse('eligible')

    return HttpResponse('Invalid request')

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