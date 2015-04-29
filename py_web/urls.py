#from django.conf.urls import patterns, include, url
from django.conf.urls import *
#<<<<<<< HEAD
#from TriAquae.views import TriAquae
#=======
#>>>>>>> 4d44c37967a40556edc6361216fa2f68f88ddb17
#from TriAquae.views import CpuUsage
#from TriAquae.views import ServiceStatus
#from TriAquae.datas import TriAquaeData
#from TriAquae.views import TriAquae, Command_Execution, File_Transfer, Server_Configuration, Job_Schedule, Assets_Management,GetServers
#from hosts.views import runCmd, cmd_result,AllUsers,AllCommands,stopExecution,getFailedLists,file_transfer,getFileLists,getDangerousCmd
#from hosts.views import *

## Uncomment the next two lines to enable the admin:
#from web.views import *
#from TriAquae.views import ServiceStatus
from django.contrib import admin

import django
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^admin/hosts/',include('TriAquae.hosts.admin_urls')),
       ('^$',LogIn),
       ('^login/$',LogIn),
       ('^index/$',account_auth),
       ('^showDashboard$',showDashboard),
       ('^logout$',logout_view),
    url(r'^assets_management/$',assets),
    url(r'^assets_management/(?P<id>\d+)/$', assets_detail, name='assets_detail'),
    url(r'^assets_management/diff$',assets_diff),
    url(r'^server_status/$',status),
    url(r'^server_status/(?P<hostname>\S+)/$',status_detail, name='status_detail'),
    url(r'^command_execution$',command_execution),
    url(r'^file_transfer$',file_transfer),
    # end by zp

    #start by tangjing
    (r'^GetServers$',GetServers),
    (r'^runCmd/$',runCmd),
    (r'^cmd_result/$',cmd_result),
    (r'^AllCommands/$',AllCommands),
    (r'^AllUsers/$',AllUsers),
    (r'^stopExecution/$',stopExecution),
    (r'^getFailedLists/$',getFailedLists),
    (r'^getSuccessLists/$',getSuccessLists), 
    (r'^transferFile/$',transfer_file),
    (r'^getFileLists/$',getFileLists),
    (r'^getDangerousCmd/$',getDangerousCmd),
	 (r'^getCPUInfo/$',getCPUInfo),
    (r'^getMemInfo/$',getMemInfo),
    (r'^getServerUpDownNum/$', getServerUpDownNum),
    (r'^getAverageLoad/$',getAverageLoad),
    #---------- BaoLeiHost ----------
	#(r'baoleihost/$',baoleihost),
    (r'^baoleihost_remote/$',baoleihost_remote),
    #(r'^loadFileTransferPage/$',loadFileTransferPage),
    #---------- Log ----------
    #(r'^log/$', Log),
    #(r'^log_view/$', LogView),
    (r'^getLog/$', getLog),
    #end by tangjing
)
