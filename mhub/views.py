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
# contract_abi = config('AIRDROP_ABI')

# Contract address
contract_address = config('AIRDROP_ADDRESS')

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