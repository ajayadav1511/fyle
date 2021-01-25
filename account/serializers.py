from rest_framework import serializers
from .models import *
from rest_framework.serializers import HyperlinkedModelSerializer


class BankNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=banks
        fields=('name')


class BranchDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank_branches
        fields = '__all__'
