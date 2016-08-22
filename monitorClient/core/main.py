#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import client, commands


class command_handler(object):
    def __init__(self, sys_args):
        self.sys_args = sys_args
        if len(self.sys_args) < 2: exit(self.help_msg())
        self.command_allowcator()

    def command_allowcator(self):
        '''分捡用户输入的不同指令'''
        # print(self.sys_args[1])

        if hasattr(self, self.sys_args[1]):
            func = getattr(self, self.sys_args[1])
            return func()
        else:
            print("command does not exist!")
            self.help_msg()

    def help_msg(self):
        valid_commands = '''
        start   start monitor client
        stop    stop monitor client
        '''
        exit(valid_commands)

    def start(self):
        print("going to start the monitor client")
        status, output = self.Get_ip()
        if status == 0:
            client_ip = output
        Client = client.ClientHandle(client_ip)
        Client.forever_run()

    def stop(self):
        print("stop the monitor client")

    def Get_ip(self):
        status, output = commands.getstatusoutput(
            'ip addr show eth0 | grep inet | awk \'NR==1{print $2}\' |awk -F / \'{print $1}\' ')
        return status, output
