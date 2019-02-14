from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer


@api_view(['GET', 'POST'])
def bank_list(request):
    """List all the Banks or create new Bank"""

    if request.method == 'GET':
        banks = Banks.objects.all()
        serializer = BanksSerializer(banks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BanksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def bank_detail(request, pk):
    """Retrieve, Update or Delete a Bank"""
    try:
        bank = Banks.objects.get(pk=pk)
    except Banks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BanksSerializer(bank)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BanksSerializer(bank, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bank.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
