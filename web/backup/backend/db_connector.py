#!/usr/bin/env python
#Author: Alex Li
import sys,os,time
import tri_config,tri_module
sys.path.append(tri_config.Working_dir)
os.environ['DJANGO_SETTINGS_MODULE'] ='web.settings'
#----------------Use Django Mysql model----------------
from web.models import * 
