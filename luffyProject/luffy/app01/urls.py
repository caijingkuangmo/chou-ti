from django.conf.urls import url
from app01.views import course_view

urlpatterns = [
    # url(r'^course/$', views.CourseView.as_view()),
    url(r'^course/$', course_view.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course_view.CourseView.as_view({'get':'retrieve'})),
    url(r'^course-detail/$', course_view.CourseDetailView.as_view()),
    url(r'^chapter/$', course_view.ChapterView.as_view()),
]