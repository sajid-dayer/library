from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from django.contrib import auth
from django.contrib.auth import authenticate
from arya_lib.models import *
def login_page(request):
	return render(request, 'arya_lib/log in.html',{'var': 'none'})
def book_issue(request):
	return render(request,'arya_lib/issue.html')
def check_user(request):
	user_id = request.POST.get('username') 
	user_pass = request.POST.get('password')
	user = authenticate(username=user_id, password=user_pass)
	auth.login(request, user)
	"""if user.is_active:"""
	if user is not None:
		return render(request,'arya_lib/home.html')
	else:
		return render(request,'arya_lib/log in.html',{'kk':"wrong password" ,'var': 'block'})
def data_book(request):
	return HttpResponse("ok from my side")
"""
response_list ={}
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
	return HttpResponse(json.dumps(response_list), content_type='application/json')"""
# here we have not writing nothing

