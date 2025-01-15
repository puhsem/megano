from django.db import models


class Review(models.Model):
    """Модель для хранения отзывов"""

    author = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    text = models.TextField()
    rate = models.PositiveSmallIntegerField()
    date = models.CharField(max_length=16)


class Specification(models.Model):
    """Модель для хранения спецификация"""

    name = models.CharField(max_length=32)
    value = models.CharField(max_length=32)


class ProductShort(models.Model):
    """Модель для хранения продуктов"""

    category = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    date = models.CharField(max_length=64)
    title = models.CharField(max_length=16)
    description = models.CharField(max_length=128)
    freeDelivery = models.BooleanField(default=False)
    reviews = models.PositiveSmallIntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1)


class ProductImage(models.Model):
    """Модель для хранения изображения товара"""

    src = models.ImageField(
        upload_to="images/product_images/",
        default="images/default.jpg",
        verbose_name="Ссылка",
    )
    alt = models.CharField(max_length=128, blank=True, null=True, verbose_name="Описание")
    product = models.ForeignKey(ProductShort, related_name='images', on_delete=models.CASCADE)


class ProductTag(models.Model):
    """Модель для хранения тэгов"""

    name = models.CharField(max_length=128)
    product = models.ForeignKey(ProductShort, related_name='tags', on_delete=models.CASCADE)


# class Catalog(models.Model):
#     """Модель для хранения категорий"""
#
#     title = models.CharField(max_length=64)
#     subcategories = models.ForeignKey('self', blank=True, symmetrical=False, on_delete=models.PROTECT)
#     catalog = models.ForeignKey(Catalog, related_name='images', on_delete=models.CASCADE)

#
#
# class CatalogImage(models.Model):
#     """Модель для хранения изображения товара для каталога"""
#
#     src = models.ImageField(
#         upload_to="images/catalog_images/",
#         default="images/default.jpg",
#         verbose_name="Ссылка",
#     )
#     alt = models.CharField(max_length=128, blank=True, null=True, verbose_name="Описание")
#