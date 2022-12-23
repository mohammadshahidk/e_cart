from django.db import models
from django.db.models import Sum

from accounts.models import ProjectUser
from accounts.models import get_file_path


class Product(models.Model):
    """
    Model to store product details.

    Attribs:-
       name(char): name od the product.
       brand(char): brand name of the product.
       price(float): amount of the product.
       description(txt): description for the product.
       image(img): image of the product.
    """
    name = models.CharField(default='', max_length=200, null=True, blank=True)
    brand = models.CharField(default='', max_length=200, null=True, blank=True)
    price = models.FloatField(default=0.0, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    image = models.ImageField(
        upload_to=get_file_path, default=None, null=True, blank=True)

    def __str__(self):
        """object name in django admin."""

        return f'{self.id}: {self.name}: {self.brand}'


class Cart(models.Model):
    """
    Model to store the cart items
    """
    user = models.ForeignKey(
        ProjectUser, default=None, null=True, blank=True, on_delete=models.CASCADE)
    total = models.FloatField(default=0.0, null=True, blank=True)

    @property
    def grand_total(self):
        """Get total amount ot cart"""
        total = sum(item.sub_total for item in self.items.all())
        return total



class CartItem(models.Model):
    """
    Model to store cart items.

    Attribs:-
      product(obj): product in the cart.
      quantity(int): product quantity in the cart

    """
    cart = models.ForeignKey(
        Cart, default=None, null=True, blank=True, on_delete=models.CASCADE,
        related_name='items')
    product = models.ForeignKey(
        Product, default=None, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def sub_total(self):
        """Get cart total amount"""
        return self.product.price * self.quantity





