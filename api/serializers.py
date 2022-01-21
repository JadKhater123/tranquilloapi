from rest_framework.serializers import ModelSerializer
from .models import Goal, Journal, Profile, Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
    
class GoalSerializer(ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'
    
class JournalSerializer(ModelSerializer):
    class Meta:
        model = Journal
        fields = '__all__'