from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

import json
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer


def index(request):
    return render(request, "indianbankapp/index.html")


class BranchIfscView(APIView):

    def get(self, request, ifsc_code):
        """ Finds the Bank's branch by IFSC code"""
        branch = Branches.objects.filter(ifsc=ifsc_code.upper()).first()
        if branch is None:
            pass
        serializer = BranchesSerializer(branch).data
        return Response(serializer)


class BranchCityView(APIView):

    def get(self, request):

        """ Finds all the branches of a Bank in a given City """
        city = request.GET.get("city")
        bank_name = request.GET.get("bank_name")
        bank = Banks.objects.filter(name=bank_name.upper()).first()
        branches = Branches.objects.filter(city=city.upper(), bank=bank)
        if len(branches) < 1:
            pass
        serializer = BranchesSerializer(branches, many=True).data
        return Response(serializer)


@api_view(["GET"])
def getbankslist(request):
    banks = Banks.objects.filter(name__icontains=request.GET.get("term", ""))[:10]
    bank_name_list = []
    for bank in banks:
        bank_name_list.append(bank.name)
    return HttpResponse(json.dumps(bank_name_list))


@api_view(["GET"])
def getcitylist(request):
    branches = Branches.objects.filter(city__icontains=request.GET.get("term", ""))[:1]
    branch_city_list = []
    for branch in branches:
        branch_city_list.append(branch.city)

    return HttpResponse(json.dumps(branch_city_list))
