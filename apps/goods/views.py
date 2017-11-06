from django.shortcuts import render

# Create your views here.
from .models import Goods
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class GoodsListView(APIView):
    """
    List all goods, or create a new goods.
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializers = GoodsSerializer(goods, many=True)
        return Response(goods_serializers.data)

    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)