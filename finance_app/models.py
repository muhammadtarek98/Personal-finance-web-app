from django.db import models
import datetime


# Create your models here.

class SavingGoal(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_date = models.DateField()

    def calculate_monthly_deposit(self):
        current_date = datetime.date.today()
        num_months = (self.goal_date.year - current_date.year) * 12 + (self.goal_date.month - current_date.month)
        monthly_deposit = self.total_amount / num_months

        return round(monthly_deposit, 2)
