from django.shortcuts import render
from api_app.serializers import *
from api_app.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET",'POST'])
def product_view(req):
    if req.method == "GET":
        product_data=ProductModel.objects.all()
        serializers=ProductSerializer(product_data, many=True)
        return Response({
            'success': True,
            'message':"Data get Successfully",
            'data':serializers.data
        })

    if req.method == "POST":
        serializers=ProductSerializer(data=req.data)
        if serializers.is_valid():
            serializers.save()
            return Response({
                'success': True,
                'message':"Product get Successfully",
                'data':serializers.data
            })
        
@api_view(["GET",'PUT',"DELETE"])
def product_details(req,id):
    if req.method=="GET":
        try:
            data=ProductModel.objects.get(id=id)
        except:
            return Response({
                'success': False,
                'message':"Product Data NotFourd",
                'data':[]
            }, status=status.HTTP_404_NOT_FOUND)

        serializers_data=ProductSerializer(data)
        return Response({
                'success': True,
                'message':"Single Product get Successfully",
                'data':serializers_data.data
            }, status=status.HTTP_200_OK)

    if req.method =="DELETE":
        # try:
        #     data=ProductModel.objects.get(id=id)
        # except:
        #     return Response({
        #         'success': False,                                @ata dite hbe na         
        #         'message':"Product Data NotFourd",
        #         'data':[]
        #     }, status=status.HTTP_404_NOT_FOUND)   

        data.delete()     
        return Response({
                'success': True,
                'message':" Product Deleted Successfully",
                'data':[]
            }, status=status.HTTP_200_OK)

    if req.method == "PUT":
        serializers_data=ProductSerializer(data, data=req. data)
        if serializers_data.is_valid():
            serializers_data.save()
            return Response({
                            'success': True,
                            'message':" Product Update Successfully",
                            'data':serializers_data.data
                        }, status=status.HTTP_201_CREATED)
        else:
            return Response({
            'success': False,
            'message':serializers_data.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        