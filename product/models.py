from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        db_table = 'categories'


class ColorModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Код')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Цвета'
        verbose_name = 'Цвет'
        db_table = 'colors'


class Attribute(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='attributes',
                                 verbose_name='Категорие')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'attributes'
        verbose_name = 'Аттрибут'
        verbose_name_plural = 'Аттрибуты'


class ProductModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    is_recommended = models.BooleanField(default=False, verbose_name='Бест селлер?')
    color = models.ForeignKey(
        ColorModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name='Цвет'
    )
    attribute = models.ForeignKey(
        Attribute,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products',
        verbose_name='Атрибут'
    )
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        db_table = 'products'


class ProductImageModel(BaseModel):
    image = models.ImageField(upload_to='products', verbose_name='Изображение')
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Товар'
    )

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = 'Изображения'
        verbose_name = 'Изображение'
        db_table = 'products_images'
