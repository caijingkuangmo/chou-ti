from django.contrib import admin

# Register your models here.
from app01 import models
from django.contrib.contenttypes.models import ContentType

admin.site.register(ContentType)


# site.register(models.Account)
#
# class CourseConfig(ModelXadmin):
#     list_display = ['name', 'sub_category', 'course_type', 'degree_course', 'level']
# site.register(models.Course, CourseConfig)
#
#
# class CourseDetailConfig(ModelXadmin):
#     list_display = ['course', 'hours', 'course_slogan', 'why_study', 'recommend_courses', 'teachers']
# site.register(models.CourseDetail, CourseDetailConfig)
#
#
# class CourseChapterConfig(ModelXadmin):
#     list_display = ['chapter', 'name', 'course']
# site.register(models.CourseChapter, CourseChapterConfig)
#
#
# class UserAuthTokenConfig(ModelXadmin):
#     list_display = ['user', 'token']
# site.register(models.UserAuthToken, UserAuthTokenConfig)
#
#
# site.register(models.ArticleSource)
#
# class ArticleConfig(ModelXadmin):
#     list_display = ['title', 'source', 'article_type', 'brief', 'vid', 'comment_num', 'agree_num', 'view_num', 'collect_num']
# site.register(models.Article, ArticleConfig)

'''支不支持contenttype呢？  --- 不支持'''
# class CollectionConfig(admin.ModelAdmin):
#     list_display = ['content_type', 'object_id', 'account']
# admin.site.register(models.Collection, CollectionConfig)
#
# class CommentConfig(admin.ModelAdmin):
#     list_display = ['content_type', 'object_id', 'p_node', 'content', 'account', 'disagree_number', 'agree_number']
# admin.site.register(models.Comment, CommentConfig)