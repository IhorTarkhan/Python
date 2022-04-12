from django.urls import path

from src.lab6.main import views

urlpatterns = [
    path('', views.polygons),
    path('vertexes/<int:polygon_id>', views.vertexes),
]
