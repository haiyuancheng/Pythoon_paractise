#!/usr/bin/python
#-*- coding: UTF-8 -*-

import dns.resolver
import os
import httplib

iplist = []
appdomain = "www.google.com.hk" #定义顶级域名

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, "A")
    except Exception, e:
        print "dns resolver error:" + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5) #定义http连接超时间（5s）
    conn = httplib.HTTPConnection(checkurl)
    try:
        conn.request("GET", "/", headers = {"Host": appdomain}) #发起Url请求，添加host主机头
        
        r = conn.getresponse()
        getcontent = r.read(15) #获取页面前15个字符，以便做可用性校验
    finally:
        if getcontent == "<!doctype html>":# 监控URl的内容一般是实现定义好的，比喻http200等等
            
            print ip + " [OK]"
        else:
            print ip + " [Error]"

if __name__=="__main__":
	if get_iplist(appdomain) and len(iplist) > 0:
		for ip in iplist:
			checkip(ip)
	else:
		print "dns reslover error."
