from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import problem,test_case
from django.core import serializers
import json
# Create your views here.

def questions(request):
    problems =problem.objects.all()
    data = serializers.serialize('json', problems)
    return HttpResponse(data,content_type="application/json")
# def code(request,title,id):
#     question = problem.objects.get(id =id)
#     question =[question]
#     data = serializers.serialize('json',question)
#     return HttpResponse(data,content_type="application/json")
def code(request,title,id):
    question = problem.objects.get(id =id)
    testcases = list(test_case.objects.filter(problem = question,isPublic=True))
    question =[question]+testcases
    data = serializers.serialize('json',question)
    
    return HttpResponse(data,content_type="application/json")
