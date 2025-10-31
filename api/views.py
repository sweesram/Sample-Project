from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person={'name':'swees','age':13}
    return Response(person)

@api_view(['POST'])
def postData(request):
    data=request.data 
    
    response_data={
        "message":"Welcome to our team",
        "print-data":data
    }
    return Response(response_data,status=201)