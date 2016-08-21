from django.conf.urls import url
from arya_lib import views
#from django.conf.urls import patterns
urlpatterns = [
url(r'^$', views.login_page, name='login_page'),
url(r'check',views.check_user,name='check_status'),
url(r'issue',views.book_issue_render,name='book_issue_render'),
url(r'data_book',views.data_book,name='book_issue_data'),
url(r'search',views.book_search,name='book_search'),
url(r'home',views.main_page,name='main_page'),

]