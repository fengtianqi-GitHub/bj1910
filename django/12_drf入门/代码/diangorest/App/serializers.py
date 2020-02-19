#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/2/18 3:01 下午
'''
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


# class BookInfoSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     btitle = serializers.CharField(min_length=3)
#     bpub_date = serializers.DateField(required=False)
#     bread = serializers.IntegerField(required=False)
#     bcomment = serializers.IntegerField(required=False)
#     bimage = serializers.CharField(max_length=300,required=False)
from App.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__' #('id','btitle','bpub_date','bread','bcomment','bimage')