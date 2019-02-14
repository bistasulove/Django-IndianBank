from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer
from rest_framework import permissions


@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'banks': reverse('bank-list',request=request, format=format),
        'branches': reverse('branch-list', request=request, format=format)
    })

class BankList(generics.ListCreateAPIView):
    """List all the Banks or create new Bank"""

    queryset = Banks.objects.all()
    serializer_class = BanksSerializer



class BankDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update or Delete a Bank"""

    queryset = Banks.objects.all()
    serializer_class = BanksSerializer

class BranchList(generics.ListCreateAPIView):
    """List all the branches or create new Branch"""

    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update or Delete a Bank"""

    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer