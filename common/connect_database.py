# -*- !coding: utf-8 -*-
# !/usr/bin/python3
# @Author : Garcia
# @Date   : 2019/12/31
# @File   : connect_database.py

import os
import psycopg2
import cx_Oracle
import mysql.connector as mysql

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


def judge_database(database_info, sql):
    try:
        if database_info['type'] == 'ORACLE':
            data_obj = OracleConnect(database_info)
        elif database_info['type'] == 'MySQL':
            data_obj = MysqlConnect(database_info)
        elif database_info['type'] == 'PostgreSQL':
            data_obj = PsycopgConnect(database_info)
        result = data_obj.connect(sql)
        return result
    except Exception as e:
        print(e)
        return 'sql执行出错'


def execute_sql(conn, sql):
    try:
        cur = conn.cursor()
        cur.execute(sql.lstrip())
        if sql.lstrip().startswith('select'):
            cr = cur.fetchall()
            return cr
        else:
            return '已执行一条SQL语句'
    except Exception as e:
        print(e)
        return 'sql语句执行出错'
    finally:
        close_database(conn)


def close_database(conn):
    conn.close()


class OracleConnect:
    def __init__(self, database_info):
        self.username = database_info['username']
        self.password = database_info['password']
        self.host = database_info['host']
        self.port = database_info['port']
        self.server = database_info['server']

    def connect(self, sql):
        try:
            conn = cx_Oracle.connect(self.username, self.password, self.host + ':' + self.port + '/' + self.server)
            return execute_sql(conn, sql)
        except Exception as e:
            print(e)
            return '数据库链接错误'


class MysqlConnect:
    def __init__(self, database_info):
        self.username = database_info['username']
        self.password = database_info['password']
        self.host = database_info['host']

    def connect(self, sql):
        try:
            conn = mysql.connect(host=self.host, user=self.username, passwd=self.password)
            return execute_sql(conn, sql)
        except Exception as e:
            print(e)
            return '数据库链接错误'


class PsycopgConnect:
    def __init__(self, database_info):
        self.username = database_info['username']
        self.password = database_info['password']
        self.host = database_info['host']
        self.port = database_info['port']
        self.server = database_info['server']

    def connect(self, sql):
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.server,
                user=self.username,
                password=self.password
            )
            return execute_sql(conn, sql)
        except Exception as e:
            print(e)
            return '数据库链接错误'


if __name__ == '__main__':
    # sql = "select * from project_news where id = 993245"
    # sql = "update project_news set title = '123' where id = 993245"
    # database_info = {"type": "ORACLE", "host": "192.168.9.223", "port": "1522", "server": "REACH",
    #                  "password": "reach123", "username": "PROJECTS"}

    # sql = "select * from leads.app_users where id = 13239"
    # sql = "UPDATE leads.crm_users set login_start = now() where id = 10240"
    # database_info = {"type": "PostgreSQL", "host": "test-rcc-pg.pg.rds.aliyuncs.com", "port": "3433",
    #                  "server": "leads2018", "password": "qBMYePl6UB5oSZlanETE", "username": "testpg"}
    # sql = "select * from bidding.bid_firms WHERE id in (16, 17)"
    sql = "update bidding.bid_firms set province_id = 32 WHERE ID in (1234565434565434)"
    database_info = {"type": "MySQL", "host": "rcc-test-mysql.mysql.rds.aliyuncs.com", "port": "",
                     "server": "bidding", "password": "JJrMQTowU8fV2gCU", "username": "bidding"}
    print(judge_database(database_info, sql))
