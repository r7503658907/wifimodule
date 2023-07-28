from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
import requests


class postwifi(APIView):
    def post(self, request):
        try:
            serializer = wifiModeSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.data["user"]
                wifiMode.objects.create(
                    **serializer.data
                )
               
                return JsonResponse({
                        'status': 200,
                        'message': 'Create  Successfully',
                        })
            return JsonResponse(
                {
                    "status" : 400,
                    "error" : serializer.errors
                }
            )
        except Exception as e:
            return JsonResponse({
             'status' : 400,
             'message': 'Something Went Wrong',
              "error " : str(e)
            })



class getwifi(APIView):
    def get(self,request):
        try:
            courseCategoryData = list(wifiMode.objects.filter().values())
            print(courseCategoryData)
            return JsonResponse({
            'status': 200,
            'message': 'all Details ',
            'data' : courseCategoryData
            })
        except Exception as e:
            return JsonResponse({
                'status': 200,
                'message': 'Something Went Wrong',
                'error': str(e)
            })