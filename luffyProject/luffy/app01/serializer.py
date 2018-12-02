from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
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
        depth = 1

    # course = serializers.CharField(source='course.name')
    # recommend_courses = serializers.SerializerMethodField()
    # def get_recommend_courses(self, obj):
    #     temp = []
    #     for c in obj.recommend_courses.all():
    #         temp.append(c.name)
    #     return temp
    #
    # teachers = serializers.SerializerMethodField()
    #
    # def get_teachers(self, obj):
    #     temp = []
    #     for teacher in obj.teachers.all():
    #         temp.append(teacher.name)
    #     return temp


class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CourseChapter
        fields = '__all__'

    course = serializers.CharField(source='course.name')


class SectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = "__all__"

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class PricePolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PricePolicy
        fields = "__all__"


#######################深科技相关##############################
class ArticleSourceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleSource
        fields = "__all__"

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"

    source = serializers.CharField(source='source.name')
    article_type = serializers.SerializerMethodField()
    def get_article_type(self, obj):
        return obj.get_article_type_display()

    status = serializers.SerializerMethodField()
    def get_status(self, obj):
        return obj.get_status_display()

    position = serializers.SerializerMethodField()
    def get_position(self, obj):
        return obj.get_position_display()


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"

    account = serializers.CharField(source="account.username")
    # content_type = serializers.CharField(source="content_type.model", allow_null=True)
    content_type = serializers.CharField(source="content_type.model", default=None)
    # content_type = serializers.SerializerMethodField()  #这个只是显示用？
    # def get_content_type(self, obj):
    #     return obj.content_type.model if obj.content_type else None

    def create(self, validated_data):
        print("validated_data", validated_data)
        model_dic = validated_data.pop("content_type")
        validated_data['content_type'] = ContentType.objects.filter(**model_dic).first()
        account_dic = validated_data.pop("account")
        validated_data['account'] = models.Account.objects.filter(**account_dic).first()
        obj = models.Comment.objects.create(**validated_data)
        return obj

class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = "__all__"

    account = serializers.CharField(source="account.username")
    # content_type = serializers.CharField(source="content_type.app_label")
    content_type = serializers.CharField(source="content_type.model")

    def create(self, validated_data):
        model_dic = validated_data.pop("content_type")
        validated_data['content_type'] = ContentType.objects.filter(**model_dic).first()
        account_dic = validated_data.pop("account")
        validated_data['account'] = models.Account.objects.filter(**account_dic).first()
        obj = models.Collection.objects.create(**validated_data)
        return obj


#####################购物车相关############################
class ShoppingCarAddSerializers(serializers.Serializer):
    account_id = serializers.IntegerField(write_only=True)
    couse_id = serializers.IntegerField(write_only=True)
    policy_id = serializers.IntegerField(write_only=True)

class ShoppingCarShowSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['name', 'course_img']

    policy_list = serializers.ModelSerializer()
    def get_policy_list(self, obj):
        temp = {}
        for policy in obj.policy_list.all():
            temp[policy.id] = {
                "valid_period": policy.get_valid_period_display(),
                "price": policy.price
            }
        return temp


class ShoppingCarUpdateSerializers(serializers.Serializer):
    account_id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    policy_id = serializers.IntegerField()






