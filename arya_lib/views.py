from django.shortcuts import render
from django.http import HttpResponse
def login_page(request):
	return render(request, 'arya_lib/log in.html')
def home_page(request):
	print request.GET.get('username')
	return HttpResponse("response is done")
def login(request):
	return view_login(request)

