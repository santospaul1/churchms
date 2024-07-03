from django.db import models
from members.models import Member

class Donation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE,default=None, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member} - {self.amount} on {self.date}"
class Spending(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.amount} on {self.date}"