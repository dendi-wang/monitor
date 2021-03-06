#!/usr/bin/env python
# _*_ coding:utf-8 _*_

configs = {
    "HostID": '192.168.112.130',
    "Server": "192.168.8.134",
    "ServerPort": 8000,
    "urls": {

        'get_configs': ['api/client/config', 'get'],
        # acquire all the services will be monitored
        'service_report': ['api/client/service/report/', 'post'],

    },
    'RequestTimeout': 30,
    'ConfigUpdateInterval': 300,  # 5 mins as default

}
