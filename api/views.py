import profile
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

import api
from .serializers import GoalSerializer, JournalSerializer, ProfileSerializer, TaskSerializer
from .models import Goal, Journal, Profile, Task

@api_view(['GET'])

def getRoutes(request):
    routes = [
        {
            'Endpoint': '/tasks/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns and Array of Notes'
        },
        {
            'Endpoint': '/tasks/id/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/tasks/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates Note'
        },
        {
            'Endpoint': '/tasks/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates Note'
        },
        {
            'Endpoint': '/tasks/id/delete',
            'method': 'GET',
            'body': 'none',
            'description': 'Deletes Note'
        },
        {
            'Endpoint': '/profiles/',
            'method': 'GET',
            'body': 'none',
            'description': 'returns an array of profiles',
        },
        {
            'Endpoint': '/profiles/id/',
            'method': 'GET',
            'body': "none",
            'description': 'returns a single profile object',
        },
        {
            'Endpoint': '/profiles/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'creates profile',
        },
        {
            'Endpoint': '/profiles/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'updates profile',
        },
        {
            'Endpoint': '/profiles/id/delete/',
            'method': 'DELETE',
            'body': 'none',
            'description': 'deletes profile',
        },
        {
            'Endpoint': '/journals/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns and Array of Notes'
        },
        {
            'Endpoint': '/journals/id/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/journals/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates Note'
        },
        {
            'Endpoint': '/journals/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates Note'
        },
        {
            'Endpoint': '/journals/id/delete',
            'method': 'GET',
            'body': 'none',
            'description': 'Deletes Note'
        },     
        {
            'Endpoint': '/goals/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns and Array of Notes'
        },
        {
            'Endpoint': '/goals/id/',
            'method': 'GET',
            'body': 'none',
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/goals/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates Note'
        },
        {
            'Endpoint': '/goals/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates Note'
        },
        {
            'Endpoint': '/goals/id/delete',
            'method': 'GET',
            'body': 'none',
            'description': 'Deletes Note'
        },
    ]
# Create your views here.
    return Response(routes)


@api_view(['GET'])
def getTasks (request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getTask (request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    data = request.data 
    task = Task.objects.create(
        body=data['body'],
        title=data['title']
    )
    serializer = TaskSerializer(task, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data 
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Note was deleted.')

#
# Profile
#

@api_view(['GET'])
def getProfiles (request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile (request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createProfile(request):
    data = request.data 
    profile = Profile.objects.create(
        body=data['body']
    )
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateProfile(request, pk):
    data = request.data 
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return Response('Note was deleted.')

#
# Goal
#

@api_view(['GET'])
def getGoals (request):
    goal = Goal.objects.all()
    serializer = GoalSerializer(goal, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getGoal (request, pk):
    goal = Goal.objects.get(id=pk)
    serializer = GoalSerializer(goal, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createGoal(request):
    data = request.data 
    goal = Goal.objects.create(
        body=data['body']
    )
    serializer = GoalSerializer(goal, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateGoal(request, pk):
    data = request.data 
    goal = Goal.objects.get(id=pk)
    serializer = GoalSerializer(goal, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteGoal(request, pk):
    goal = Goal.objects.get(id=pk)
    goal.delete()
    return Response('Note was deleted.')

#
# Journal
#

@api_view(['GET'])
def getJournals (request):
    journals = Journal.objects.all()
    serializer = JournalSerializer(journals, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getJournal (request, pk):
    journal = Journal.objects.get(id=pk)
    serializer = JournalSerializer(journal, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def createJournal(request):
    data = request.data 
    journal = Journal.objects.create(
        body=data['body']
    )
    serializer = JournalSerializer(journal, many = False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data 
    journal = Journal.objects.get(id=pk)
    serializer = JournalSerializer(journal, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteJournal(request, pk):
    journal = Journal.objects.get(id=pk)
    journal.delete()
    return Response('Note was deleted.')

