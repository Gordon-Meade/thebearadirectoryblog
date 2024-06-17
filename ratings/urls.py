
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.rate_area_list, name='rate_area_list'),
    path('rate/<int:area_id>/', views.rate_area, name='rate_area'),
    path('area/<int:area_id>/', views.area_detail, name='area_detail'),
]
