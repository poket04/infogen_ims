from django.conf.urls import url, include
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'emp_api'

urlpatterns = [
    url(r'^$', views.Emp_api_index.as_view(), name='emp_api'),
    url(r'^testFox/', views.Emp_api_testFox.as_view(), name='emp_foxTest'),
    url(r'^insert_ajax/post', views.insert_ajax, name='insert_ajax'),
    url(r'^update_ajax/post', views.update_ajax, name='update_ajax'),
    url(r'^search_ajax/get', views.search_ajax, name='search_ajax'),

    url(r'^signUpForm/', views.Emp_api_signUpForm.as_view(), name='emp_signUpForm'),    #url(URL/Method/명칭)
    url(r'^insert_signUp_ajax/post', views.insert_signUp_ajax, name='insert_signUp_ajax'),   # views.py  에 정의되어있음.

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)