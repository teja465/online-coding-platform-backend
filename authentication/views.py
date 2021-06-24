from django.shortcuts import render
import jwt
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json
SECRET ="SECRET_KEY!@#123"
# Create your views here.
@csrf_exempt
def login_user(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # print(body)
    data={}
    user = authenticate(username=body.get('username',''), password=body.get('password',''))
    if user:
        data['user']=user.username
        data['success']="user successfully validated"
        token =  jwt.encode({"user": user.username}, SECRET, algorithm="HS256")
        # print("bef str",token)
        token= str(token)
        # print("aft str",token)
        # print(token,type(token))
        data['token'] =token
    else:
        data['user']="Invalid credentials"
        data['failure']="Invalid credentials to login"
    # user = User.objects.get()
    return JsonResponse(data,safe=False)

@csrf_exempt
def signup_user(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # print(body)
    data={}
    # user = authenticate(username=body.get('username',''), password=body.get('password',''))
    try:

        user = User.objects.create_user(body.get('username',''), 'lennon@thebeatles.com', body.get('password','') )
        data['message']="Successfully created account"
        data['success']  = "Successfully created account"
    except:
        data['message']="Error while creating again please try again"
        data['error']= data['message']
    return  JsonResponse(data,safe=False)

def get_user_from_jwt(request):
    pass
def logout_user(request):
    pass

def auth_test(request):
    print(request.headers)
    print(is_authenticated(request))
    data={'msg':"un authenticated user"}
    return JsonResponse(data,safe=False)

def is_authenticated(request):
    token =request.headers.get('Authorization',None)
    token = bytes(token, 'utf-8')
    user =None
    token=token[2:len(token)-1]
    try:
        user = jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        print("Error while decoding jwt token")
    if user:
        user_obj =User.objects.get(username=user['user'])
        return user_obj
    else:
        return None
