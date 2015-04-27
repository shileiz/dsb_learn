# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='名称', max_length=40)),
                ('alias', models.CharField(verbose_name='英文名', max_length=40)),
                ('is_nav', models.BooleanField(verbose_name='是否在导航位置显示', default=False)),
                ('desc', models.CharField(verbose_name='描述', blank=True, help_text='点击分类之后显示', max_length=100)),
                ('rank', models.IntegerField(verbose_name='展示排序', default=0)),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], verbose_name='状态', default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('parent', models.ForeignKey(null=True, verbose_name='上级分类', blank=True, to='selfblog.Category', default=None)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
                'ordering': ['rank', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('alias', models.CharField(null=True, verbose_name='英文标题', blank=True, db_index=True, help_text='做伪静态url用', max_length=100)),
                ('is_top', models.BooleanField(verbose_name='置顶', default=False)),
                ('summary', models.TextField(verbose_name='摘要')),
                ('content', models.TextField(verbose_name='文章正文rst格式')),
                ('content_html', models.TextField(verbose_name='文章正文html')),
                ('view_times', models.IntegerField(default=1)),
                ('tags', models.CharField(null=True, verbose_name='标签', blank=True, help_text='用英文逗号分割', max_length=100)),
                ('status', models.IntegerField(choices=[(0, '正常'), (1, '草稿'), (2, '删除')], verbose_name='状态', default=0)),
                ('is_old', models.BooleanField(verbose_name='是否为旧数据', default=False)),
                ('pub_time', models.DateTimeField(verbose_name='发布时间', default=datetime.datetime.now)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='分类', to='selfblog.Category')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'ordering': ['-is_top', '-pub_time', '-create_time'],
            },
        ),
    ]
