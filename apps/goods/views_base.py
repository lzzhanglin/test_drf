from django.views.generic.base import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        goods=Goods.objects.all()[:10]
        json_list=[]


        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict=model_to_dict(good)
        #     json_list.append(json_dict)
        from django.core import serializers
        import  json
        json_data=serializers.serialize('json',goods)
        json_data=json.loads(json_data)
        from django.http import HttpResponse,JsonResponse

        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(json_data,safe=False)