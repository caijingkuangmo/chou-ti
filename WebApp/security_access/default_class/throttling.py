# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import time
from flask import request

class BaseThrottle(object):
    def allow_request(self, view):
        raise NotImplemented('必须重写allow_request方法')

class IPThrottling(BaseThrottle):
    '''
    一分钟内访问超过5次  禁用两分钟
    '''

    VISIT_RECORD = {}
    def __init__(self):
        self.visit_num = None
        self.unit_time = None
        self.forbid_time = None

    def allow_request(self, view):
        try:
            self.parse_rate(view.throttle_rates.get('visit_rate'))
        except:
            return True

        remote_addr = request.host
        print(remote_addr)
        now_time = time.time()

        if remote_addr not in IPThrottling.VISIT_RECORD:
            IPThrottling.VISIT_RECORD[remote_addr] = {
                'start_time': [now_time, ],
                'forbid': False
            }
            return True

        start_time = IPThrottling.VISIT_RECORD[remote_addr]['start_time']
        forbid_state = IPThrottling.VISIT_RECORD[remote_addr]['forbid']
        while start_time and start_time[-1] < now_time - self.unit_time and not forbid_state:
            start_time.pop()

        if forbid_state:
            if now_time - start_time[-1] > self.forbid_time:
                print('两分钟过了，解禁')
                IPThrottling.VISIT_RECORD[remote_addr] = {
                    'start_time': [now_time, ],
                    'forbid': False
                }
                print(IPThrottling.VISIT_RECORD[remote_addr])
                return True
            else:
                print("两分钟内禁止访问，已经过了%s秒" % (now_time - start_time[-1]))
                return False
        else:
            if len(start_time) < self.visit_num:
                print("访问%s次" % (len(start_time) + 1))
                print(start_time)
                start_time.insert(0, now_time)
                return True
            else:
                print("访问%s次，禁止访问" % len(start_time))
                IPThrottling.VISIT_RECORD[remote_addr] = {
                    'start_time': [now_time, ],
                    'forbid': True
                }
                return False


    def parse_rate(self, rate_str):
        try:
            self.visit_num, self.unit_time, self.forbid_time = [int(i) for i in rate_str.split('/')]
        except ValueError as e:
            print('访问频率参数有误  请按照1/2/3这种格式')
            raise