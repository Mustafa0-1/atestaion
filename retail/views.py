from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from retail.filter import RetailCountryFilter
from retail.models import Retail
from retail.serializers import RetailCreateSerializer, RetailUpdateSerializer, RetailSerializer


class RetailViewSet(ModelViewSet):
    queryset = Retail.objects.all()
    filterset_class = RetailCountryFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return RetailCreateSerializer
        elif self.action == 'update':
            return RetailUpdateSerializer
        else:
            return RetailSerializer
