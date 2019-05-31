from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name ='home'),
    url(r'profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^neighborhood/new/post/(\d+)$', views.new_post, name='new-post'),
    url(r'^neighborhood/new/business/(\d+)$',views.business_post, name='new-business'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
]