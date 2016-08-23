from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import json
from django.contrib import auth
from django.contrib.auth import authenticate
from arya_lib.models import *
def login_page(request):
	return render(request, 'arya_lib/log in.html',{'var': 'none'})
def main_page(request):
	return render(request,'arya_lib/home.html')
def check_user(request):
	user_id = request.POST.get('username') 
	user_pass = request.POST.get('password')
	user = authenticate(username=user_id, password=user_pass)
	auth.login(request, user)
	"""if user.is_active:"""
	if user is not None:
		return HttpResponseRedirect('home',{'user':request.user.username})
	else:
		return render(request,'arya_lib/log in.html',{'kk':"wrong password" ,'var': 'block'})
def book_issue_render(request):
	print request.user.username
	return render(request,'arya_lib/issue.html')
def data_book(request):
	try:
		book_data=book_issue()
		book_data.user_name=request.user.username
		book_data.bookname=request.GET.get("book_name")
		book_data.author=request.GET.get("author_name")
		book_data.book_id=request.GET.get("book_id")
		book_data.issue_date=request.GET.get("issue_date")
		book_data.return_date=request.GET.get("return_date")
		book_data.save()
		return HttpResponse("Data Inserted Succesfully!")
	except Exception as e:
		return HttpResponse("Problem while inserting data")
def book_search(request):
	return render(request,'arya_lib/search.html')
def search_in_db(request):
	bookname= request.GET.get("bookname")
	author= request.GET.get("author")
	book_id=book_list.objects.filter(bookname=bookname,author=author).values('book_id')
	if book_id != None or book_id != ():
		return HttpResponse("book found")
	else:
		return HttpResponse("book not found")


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

