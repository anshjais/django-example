from django.conf.urls import url
from basic_app import views

#Template tagging
app_name = 'basic_app'  #always equal to the app name

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    # relative/$ means anything after relative
    url(r'^other/$',views.other,name='other'),
]
