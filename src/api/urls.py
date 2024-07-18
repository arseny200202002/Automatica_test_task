from django.urls import path

from . import views


urlpatterns = [
    path('shop/list', views.ShopListApiView.as_view()),
    path('visit/create', views.CreateVisitApiView.as_view()),
]