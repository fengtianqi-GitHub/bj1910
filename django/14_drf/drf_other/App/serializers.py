#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/2/20 10:04 上午
'''
from rest_framework import serializers

from App.models import Bookinfo, User


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"