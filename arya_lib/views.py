from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from django.contrib.auth import authenticate
from arya_lib.models import *
def login_page(request):
	return render(request, 'arya_lib/log in.html')
def check_user(request):
	user_id = request.GET.get('username') 
	user_pass = request.GET.get('password')
	response_list ={}
	user = authenticate(username=user_id, password=user_pass)
	if user is not None:
		print "wowwlknddnf"
	print type(user),user_id,user_pass
	if user_id is None or len(user_id) < 1:
		response_list["error"]="No data found"
		print "yes"
		return HttpResponse(json.dumps(response_list), content_type='application/json')
	else:
		b =User_Login_List.objects.filter(username=user_id,password=user_pass).values('id')
		print "no",b
		response_list["status"]="False"
		return HttpResponse(json.dumps(response_list), content_type='application/json')
	
"""def home(request):
	return render(request'arya_lib/home.html')
def login(request):
	return view_login(request)
"""
