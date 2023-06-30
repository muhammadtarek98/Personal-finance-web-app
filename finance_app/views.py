from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import SavingGoal
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SavingGoalSerializer


class SavingGoalViewSet(viewsets.ModelViewSet):
    queryset = SavingGoal.objects.all()
    serializer_class = SavingGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Calculate monthly deposit value based on total amount and goal date
        total_amount = serializer.validated_data['total_amount']
        goal_date = serializer.validated_data['goal_date']
        monthly_deposit = total_amount / goal_date.month

        # Save the saving goal with the calculated monthly deposit value
        saving_goal = serializer.save(user=request.user, monthly_deposit=monthly_deposit)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class SavingGoalViewSet(viewsets.ModelViewSet):
    queryset = SavingGoal.objects.all()
    serializer_class = SavingGoalSerializer


@api_view(['GET', 'POST'])
def saving_goal_list(request):
    if request.method == 'GET':
        saving_goals = SavingGoal.objects.all()
        serializer = SavingGoalSerializer(saving_goals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SavingGoalSerializer(data=request.data)
        if serializer.is_valid():
            total_amount = serializer.validated_data['total_amount']
            goal_date = serializer.validated_data['goal_date']
            monthly_deposit = total_amount / goal_date.month

            saving_goal = serializer.save(monthly_deposit=monthly_deposit)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def create_saving_goal(request):
    return render(request,
                  template_name=r'E:\programming practices\pythons\meta course\backend_assessment\templates\create saving goal.html')
