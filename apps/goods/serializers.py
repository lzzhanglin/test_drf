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
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsCategory
        fields="__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Goods
        # fields=('name','click_num','market_price','add_time')
        fields="__all__"