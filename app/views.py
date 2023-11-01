from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
#from . serializer import *
from rest_framework.response import Response

class LegaleaseView(APIView):
    def get(self, request):
        output  = [{"prompt": output.prompt, "result": output.result} for output in Legalease.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = LegaleaseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

