from rest_framework import generics
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer


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