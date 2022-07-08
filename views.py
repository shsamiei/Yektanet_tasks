from Advertisement.models import Ad, Advertiser, View, Click
from Advertisement.serializer import AdSerializer, AdvertiserSerializer, ViewSerializer, ClickSerializer
from rest_framework import viewsets


class AdvertiserViewSet(viewsets.ModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer


class AdViewSet(viewsets.ModelViewSet):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class ViewViewSet(viewsets.ModelViewSet):

    queryset = View.objects.all()
    serializer_class = ViewSerializer


class ClickViewSet(viewsets.ModelViewSet):

    queryset = Click.objects.all()
    serializer_class = ClickSerializer

































# class AdvertiserList(generics.ListCreateAPIView):
#
#     queryset = Advertiser.objects.all()
#     serializer_class = AdvertiserSerializer
#
#     def get(self, request, *args, **kwargs):
#         [[ad.add_view() for ad in advertiser.ads.all()] for advertiser in self.get_queryset()]
#         return super(AdvertiserList, self).get(request, *args, **kwargs)
#
#
# class AdvertiserDetail(generics.RetrieveUpdateDestroyAPIView):
#         queryset = Advertiser.objects.all()
#         serializer_class = AdvertiserSerializer
#



# class AdvertiserList(APIView):
#     def get(self, request):
#         advertisers = Advertiser.objects.all()
#         serialiazer = AdvertiserSerializer(advertisers, many=True)
#         return Response(serialiazer.data)
#
#     def post(self, request):
#         serializer = AdvertiserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class AdvertiserDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Advertiser.objects.get(pk=pk)
#         except Advertiser.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         advertiser = self.get_object(pk)
#         serializer = AdvertiserSerializer(advertiser)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         advertiser = self.get_object(pk)
#         serializer = AdvertiserSerializer(advertiser, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#     def delete(self, request, pk):
#         advertiser = self.get_object(pk)
#         advertiser.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

