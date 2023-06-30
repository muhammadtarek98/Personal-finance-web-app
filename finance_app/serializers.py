from rest_framework import serializers
from .models import SavingGoal


class SavingGoalSerializer(serializers.ModelSerializer):
    monthly_deposit = serializers.SerializerMethodField()

    def get_monthly_deposit(self, obj):
        return obj.calculate_monthly_deposit()

    class Meta:
        model = SavingGoal
        fields = ('id', 'total_amount', 'goal_date', 'monthly_deposit')
