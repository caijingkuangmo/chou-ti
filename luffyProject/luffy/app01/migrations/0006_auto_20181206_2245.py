# Generated by Django 2.1.3 on 2018-12-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20181206_2239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stufollowuprecord',
            options={'verbose_name_plural': '学员跟进记录'},
        ),
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.PositiveIntegerField(default=0, verbose_name='可提现和使用余额'),
        ),
        migrations.AddField(
            model_name='account',
            name='openid',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='role',
            field=models.SmallIntegerField(choices=[(0, '学员'), (1, '导师'), (2, '讲师'), (3, '管理员')], default=0, verbose_name='角色'),
        ),
        migrations.AddField(
            model_name='account',
            name='uid',
            field=models.CharField(blank=True, help_text='微信用户绑定和CC视频统计', max_length=64, null=True, unique=True),
        ),
    ]