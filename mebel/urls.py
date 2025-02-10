from django.urls import path
from .views import  HomeView, AboutView, CategoryView, ProductView, ProfileView,search_products

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('category/', CategoryView.as_view(), name='category_page'),
    path('product/', ProductView.as_view(), name='product_page'),
    path('profile/', ProfileView.as_view(), name='profile_page'),
    path('search/', search_products, name='search_products'),  # Qidiruv uchun URL
]
