#!/usr/bin/env python
#Author: Coral
import sys,os,time
import tri_config
import platform
sys.path.append(tri_config.Working_dir)
#Tri_PATH = PATH = os.path.abspath(os.path.dirname(__file__))
#Tri_Models = os.path.join(Tri_PATH,'web/models')

Tri_Models = os.path.join(tri_config.Working_dir,'web/models')
sys.path.append(Tri_Models)

# Select the current system version
version = platform.platform().split('with-')[1].split('.')[0]
if version == 'redhat-5':
    Tri_Ver_Models = os.path.join(tri_config.Working_dir,'web/models/Centos_5.9')
elif version == 'centos-6':
    Tri_Ver_Models = os.path.join(tri_config.Working_dir,'web/models/')
    #Tri_Ver_Models = os.path.join(tri_config.Working_dir,'web/models/Centos_6.4')
elif version == 'Ubuntu-12':
    Tri_Ver_Models = os.path.join(tri_config.Working_dir,'web/models/Ubuntu_12')
elif version == 'Ubuntu-13':
    Tri_Ver_Models = os.path.join(tri_config.Working_dir,'web/models/Ubuntu_13')
else:
    Tri_Ver_Models = os.path.join(tri_config.Working_dir,'web/models/Centos_5.9')
sys.path.append(Tri_Ver_Models)
