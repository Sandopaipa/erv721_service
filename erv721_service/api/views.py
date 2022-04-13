from django.shortcuts import render

from django.db import models

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Token

from .serializers import TokenListSerializer
from .serializers import TokenCreateSerializer
from .serializers import TokenTotalsupplySerializer


class TokenCreateView(APIView):
    pass

class TokenListView(APIView):
    pass

class TokenTotalsupplyView(APIView):
    pass
