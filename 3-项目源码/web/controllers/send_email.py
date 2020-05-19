# -*- coding: utf-8 -*-
from flask import current_app, render_template
from application import app
import yagmail
import os



def send_mail(to,  registcode):
    yag = yagmail.SMTP(user="offeryes@163.com", password="YVZQJFLNWFLYQOCD", host='smtp.163.com',encoding='gbk')
    b=str(registcode)
    # 邮件正文
    contents = ['亲爱的用户您好： 感谢注册艺术创作平台，请在网站注册页面填入验证码完成注册：%s'%b,
                '艺术创作平台开发团队']

    yag.send(to, '艺术创作平台注册验证码', contents)

    yag.close()




