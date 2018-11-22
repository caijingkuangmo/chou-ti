from django.conf.urls import url, include
from django.contrib import admin
from Xadmin.service.xadmin import site

from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', site.urls),
    url(r'^api/', include('app01.urls')),
    url(r'^login/', views.LoginView.as_view()),
]







