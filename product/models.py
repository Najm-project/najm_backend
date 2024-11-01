from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(verbose_name='slug', max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_name = unidecode(self.name)
            self.slug = slugify(transliterated_name)

            while CategoryModel.objects.filter(slug=self.slug).exists():
                slug = CategoryModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        db_table = 'categories'


class ProductModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    is_recommended = models.BooleanField(default=False, verbose_name='Бест селлер?')
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория'
    )
    slug = models.SlugField(verbose_name='slug', max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_name = unidecode(self.name)
            self.slug = slugify(transliterated_name)

            while ProductModel.objects.filter(slug=self.slug).exists():
                slug = ProductModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        db_table = 'products'


class ColorModel(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='colors',
        verbose_name='Товар'
    )
    product_image_id = models.CharField(max_length=100, verbose_name='ID фото продукта с таким цветом')
    slug = models.SlugField(verbose_name='slug', max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_name = unidecode(self.name)
            self.slug = slugify(transliterated_name)

            while ColorModel.objects.filter(slug=self.slug).exists():
                slug = ColorModel.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Цвета'
        verbose_name = 'Цвет'
        db_table = 'colors'


class AttributeCategory(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='attribute_cats',
        verbose_name='Товар'
    )
    slug = models.SlugField(verbose_name='slug', max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_name = unidecode(self.name)
            self.slug = slugify(transliterated_name)

            while AttributeCategory.objects.filter(slug=self.slug).exists():
                slug = AttributeCategory.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'attribute_cats'
        verbose_name = 'Категория Параметров'
        verbose_name_plural = 'Категории Параметров'


class Attribute(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Название')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии?')
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name='attributes',
        verbose_name='Товар'
    )
    product_image_id = models.CharField(max_length=100, verbose_name='ID фото продукта с таким параметром')
    attribute_category = models.ForeignKey(
        AttributeCategory,
        on_delete=models.CASCADE,
        related_name='attributes',
        verbose_name='Категория'
    )
    slug = models.SlugField(verbose_name='slug', max_length=130, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            transliterated_name = unidecode(self.name)
            self.slug = slugify(transliterated_name)

            while Attribute.objects.filter(slug=self.slug).exists():
                slug = Attribute.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.name:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'attributes'
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'


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