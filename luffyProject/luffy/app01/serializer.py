from rest_framework import serializers

from app01 import models

########################课程相关#############################
class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = "__all__"

    level = serializers.SerializerMethodField()
    def get_level(self, obj):
        return obj.get_level_display()


class CourseDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CourseDetail
        fields = '__all__'
        # depth = 1

    course = serializers.CharField(source='course.name')
    recommend_courses = serializers.SerializerMethodField()
    def get_recommend_courses(self, obj):
        temp = []
        for c in obj.recommend_courses.all():
            temp.append(c.name)
        return temp

    teachers = serializers.SerializerMethodField()

    def get_teachers(self, obj):
        temp = []
        for teacher in obj.teachers.all():
            temp.append(teacher.name)
        return temp


class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CourseChapter
        fields = '__all__'

    course = serializers.CharField(source='course.name')