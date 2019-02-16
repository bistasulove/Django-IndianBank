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
            return Response({'error_message': "Sorry. No Branch with such IFSC code exists."},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = BranchesSerializer(branch).data
        return Response(serializer)


class BranchCityView(APIView):

    def get(self, request):

        """ Finds all the branches of a Bank in a given City """
        city = request.GET.get("city", False)
        bank_name = request.GET.get("bank_name", False)
        if not city and not bank_name:
            city="na"
            bank_name = "na"
            return Response({'error_message': "Please enter both Bank and City."}, status=status.HTTP_404_NOT_FOUND)
        elif not bank_name:
            bank_name = "na"
            return Response({'error_message':"Please enter Bank Name."}, status=status.HTTP_404_NOT_FOUND)
        elif not city:
            city = "na"
            return Response({'error_message':"Please enter City Name."}, status=status.HTTP_404_NOT_FOUND)
        else:
            bank = Banks.objects.filter(name=bank_name.upper()).first()
            if bank is None:
                return Response({'error_message': "{} doesn't exists!".format(bank_name.upper())},
                                status=status.HTTP_404_NOT_FOUND)
            branches = Branches.objects.filter(city=city.upper(), bank=bank)
            if len(branches) < 1:
                return Response({'error_message': "There are no branches of {} in {}.".format(bank_name, city)},
                                status=status.HTTP_404_NOT_FOUND)
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