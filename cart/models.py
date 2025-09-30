from django.db import models
from store.models import Product
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db.models import Sum, F

class CartItemManager(models.Manager):
    def grand_total(self, user):
        if(user.is_anonymous):
            return 0
        return self.filter(user=user).aggregate(
            total=Sum(F("quantity") * F("product__price"))
        )["total"] or 0
    
    def get_total_items(self, user):
        return sum(item.quantity for item in self.filter(user=user))





class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    class Meta:
        unique_together = ('user', 'product')


    objects = CartItemManager()

    def subtotal(self):
        return self.product.price * self.quantity
    
    

    

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for {self.user}"