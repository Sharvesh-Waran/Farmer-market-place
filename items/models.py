from django.db import models
from django.contrib.auth.models import User
from core.models import UserProfile

from django.core.exceptions import ValidationError

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name

class Transaction(models.Model):
    name=models.ForeignKey(Product, related_name="transactions", on_delete=models.CASCADE)
    price=models.DecimalField(decimal_places=2, max_digits=6)
    quantity=models.IntegerField()
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    is_sold=models.BooleanField(default=False)
    sold_at = models.DateTimeField(blank=True, null=True)
    sold_to = models.ForeignKey(User, related_name='items_bought', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.quantity} @ {self.price}"
    
    def save(self, *args, **kwargs):
        # Check if the user has the role 'Farmer'
        user_profile = UserProfile.objects.filter(user=self.created_by).first()
        if user_profile is None or user_profile.role.name != "Farmer":
            raise ValidationError("Only users with the 'Farmer' role can create transactions.")

        # Proceed with saving the instance if the role is valid
        super().save(*args, **kwargs)
