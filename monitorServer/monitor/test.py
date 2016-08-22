#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import models
def test(request):
    hostobj = models.Host.objects.get(ip='192.168.112.130')
    print hostobj
