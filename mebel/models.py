from django.db import models

class OneModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nomi')
    image = models.ImageField(upload_to='products/', verbose_name='Rasmi')

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    product = models.ForeignKey(OneModel, on_delete=models.CASCADE, verbose_name='Mahsulot', related_name='one_models')
    name = models.CharField(max_length=255, verbose_name='Nomi')
    brand = models.CharField(max_length=255, verbose_name='Kim tomonidan')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    image = models.ImageField(upload_to='products/', verbose_name='Rasmi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Products'
        managed = True
        verbose_name = 'Mahsulotlar'
        verbose_name_plural = 'Mahsulotlar'


# class OneModel(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Nomi')
#     image = models.ImageField(upload_to='one_models/', verbose_name='Rasmi')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

#     def __str__(self):
#         return self.name

# class Meta:
#         db_table = 'one_models'
#         verbose_name = 'Yagona model'
#         verbose_name_plural = 'Yagona modelllar'
