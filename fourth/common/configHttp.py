# coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.02

import os
import codecs
import configparser

#获取该文件的真实路径，然后分割路径和文件名存入一个元组
proDir = os.path.split(os.path.realpath(__file__))[0]
#获取上层目录
parDir = os.path.dirname(proDir)
configPath = os.path.join(parDir,"config.ini")
print('---',configPath)
print('prodir:',proDir,configPath)