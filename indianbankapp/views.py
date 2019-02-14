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
