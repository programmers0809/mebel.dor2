from django.shortcuts import render

from django.views import View

from .models import ProductModel,OneModel


class HomeView(View):
    def get(self, request):
        products_list = ProductModel.objects.all()
        One_list = OneModel.objects.all()
        
        context = {
            'products_list' : products_list,
             'One_list' :One_list

        }
        return render(request, 'home.html', context=context)
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class CategoryView(View):
    def get(self, request):
        return render(request, 'category.html')
    
class ProductView(View):
    def get(self, request):
        return render(request, 'productpage.html')
    
class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')
    


def search_products(request):
    query = request.GET.get('q')  # Qidiruv so'zi
    if query:
        products = ProductModel.objects.filter(name__icontains=query)  # Mahsulot nomida qidirish
    else:
        products = ProductModel.objects.all()  # Hech narsa qidirilmasa, barcha mahsulotlarni olish
    return render(request, 'your_template.html', {'products': products})
