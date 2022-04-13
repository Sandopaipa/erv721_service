from django.urls import path

from . import views

import include

urlpatterns = [
    path('api/v1/tokens/create', views.TokenCreateView.as_view()),
    path('api/v1/tokens/list', views.TokenListView.as_view()),
    path('api/v1/tokens/total_supply', views.TokenTotalsupplyView.as_view()),

]