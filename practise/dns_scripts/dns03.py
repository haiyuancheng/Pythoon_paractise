#!/usr/bin/python
#-*- coding: UTF-8 -*-
#Only limited by top-level domain

import dns.resolver

domain = raw_input("Please input an domain: ")

ns = dns.resolver.query(domain, 'NS')

for i in ns.response.answer:
    for j in i.items:
        print j.to_text()
