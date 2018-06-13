# -*- encoding: utf-8 -*-
# @Time    : 2018/6/13 11:03
# @Author  : mike.liu
# @File    : sql.py

#创建数据库sql语句
create_database = 'create database if not exists testdb default character set utf8; '

#创建testdata表
create_table = """
    drop table if exists testdata;
    create table testdata(
         Movie_Name varchar(40) unique not null comment '用户名',
         Movie_Property varchar(30) not null comment '密码',
         Excpect_result varchar(40) unique not null comment '期望结果',
         )engine=innodb character set utf8 comment '测试数据表';"""