from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models


class BanksView(viewsets.ModelViewSet):
    queryset = models.Banks.objects.all()
    serializer_class = serializers.BanksSerializer


class BranchesView(viewsets.ModelViewSet):
    queryset = models.Branches.objects.all()
    serializer_class = serializers.BranchesSerializer