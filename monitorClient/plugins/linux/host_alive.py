#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import subprocess


def monitor(frist_invoke=1):
    value_dic = {}
    shell_command = 'uptime'
    result = subprocess.Popen(shell_command, shell=True, stdout=subprocess.PIPE).stdout.read()

    # user,nice,system,iowait,steal,idle = result.split()[2:]
    value_dic = {
        'uptime': result,

        'status': 0
    }
    return value_dic

# monitor()
