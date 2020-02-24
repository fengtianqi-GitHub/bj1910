#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/2/19 9:52 上午
'''
from rest_framework import serializers
#
# class BookInfoSerializers(serializers.Serializer):
#     btitle = serializers.CharField()
#     bpub_date = serializers.DateField()
#     bread = serializers.IntegerField()
#     bcomment = serializers.IntegerField()
#     bimage = serializers.CharField()
#     def create

# 从模型生成序列化类
from App.models import BookInfo, Heroinfo


class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroinfo
        fields = "__all__"



def check_bcomment(value):
    value = int(value)
    if value < 0:
        raise serializers.ValidationError("评论数不能小于0")

class BookInfoSerializers(serializers.ModelSerializer):
    # 关联对象 : 模型必须有外键关系
    # heros = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # heros = serializers.StringRelatedField(many=True,read_only=True)
    heros = HeroInfoSerializer(many=True,read_only=True)
    class Meta:
        model = BookInfo
        # 显示指定使用那些模型中字段
        # fields = ('btitle','bpub_date','bread','bcomment','bimage')

        # 使用模型的全部字段
        fields = "__all__"
        extra_kwargs = {
            'bcomment':{'validators':[check_bcomment]}
        }

    def validate_bread(self,value):
        value = int(value)
        print(value)
        if value < 0:
            raise serializers.ValidationError("阅读数不能小于0")
        return value
