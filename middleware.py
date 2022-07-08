from Advertisement.models import Ad, View, Click
from django.utils import timezone


class Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view_click(self, request,  ad_kwargs):
        if request.path == '/advertiser/':
            self.viewInc(request)
        if '/advertiser/click' in request.path:
            self.clickInc(request, ad_kwargs)

    @staticmethod
    def viewInc():
        for ad in Ad.objects.filter(approve=True):
            v = View()
            v.ad = ad
            v.viewed_time = timezone.now()
            v.save()

    @staticmethod
    def clickInc(kwargs):
        c = Click()
        # c.ad = Ad.objects.get(pk=kwargs['ad_id'])
        ad = Ad.objects.get(pk=kwargs)
        c.ad = ad
        c.clicked_time = timezone.now()
        c.save()
