from rest_framework import serializers
from goods.models import Goods,GoodsCategory


# class GoodsSerializer(serializers.Serializer):
#     name=serializers.CharField(required=True,max_length=100)
#     click_num=serializers.IntegerField(default=0)
#     goods_front_image=serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Goods` instance, given the validated data.
#         """
#          Goods.objects.create(**validated_data)return
class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Goods
        # fields=('name','click_num','market_price','add_time')
        fields="__all__"


class GoodsCategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    class Meta:
        model=GoodsCategory
        fields="__all__"

