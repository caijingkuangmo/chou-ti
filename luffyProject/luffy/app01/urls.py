from django.conf.urls import url
from app01.views import course_view, news_view

urlpatterns = [
    ##################课程相关#########################
    # url(r'^course/$', views.CourseView.as_view()),
    url(r'^course/$', course_view.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/$', course_view.CourseView.as_view({'get':'retrieve'})),
    url(r'^course-detail/$', course_view.CourseDetailView.as_view()),
    url(r'^course-chapter/(?P<pk>\d+)/$', course_view.ChapterView.as_view()),
    url(r'^course-section/(?P<pk>\d+)/$', course_view.SectionView.as_view()),
    url(r'^price-policy/(?P<pk>\d+)/$', course_view.PricePolicy.as_view()),
    url(r'^course-comment/(?P<pk>\d+)/$', course_view.CouserCommentView.as_view()),


    ####################深科技相关#########################
    url(r'^article-source/$', news_view.ArticleSourceView.as_view()),
    url(r'^article/$', news_view.ArticleView.as_view({'get':'list'})),
    url(r'^article/(?P<pk>\d+)/$', news_view.ArticleView.as_view({'get':'retrieve'})),
    url(r'^collection/$', news_view.CollectionView.as_view({'get':'list', 'post':'create'})),
    url(r'^collection/(?P<pk>\d+)/$', news_view.CollectionView.as_view({'get':'retrieve'})),
    url(r'^comment/$', news_view.CommentView.as_view({'get': 'list', 'post':'create'})),
    url(r'^comment/(?P<pk>\d+)/$', news_view.CommentView.as_view({'get': 'retrieve'})),
]