# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, ModelViewSet

from app01 import serializer
from app01 import models

class ArticleSourceView(APIView):
    authentication_classes = []
    def get(self, request, *args, **kwargs):
        article_sources = models.ArticleSource.objects.all()
        ass = serializer.ArticleSourceSerializers(instance=article_sources, many=True)
        return Response(ass.data)

class ArticleView(ViewSetMixin, APIView):
    authentication_classes = []
    def list(self, request, *args, **kwargs):
        articles = models.Article.objects.all()
        art_s = serializer.ArticleSerializers(instance=articles, many=True)
        return Response(art_s.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        article = models.Article.objects.filter(id=pk).first()
        art = serializer.ArticleSerializers(instance=article, many=False)
        return Response(art.data)

class CollectionView(ViewSetMixin, APIView):
    authentication_classes = []
    def list(self, request, *args, **kwargs):
        collections = models.Collection.objects.all()
        cs = serializer.CollectionSerializers(instance=collections, many=True)
        return Response(cs.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        collection_obj = models.Collection.objects.filter(id=pk).first()
        collection = serializer.CollectionSerializers(instance=collection_obj, many=False)
        return Response(collection.data)

    def create(self, request, *args, **kwargs):
        '''
        {
        "account": "alex",
        "content_type": "article",
        "object_id": 1,
        # "date": "2018-11-26T03:53:30.947000Z"
        }
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        cs = serializer.CollectionSerializers(data=request.data, many=False)
        if cs.is_valid():
            cs.save()
            return Response(cs.data)
        else:
            return Response(cs.errors)

class CommentView(ViewSetMixin, APIView):
    authentication_classes = []
    def list(self, request, *args, **kwargs):
        comments = models.Comment.objects.all()
        cs = serializer.CommentSerializers(instance=comments, many=True)
        return Response(cs.data)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop("pk")
        comment = models.Comment.objects.filter(id=pk).first()
        c = serializer.CommentSerializers(instance=comment, many=False)
        return Response(c.data)

    def create(self, request, *args, **kwargs):
        cs = serializer.CommentSerializers(data=request.data, many=False)
        if cs.is_valid():
            cs.save()
            return Response(cs.data)
        else:
            return Response(cs.errors)
