from django.conf.urls import url
from arya_lib import views
#from django.conf.urls import patterns
urlpatterns = [
url(r'^$', views.login_page, name='login_page'),
url(r'check',views.check_user,name='check_status'),
url(r'issue',views.book_issue,name='book_issue'),
url(r'issue_data',views.book_issue_data,name='book_issue_data'),

]