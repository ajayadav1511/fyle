from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, status, generics
from rest_framework.generics import * 
from .serializers import *
from .models import *
from rest_framework.response import Response
import requests
import json
class BranchView(generics.ListCreateAPIView):
    
    serializer_class = BranchDetailsSerializer
    queryset = bank_branches.objects.all()
    def list(self, request):
        try:
            offset = int(self.request.GET.get('offset'))
            limit = int(self.request.GET.get('limit'))
            branch = self.request.GET.get('q').upper()
        except:
            offset, limit, branch = 0, 10, "BANGALORE" #Default
        queryset = bank_branches.objects.filter(branch=branch).order_by('ifsc')[offset:limit]
        serializer = BranchDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


class BranchViewAuto(generics.ListCreateAPIView):

    serializer_class = BranchDetailsSerializer
    queryset = bank_branches.objects.all()

    def list(self, request):
        offset, limit, = 0, 10
        try:
            offset = int(self.request.GET.get('offset'))
            limit = int(self.request.GET.get('limit'))
            branch = self.request.GET.get('q').upper()
        except:
            offset, limit, branch = 0, 10, "BANGALORE"
        queryset = bank_branches.objects.filter(branch__startswith=branch).order_by('ifsc')[offset:limit]
        serializer = BranchDetailsSerializer(queryset, many=True)
        return Response(serializer.data)


def home(request):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
    }
    
    API_ENDPOINT = 'https://credicxoo.herokuapp.com/api/branches/?q=BANGALORE&offset=0&limit=3'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    data = r.json()
    return render(request, "account/index.html", {'data':data})
