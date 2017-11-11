from django.shortcuts import render

# Create your views here.
from .models import Goods,GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters

class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = "page_size"
    page_query_param = 'page'
    max_page_size = 100

# class GoodsListView(APIView):
#     """
#     List all goods, or create a new goods.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializers = GoodsSerializer(goods, many=True)
#         return Response(goods_serializers.data)


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
   商品列表页 分页 过滤 搜索 排序
    """
    queryset=Goods.objects.all()
    serializer_class=GoodsSerializer
    pagination_class = GoodsPagination
    authentication_classes =(TokenAuthentication,)
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields=('sold_num', 'shop_price')
    # filter_fields=('name','shop_price')
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, format=None):
    #     serializer = GoodsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    商品分类列表数据
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer