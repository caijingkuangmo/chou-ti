# -*- coding:utf-8 -*-
#! /usr/bin/env python
# __author__ = 'seven'

import re

'''
分页组件主要关注的是两个方面：
    一个是 分页数据展示
    一个是 页码变化

对于分页数据展示，涉及到业务需求，这块主要提给一个 切片的数据，不涉及前端页面控制

而对于页码，一般都是一个独立组件，可以分离出来，前后端都可把控

所以：主要是 切片数据和生成页码html

需要提供数据：所有的数据、当前页(从请求中获取)、每页显示多少条

'''

#定义页面异常类
class InvalidPage(Exception):
    pass

class PageNotAnInteger(InvalidPage):
    pass

class EmptyPage(InvalidPage):
    pass


'''
使用:
paginator = Paginator(contact_list, 25) 
page_num = request.GET.get('page')
page = paginator.page(page_num)
'''

#定义分页器
class Paginator:

    def __init__(self, data_list, per_page_size, full_url_path, page_number=11):
        self.data_list= data_list
        self.per_page_size = int(per_page_size)
        self.page_number = page_number
        #比如 /index/?o=-1
        self.full_url_path = full_url_path

    @property
    def count(self):
        '''数据总条数'''
        try:
            return self.data_list.count()
        except (AttributeError, TypeError):
            return len(self.data_list)

    @property
    def num_pages(self):
        if self.count == 0:
            return
        from math import ceil
        return ceil(self.count / self.per_page_size)

    @property
    def page_range(self):
        '''页码范围'''
        return range(1, self.num_pages + 1)

    def page(self, number):
        number = self.validate_number(number)

        #获取当前页的起始索引位置和结束索引位置
        bottom = (number - 1) * self.per_page_size
        top = bottom + self.per_page_size
        if top >= self.count:
            top = self.count #考虑最后一页的情况
        return self._get_page(self.data_list[bottom:top], number, self)

    def validate_number(self, number):
        '''请求数字必须基于1的整数页码'''
        try:
            if isinstance(number, float) and number.is_integer():
                raise ValueError  #比如1.5的情况，抛出异常
            number = int(number)  #比如1.0
        except (TypeError, ValueError):
            raise PageNotAnInteger('当前页数不为一个整数')
        if number < 1:
            raise EmptyPage('当前页数小于1')
        if number > self.num_pages:
            raise EmptyPage('当前页数没有结果')
        return number

    def _get_page(self, *args, **kwargs):
        '''返回当前页实例'''
        return Page(*args, **kwargs)

#单页类
class Page(object):
    def __init__(self, current_page_data_list, number, paginator):
        self.data_list = current_page_data_list
        self.number = number
        self.paginator = paginator

    def __repr__(self):
        return '<Page %s of %s>'%(self.number, self.paginator.num_pages)

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, index):
        if not isinstance(index, (int, slice)):
            raise TypeError
        if not isinstance(self.data_list, list):
            self.data_list = list(self.data_list)
        return self.data_list[index]

    def has_next(self):
        return self.number < self.paginator.num_pages

    def has_previous(self):
        return self.number > 1

    def has_other_pages(self):
        return self.has_next() or self.has_previous()

    def next_page_number(self):
        return self.paginator.validate_number(self.number + 1)

    def previous_page_number(self):
        return self.paginator.validate_number(self.number - 1)


    def start_index(self):
        '''感觉用不到'''
        if self.paginator.count == 0:
            return 0
        return self.paginator.per_page_size * (self.number - 1)

    def end_index(self):
        '''感觉用不到'''
        if self.number == self.paginator.num_pages:
            return self.paginator.count
        return self.number * self.paginator.per_page_size

    @property
    def start_end_page_range(self):
        '''返回 起始页码和结束页码 的迭代范围'''
        bottom_extend_size = int((self.paginator.page_number - 1) / 2)
        top_extend_size = self.paginator.page_number - bottom_extend_size - 1

        left_page_num = self.number - bottom_extend_size
        right_page_num = self.number + top_extend_size

        if self.number - self.paginator.page_number <= 0 and self.number <= bottom_extend_size:  #考虑左边界的几个页码变化
            left_page_num = 1
            right_page_num = self.paginator.page_number

        # 考虑右边界的几个页码变化
        if ((self.number + self.paginator.page_number - 1) >= self.paginator.num_pages) and (self.number > self.paginator.num_pages - top_extend_size):
            left_page_num = self.paginator.num_pages - self.paginator.page_number + 1
            right_page_num = self.paginator.num_pages

        if self.paginator.page_number > self.paginator.num_pages:  #如果页数 小于 要求的页码个数，显示所有页码
            left_page_num = 1
            right_page_num = self.paginator.num_pages
        return range(left_page_num, right_page_num+1)

    @property
    def url_temp(self):
        if '?' in self.paginator.full_url_path and 'page' in self.paginator.full_url_path:
            return re.sub('page=\d+', 'page={page}', self.paginator.full_url_path, 1)
        elif '?' in self.paginator.full_url_path:
            return "{full_url_path}&page={page}"
        else:
            return "{full_url_path}?page={page}"

    def bulid_page_number_html(self):
        '''构建页面前端代码'''

        list_page = []
        if self.number == 1:  #上一页
            prev = '<li><a class="pre-page" href="javascript:void(0);">上一页</a></li>'
        else:
            prev = '<li><a class="pre-page" href="%s">上一页</a></li>' % (self.url_temp.format(full_url_path=self.paginator.full_url_path, page=self.number - 1),)

        list_page.append(prev)

        for p in self.start_end_page_range:
            if p == self.number:
                temp = '<li><a class="active-page" href="%s">%s</a></li>' % (self.url_temp.format(full_url_path=self.paginator.full_url_path, page=p), p)
            else:
                temp = '<li><a class="li-page" href="%s">%s</a></li>' % (self.url_temp.format(full_url_path=self.paginator.full_url_path, page=p), p)
            list_page.append(temp)

        if self.number == self.paginator.num_pages: #下一页
            nex = '<li><a class="next-page" href="javascript:void(0);">下一页</a></li>'
        else:
            nex = '<li><a class="next-page" href="%s">下一页</a></li>' % (self.url_temp.format(full_url_path=self.paginator.full_url_path, page=self.number + 1),)
        list_page.append(nex)

        # 跳转
        # jump = """<input type='text' /><a onclick="Jump('%s',this);">GO</a>""" % ('/index/')
        # script = """<script>
        #         function Jump(baseUrl,ths){
        #             var val = ths.previousElementSibling.value;
        #             if(val.trim().length>0){
        #                 location.href = baseUrl + val;
        #             }
        #         }
        #         </script>"""

        str_page = "".join(list_page)
        return str_page



