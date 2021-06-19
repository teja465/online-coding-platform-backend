from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import problem,test_case
from django.core import serializers
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny




# Create your views here.

CODE_EVALUATION_URL = u'https://api.hackerearth.com/v4/partner/code-evaluation/submissions/'
CLIENT_SECRET = '7b9e5877ccb804b9ae5e690c33e47fcfc72d31ec'
CLIENT_ID ='7f5bd882998711a63b94adce5b399a48974a3b2d7942.api.hackerearth.com'



def questions(request):
    """
    returns all questions to show in home page 
    """
    problems =problem.objects.all()
    data = serializers.serialize('json', problems)
    return HttpResponse(data,content_type="application/json")

def code(request,title,id):
    """
    returns question and all  its public test cases 
    """
    question = problem.objects.get(id =id)
    testcases = list(test_case.objects.filter(problem = question,isPublic=True))
    question =[question]+testcases
    data = serializers.serialize('json',question)

    return HttpResponse(data,content_type="application/json")


@csrf_exempt
def compile(request,code="",language="PYTHON3",input=""):
    print("In compile ------------------------------------>>>>>>>>>>>>>>>>>>>>>")
    if request.method=="POST":
        data_from_post = json.load(request)['post_data']
        #print(data_from_post)
        code=data_from_post.get('code',"")
        user_input=data_from_post.get('input',"")
        language=data_from_post.get('language',"")
        print("user input",user_input)
        print("code ",code)
        print("language",language)

        COMPILE_URL = 'https://api.hackerearth.com/v3/code/compile/'
        RUN_URL = 'https://api.hackerearth.com/v3/code/run/'
        # CLIENT_SECRET="7b9e5877ccb804b9ae5e690c33e47fcfc72d31ec"
        data = {
            'client_secret': CLIENT_SECRET,
            'async': 0,
            'source': code,
            'lang': language,
            'time_limit': 5,
            'memory_limit': 262144,
            'input':user_input
        }
 
        r = requests.post(RUN_URL, data=data)
        # print(r.json(),type(r.json()))
        # print(r)
        resp=r.json()
        return JsonResponse(resp)

@csrf_exempt
def submit_code(request):
    # question
    if request.method=="POST":
        data_from_post = json.load(request)['post_data']
        print(data_from_post)
        code=data_from_post["code"]
        language= data_from_post["language"]
        question_pk=data_from_post["question_pk"]
    
    question =problem.objects.get(pk = question_pk)
    # print(question)
    private_testcases = list( test_case.objects.filter(problem=question,isPublic= False) )
    # print(private_testcases)


    COMPILE_URL = 'https://api.hackerearth.com/v3/code/compile/'
    RUN_URL = 'https://api.hackerearth.com/v3/code/run/'
    # CLIENT_SECRET="7b9e5877ccb804b9ae5e690c33e47fcfc72d31ec"
    data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': code,
        'lang': language,
        'time_limit': 5,
        'memory_limit': 262144,
        'input':""
    }
 
    final_response=[]
    for tc in private_testcases:
        data["input"] = tc.__dict__["input"]
        r = requests.post(RUN_URL, data=data)
        resp=r.json()
        run_status = resp.get("run_status",None),
        if run_status!=None:
            # print(run_status)
            output = run_status[0].get("output","ERROR")

            print(output.strip() == tc.__dict__["output"].strip())
            if output.strip() == tc.__dict__["output"].strip():
                final_response.append(
                    {
                        "status":"Passed"
                    }
                )

            else:
                final_response.append(
                    {
                        "status":"Failed"
                    }
                )

            
        else:
            final_response.append(
                    {
                        "status":"Error"
                    }
                )
        print()
        print()
        print()
    return JsonResponse(final_response,safe=False)

@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
# @permission_classes([AllowAny])

def auth_test(request):
    print("In test method ",request.user)
    
    data ={}
    data['name']='some-test-name-here'
    return JsonResponse(data,safe=False)