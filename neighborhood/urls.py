from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name ='home'),
    url(r'new-post/$',views.new_post,name='post')
]