from django.conf.urls import url, include
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name ='home'),
    url(r'profile/$',views.profile,name='profile'),
    url(r'^edit/profile/$',views.edit_profile,name='edit_profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^neighborhood/new/post/(\d+)$', views.new_post, name='new-post'),
    url(r'^neighborhood/new/business/(\d+)$',views.new_business, name='new-business'),
    url(r'^neighborhood/(\d+)',views.neighborhood,name='neighborhood'),
    url(r'^neighborhoods/',views.neighborhoods,name='neighborhoods'),
    url(r'^accounts/',include('registration.backends.simple.urls')),
]

if settings.DEBUG:
   urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
