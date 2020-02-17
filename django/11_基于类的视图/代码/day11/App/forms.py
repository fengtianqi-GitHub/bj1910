#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: forms.py
@time: 2020/2/17 2:53 下午
'''
from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()