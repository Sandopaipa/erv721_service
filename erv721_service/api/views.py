from web3 import Web3

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Token

from .serializers import TokenListSerializer
from .serializers import TokenCreateSerializer
from .serializers import TokenTotalsupplySerializer

import env
env = env.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
env.Env.read_env()


class TokenCreateView(APIView):
    """Connecting with infura"""
    """Getting tx_hash"""
    def post(self, request):
        token = TokenCreateSerializer(data=request.data)
        if token.is_valid():
            token.save()
        return Response(status=201)


class TokenListView(APIView):
    def get(self, request):
        tokens = Token.objects.all()
        serializer = TokenListSerializer(tokens)
        return Response(serializer.data)


class TokenTotalsupplyView(APIView):
    """View total supply"""
    web3 = Web3(Web3.HTTPProvider(url=env('INFURA_URL')))
    contract = web3.eth.contract(address=env('ADDRESS'), abi=env('ABI'))
    totalSupply = contract.functions.totalSupply().call()
