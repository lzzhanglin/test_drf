import django_filters
from django.db.models import Q
from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    # contains前面加一个i可以忽略大小写
    top_category = django_filters.NumberFilter(method="top_category_filter")
    def top_category_filter(self,queryset,name,value):
        queryset=queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|
                                 Q(category__parent_category__parent_category_id=value))


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']