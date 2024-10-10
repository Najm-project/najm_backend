from django.db import models
from product.models import BaseModel, ProductModel
from user.models import User


class CartItem(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Пользователь')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    color = models.CharField(max_length=255, null=True, blank=True, verbose_name="Цвет")
    attributes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'

    class Meta:
        verbose_name_plural = 'Корзина'
        verbose_name = 'Корзина'
        db_table = 'cart_items'


class OrderModel(BaseModel):
    DELIVERY_CHOICES = [
        ('pickup', 'Cамовывоз'),
        ('delivery', 'Доставка'),
    ]
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='cart_items', verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    color = models.CharField(max_length=255, null=True, blank=True, verbose_name="Цвет")
    attributes = models.TextField(null=True, blank=True)
    delivery_type = models.CharField(max_length=10, choices=DELIVERY_CHOICES, verbose_name='Delivery Type')
    first_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Last Name')
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name='Phone Number')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.product.name}"

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        db_table = 'orders'


class FavoriteItem(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_items', verbose_name='Пользователь')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='favorite_items',
                                verbose_name='Товар')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name_plural = 'Избранные'
        verbose_name = 'Избранное'
        db_table = 'favorite_items'


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', verbose_name='Пользователь')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='reviews', verbose_name='Товар')
    rating = models.PositiveIntegerField(verbose_name='Рейтинг', default=1)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'Отзыв на {self.product.name} от {self.user.username}'

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        db_table = 'reviews'
