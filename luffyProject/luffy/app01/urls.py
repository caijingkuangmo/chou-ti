from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^course/$', views.CourseView.as_view()),
    url(r'^course-detail/$', views.CourseDetailView.as_view()),
    url(r'^chapter/$', views.ChapterView.as_view()),
]