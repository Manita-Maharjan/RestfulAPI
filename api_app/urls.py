from django.urls import path
from .views import ProductListCreateView, ProductRetrieveUpdateDestroyView


urlpatterns = [
    path('addproduct/', ProductListCreateView.as_view(), name = "productlistcreate" ),
    path('addproduct/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name = "productretrieveupdatedestroy")
]
