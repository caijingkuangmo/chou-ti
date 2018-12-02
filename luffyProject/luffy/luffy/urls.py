from django.conf.urls import url, include
from django.contrib import admin
from Xadmin.service.xadmin import site

from app01.views import account_view
from app01.views import test_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', site.urls),
    url(r'^api/v1/', include('app01.urls')),
    url(r'^login/', account_view.LoginView.as_view()),
    url(r'^logout/', account_view.LogoutView.as_view()),
    url(r'^test/', test_view.test),
]







