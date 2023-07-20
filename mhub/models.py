from django.db import models
from web3 import Web3
from decouple import config

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed1.binance.org'))

# ABI (Application Binary Interface) of the smart contract
contract_abi = config('COIN_ABI')

# Contract address
contract_address = config('COIN_ADDRESS')

# Create your models here.


class SmartContract(models.Model):
    referalReward = models.CharField(max_length=100)
    claimedSupply = models.CharField(max_length=100)
    isClaimingEnabled = models.BooleanField(null=True)

    @classmethod
    def retrieve_data_from_contract(cls):
        # Load the contract ABI
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)

        # Retrieve data from the smart contract using contract function calls
        referal_reward = contract.functions.referReward().call()
        claimed_supply = contract.functions.claimedSupply().call()
        is_claiming_enabled = contract.functions.isClaimingEnabled().call()

        # Get the existing instance if it exists, otherwise create a new instance
        instance, created = cls.objects.get_or_create(
            defaults={
                'referalReward': referal_reward,
                'claimedSupply': claimed_supply,
                'isClaimingEnabled': is_claiming_enabled
            }
        )

        if not created:
            # If the instance already exists, update its fields
            instance.referalReward = referal_reward
            instance.claimedSupply = claimed_supply
            instance.isClaimingEnabled = is_claiming_enabled
            instance.save()

        return instance
    
class Text(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.name

class TimeLeft(models.Model):
    name = models.CharField(max_length=100)
    date = models.TextField()
    def __str__(self):
        return self.name

class Roadmap(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=250)
    
class Airdrop2(models.Model):
    user_address = models.CharField(max_length=100)
    referral_address = models.CharField(max_length=100, null=True)