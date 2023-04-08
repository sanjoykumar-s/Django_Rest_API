from django.contrib import admin
from django.urls import path, re_path
from django.urls import path, include
from dog import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name='Home'),
    path('admin/', admin.site.urls, name='Admin-Panel'),
    path('api/', include('dog.urls'), name='Dog-API'),
    re_path(r'^.*$', views.ApiRoot.as_view(), name='catch-all'),

]