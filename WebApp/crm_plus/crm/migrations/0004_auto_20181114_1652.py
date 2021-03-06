# Generated by Django 2.1.2 on 2018-11-14 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
        ('crm', '0003_customerdistrbute'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.User'),
        ),
        migrations.AlterField(
            model_name='classlist',
            name='teachers',
            field=models.ManyToManyField(limit_choices_to={'depart__in': [1002, 1005]}, related_name='abc', to='crm.UserInfo', verbose_name='任课老师'),
        ),
        migrations.AlterField(
            model_name='classlist',
            name='tutor',
            field=models.ForeignKey(limit_choices_to={'depart': 1001}, on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='crm.UserInfo', verbose_name='班主任'),
        ),
        migrations.AlterField(
            model_name='courserecord',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'depart_id__in': [1002, 1003]}, on_delete=django.db.models.deletion.CASCADE, to='crm.UserInfo', verbose_name='讲师'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='consultant',
            field=models.ForeignKey(limit_choices_to={'depart_id': 1001}, on_delete=django.db.models.deletion.CASCADE, related_name='consultanter', to='crm.UserInfo', verbose_name='课程顾问'),
        ),
        migrations.AlterField(
            model_name='customerdistrbute',
            name='consultant',
            field=models.ForeignKey(limit_choices_to={'depart_id': 1001}, on_delete=django.db.models.deletion.CASCADE, to='crm.UserInfo', verbose_name='课程顾问'),
        ),
        migrations.AlterField(
            model_name='studyrecord',
            name='homework_note',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='作业评语'),
        ),
    ]
