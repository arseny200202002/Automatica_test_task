from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .authentication import PhoneAuthentication
from .models import (
    Shop,
    Visit,
    Employee
)
from .serializers import (
    ShopListSerializer,
    VisitSerializer,
    CreateVisitSerializer,
)



class ShopListApiView(APIView):
    http_method_names = ['get']

    @extend_schema(
        responses={
            status.HTTP_200_OK: ShopListSerializer, 
        },
        description="Метод для получения списка магазинов по номеру телефона"
    )
    def get(self, request):
        employee = request.user
        shops: list[Shop] = get_list_or_404(Shop, employee=employee)

        serialised_shops = []
        for shop in shops:
            serialised_shops.append({
                'shop_id': shop.pk,
                'name': shop.name
            })
        return Response(data={'shops':serialised_shops}, status=status.HTTP_200_OK)


class CreateVisitApiView(APIView):
    http_method_names = ['post']

    @extend_schema(
        request=CreateVisitSerializer,
        responses={
            status.HTTP_200_OK: VisitSerializer, 
        },
        description="Метод для получения списка магазинов по номеру телефона"
    )
    def post(self, request):
        employee = request.user
        serializer = CreateVisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        shop = get_object_or_404(Shop, pk=serializer.validated_data.pop('shop_id'))
        visit = Visit(shop=shop, employee=employee, **serializer.validated_data)
        visit.save()
        return Response(
            data=VisitSerializer(instance=visit).data, 
            status=status.HTTP_201_CREATED
        )

        
