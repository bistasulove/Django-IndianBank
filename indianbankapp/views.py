from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer


@csrf_exempt
def bank_list(request):
    """List all the Banks or create new Bank"""

    if request.method == 'GET':
        banks = Banks.objects.all()
        serializer = BanksSerializer(banks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BanksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)


@csrf_exempt
def bank_detail(request, pk):
    """Retrieve, Update or Delete a Bank"""
    try:
        bank = Banks.objects.get(pk=pk)
    except Banks.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BanksSerializer(bank)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BanksSerializer(bank, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        bank.delete()
        return HttpResponse(status=204)
