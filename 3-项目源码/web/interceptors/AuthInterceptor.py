from application import app
from flask import request,redirect,g
from common.models.member import Member
from common.models.admin import Admin
from common.libs.UserService import  UserService
from common.libs.UrlManager import  UrlManager
import re

@app.before_request
def before_request():


    user_info=check_login()
    g.current_user=None
    if user_info:
        g.current_user=user_info
    redirect( UrlManager.buildUrl( "/" ) )


"""
判断用户是否已经登录
"""
def check_login():
    cookies=request.cookies
    auth_cookie=cookies[app.config['AUTH_COOKIE_NAME']]if  app.config['AUTH_COOKIE_NAME']in cookies else None

    if auth_cookie is None:
        return False

    auth_info=auth_cookie.split("#")
    if len(auth_info)!=2:
        return False

    try:
        user_info=Member.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0]!= UserService.geneAuthCode(user_info):
        return False

    return user_info