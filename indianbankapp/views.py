from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        city = request.GET.get("city", None)
        bank_name = request.GET.get("bank_name", None)
        if city is None and bank_name is None:
            return Response({'error_message': "Please enter both Bank and City."}, status=status.HTTP_404_NOT_FOUND)
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
