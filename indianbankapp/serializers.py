from rest_framework import serializers
from . import models


class BanksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Banks
        fields = ('id','url', 'name')


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Branches
        fields = ('url','ifsc', 'bank', 'branch', 'address', 'city', 'district', 'state')
