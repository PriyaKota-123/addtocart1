from django.urls import path
from .views import *
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('1/',AboutView.as_view(),name='about'),
    path('2/',ContactView.as_view(),name='contact'),
    path('add-to-cart-<int:pro_id>/',AddToCartView.as_view(),name='addtocart'),
    path('3/',MyCartView.as_view(),name='mycart'),
    path('4/<int:id>/',DeleteView.as_view(),name='delete')

]