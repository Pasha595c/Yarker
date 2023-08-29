from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("category/<slug:slug>/", views.category_detail, name="category_detail"),
]
