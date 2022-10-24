from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import (
    Bank,
    Location,
    Waybill,
    Category,
    Product,
)
from .serializers import (
    BankSerializer,
    LocationSerializer,
    WaybillSerializer,
    CategorySerializer,
    ProductSerializer,
    WaybillDateSerializer,
)

import django_filters


class FixtureFilter(django_filters.FilterSet):
    date = django_filters.DateFilter('created_at', lookup_expr='exact')

    class Meta:
        model = Waybill
        fields = ['created_at']


class BankViewSet(ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class WaybillViewSet(ModelViewSet):
    queryset = Waybill.objects.all()
    serializer_class = WaybillSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = FixtureFilter


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class GetListWaybillByDate(generics.ListAPIView):
    serializer_class = WaybillSerializer
    queryset = Waybill.objects.all()

    def get_queryset(self):
        date = self.request.GET.get('date')
        return Waybill.objects.filter(created_at__gt=date).order_by("-price")


class GetCoastsWaybill(generics.ListAPIView):
    serializer_class = WaybillSerializer
    queryset = Waybill.objects.all()

    def get_queryset(self):
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        product_id = self.request.GET.get('product_id')

        return Waybill.objects.filter(Q(created_at__gt=date_from) & Q(created_at__lt=date_to) & Q(product=product_id))
