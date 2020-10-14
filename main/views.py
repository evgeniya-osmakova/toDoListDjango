from django.shortcuts import render
from ./models import Task
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def get_tasks(request):
    print(request)
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_json = serializers.serialize('json', tasks)
        return HttpResponse(tasks_json, content_type='application/json')
    elif request.method == 'POST':
        new_task = JSONParser().parse(request)
        task = Task(task = new_task)
        task.save()
        task_json = serializers.serialize('json', task)
        return HttpResponse(task_json, content_type='application/json')


# @api_view(['POST'])
# def add_task(request):
#     new_task = JSONParser().parse(request)
#     # task = request.query_params.get('task', None)
#     task = Task(task = new_task)
#     if task.is_valid():
#         task.save()
#         return JsonResponse(task.data, status=status.HTTP_201_CREATED) 
#     return JsonResponse(task.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def change_task(request, id):
    if request.method == 'PUT':
        new_task = JSONParser().parse(request)
        task = Task.objects.get(id=id) 
        changed_task = Task(task, task=new_task)
        changed_task_json = serializers.serialize('json', changed_task)
        changed_task.save()
        return HttpResponse(changed_task_json, content_type='application/json')
    elif request.method == 'DELETE':
        task_to_delete = Task.objects.get(id=id) 
        tasks_to_delete_json = serializers.serialize('json', task_to_delete)
        task_to_delete.delete() 
        return HttpResponse(tasks_to_delete_json, content_type='application/json')


    # @api_view(['DELETE'])
    # def delete_task(request, id):
    #     task_to_delete = Task.objects.get(id=id) 
    #     tasks_to_delete_json = serializers.serialize('json', task_to_delete)
    #     task_to_delete.delete() 
    #     return HttpResponse(tasks_to_delete_json, content_type='application/json')
    #     # return JsonResponse({'message': 'Task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    