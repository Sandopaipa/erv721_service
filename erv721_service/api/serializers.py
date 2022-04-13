import uuid

from rest_framework import serializers

from .models import Token

from web3 import Web3
import os
import env

env = env.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
env.Env.read_env()


class TokenCreateSerializer(serializers.ModelSerializer):
    """Token creation serializer"""
    def get_txhash(self):
        web3 = Web3(Web3.HTTPProvider(url=env('INFURA_URL')))
        if web3.isConnected():
            Greeter = web3.eth.contract(abi=env('ABI'), bytecode=env('BYTECODE'))
            tx_hash = Greeter.constructor().transact()
            return tx_hash
    unique_hash = serializers.CharField(default=uuid.uuid1().hex())
    tx_hash = serializers.CharField(default=get_txhash())

    class Meta:
        model = Token
        fields = (
            'media_url',
            'owner',
        )


class TokenListSerializer(serializers.ModelSerializer):
    """print all tokens"""
    class Meta:
        model = Token
        fields = '__all__'


class TokenTotalsupplySerializer(serializers.ModelSerializer):
    pass
