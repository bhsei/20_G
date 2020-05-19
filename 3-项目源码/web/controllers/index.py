# -*- coding: utf-8 -*-
from flask import Blueprint,request,redirect,jsonify, make_response,url_for,g,render_template
from web.controllers.send_email import send_mail
from common.libs.Helper import ops_render
from common.libs.UrlManager import UrlManager
from common.libs.UserService import UserService
#管理员表
from common.models.admin import Admin
#用户表
from common.models.member import Member
#风格表
from common.models.style import Style
#作品表
from common.models.works import Work
#评论表
from common.models.workscomment import Workscomment
from application import app,db
from create_art_image import create_art_image
route_index = Blueprint( 'index_page',__name__ )
import random
import json
import os
import datetime
#首页

@route_index.route("/")
def index():
    resp_data={}
    return ops_render( "index.html",resp_data )

#新用户注册
#常佳辉
@route_index.route( "/memberRegister",methods = [ "GET","POST" ] )
def memberRegister():
    if request.method == "GET":
        resp_data = {}
        return ops_render( "register.html",resp_data)#render_template
    req = request.values
    resp = { 'code':200,'msg':'注册成功~~','data':{} }
    email= req['email'] if 'email' in req else 0
    login_pwd1 = str(req['login_pwd1']) if 'login_pwd1' in req else ''
    login_pwd2 = str(req['login_pwd2']) if 'login_pwd2' in req else ''
    code =str(req['code']) if 'code' in req else ''
    member_info = Member.query.filter_by(email=email).first()
    if member_info.code==code:
        member_info.salt = UserService.geneSalt()
        print(member_info.salt)
        member_info.passwd =  UserService.genePwd( login_pwd1,member_info.salt)
        print(member_info.passwd)
        db.session.add(member_info)
        db.session.commit()
        return jsonify(resp)
    else:
        resp = {'code': 400, 'msg': '注册失败~~', 'data': {}}
        return jsonify(resp)



# 新用户邮箱验证
#潘安佶
@route_index.route("/memberEmail",methods = [ "GET","POST" ])
def memberEmail():
    req = request.values
    if request.method == "GET":
        resp_data = {}
        return ops_render("register.html", resp_data)
    resp = {'code': 200, 'msg': '验证码已发送~~', 'data': {}}
    email = req['email'] if 'email' in req else 0
    code = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        code += ch
    member_info=Member.query.filter_by(email=email).first()
    if member_info:
        member_info=member_info
    else:
        member_info=Member()
    member_info.code=code
    if email is None:
        resp['code'] = 400
        resp['msg'] = "请输入符合规范的邮箱~~"
        return jsonify(resp)
    member_info.email=email
    send_mail(email,code)
    db.session.add(member_info)
    db.session.commit()
    return jsonify(resp)

#用户登录
#潘安佶
@route_index.route( "/memberLogin" ,methods = [ "GET","POST" ])
def memberlogin():
    resp={'code':200,'msg':'登录成功','data':{}  }
    user_info=g.current_user
    if user_info:
        return redirect(url_for('index_page.createArtPicture'))
    if request.method == "GET":
        resp_data = {}
        return ops_render( "login.html",resp_data )
    req = request.values
    email = req['email'] if 'email' in req else ''
    print(email)
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    print(login_pwd)
    member_info = Member.query.filter_by(email=email).first()
    if member_info:
        if member_info.passwd!= UserService.genePwd(login_pwd,member_info.salt ):
            resp['code'] = 400
            resp['msg'] = "请输入正确的登录用户名和密码~~"
            return jsonify(resp)
        response=make_response(json.dumps(resp))
        response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
            UserService.geneAuthCode(member_info), member_info.id), 60 * 60 * 24 * 120)
        return response
    else:
        resp['code'] = 400
        resp['msg'] = "该用户未注册~~"
        return jsonify(resp)


#使用网站现有风格转变图片创建用户的作品
#刘佳恒
@route_index.route( "/createArtPicture" ,methods=['POST', 'GET'])
def createArtPicture():
    user_info=g.current_user
    resp_data = {}
    if not user_info:
        redirect(url_for('index_page.memberLogin'))
    if request.method == 'POST':
        f = request.files['file']
        req = request.values
        selectStyle = str(req['selectStyle']) if 'selectStyle' in req else ''
        print(selectStyle)
        file_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        file_name=file_time+'.jpg'
        rootpath = os.getcwd()
        upload_path = os.path.join(rootpath, 'web/static/uploads',file_name)  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        contentpath='web/static/uploads/'+file_name
        styles_name='style'+selectStyle+'.jpg'
        stylepath='web/static/styles/'+styles_name
        outputpath='web/static/works/'+file_name
        model_path = 'models/21styles.model'
        create_art_image(contentpath,stylepath,outputpath, model_path='models/21styles.model')
        photo_imageurl='http://49.233.31.42:8999/static/uploads/'+file_name
        transfer_photo_imageurl='http://49.233.31.42:8999/static/works/'+file_name
        works_info=Work()
        works_info.nickname=user_info.email
        works_info.time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        works_info.photo_imageurl=photo_imageurl
        works_info.transfer_photo_imageurl=transfer_photo_imageurl
        db.session.add(works_info)
        db.session.commit()
        return redirect(url_for('index_page.releaseArtPicture'))
    if request.method == 'GET':
        return ops_render( "createArtPicture.html",resp_data )

#查看所有作品
#常佳辉
@route_index.route("/ViewAllWorks", methods=['POST', 'GET'])
def ViewAllWorks():
    resp_data = {}
    req = request.values
    user_info=g.current_user
    page_size=6
    offset= req['offset'] if 'offset' in req else 0
    work_info=Work.query.filter_by(status=1).order_by(Work.id.desc()).limit(page_size).all()
    work_list = []
    for item in work_info:
        tmp_data = {
            'tag': item.tag,
            'time': item.time,
            'imageUrl': item.transfer_photo_imageurl,
            'id':item.id
        }
        work_list.append(tmp_data)
    resp_data['list'] = work_list
    return ops_render( "allArtWorks.html",resp_data )


#评论
#秋宇
@route_index.route("/comment", methods=['GET', 'POST'])
def comment():
    if request.method == "GET":
        user_info = g.current_user
        page_size=10
        resp={}
        if user_info==False:    #没登录返回登录界面
            return redirect(url_for('index_page.memberlogin'))
        req = request.values
        workid=req['id']
        work = Work.query.filter_by(id=workid).first()
        resp['work_info']=work
    
        workcomment_display = Workscomment.query.filter_by(workid=workid).order_by(Workscomment.id.desc()).limit(
            page_size).all()
        workcomment_list = []
        for item in workcomment_display:
            tmp_data = {
                'commentUid': item.commentUid,
                'comment': item.comment,
                'time': item.time,
                'id':item.id
            }
            workcomment_list.append(tmp_data)
        resp['workcomment_info'] = workcomment_list
        return ops_render('anArtWork.html', resp)
    if request.method=="POST":
        user_info = g.current_user
        if user_info:
            req = request.values
            resp_data = {'code': 200, 'msg': '发布评论成功~~', 'data': {}}
            comment=req['anEvaluateText'] if 'anEvaluateText' in req else ''
            workid=req['ID'] if 'ID' in req else 0
            commentuid = user_info.email
            workcomment_info= Workscomment(workid=workid,uid=user_info.id,commentUid=commentuid,time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),comment=comment,updated_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),created_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            db.session.add(workcomment_info)
            db.session.commit()
            return jsonify(resp_data)
        else:
            resp_data = {'code': 400, 'msg': '请先登录在进行评论~', 'data': {}}
            return jsonify(resp_data)



#发布作品
#张祥国
@route_index.route( "/releaseArtPicture" ,methods = [ "GET","POST" ])
def releaseArtPicture():
    resp_data = {'code': 200, 'msg': '发布成功~~', 'data': {}}
    req = request.values
    member_info=g.current_user
    work_info = Work.query.filter_by(nickname=member_info.email).order_by(Work.id.desc()).first()
    if request.method == 'POST':
        tag= str(req['workText']) if 'workText' in req else ''
        work_info.status=1
        work_info.tag=tag
        db.session.add(work_info)
        db.session.commit()
        return render_template( "afterShareArtPiture.html" )
    resp_data['info']=work_info
    return ops_render("afterCreateArtPicture.html", resp_data)

#查看自己的动态
#张祥国
@route_index.route( "/viewMyPost" ,methods = [ "GET","POST" ])
def viewMyPost():
    resp_data =  {'code': 200, 'msg': '查看动态成功~~', 'data': {}}
    req = request.values
    page_size=6
    member_info=g.current_user
    work_info = Work.query.filter_by(nickname=member_info.email).order_by(Work.id.desc()).limit(page_size).all()
    work_list = []
    i=0
    if work_info:
        for item in work_info:
            print(i)
            i=i+1
            tmp_data = {
                'tag': item.tag,
                'time': item.time,
                'imageUrl': item.transfer_photo_imageurl,
            }
            work_list.append(tmp_data)
    resp_data['list'] = work_list
    return ops_render( "myHome.html",resp_data )



#管理员登录
#牟秋宇
@route_index.route( "/adminLogin" ,methods = [ "GET","POST" ])
def adminlogin():
    resp={'code':200,'msg':'','data':{}  }
    if request.method == "GET":
        resp_data = {}
        return ops_render( "adminLogin.html",resp_data )
    if request.method == "POST":
        req = request.values
        nickname = req['email'] if 'email' in req else ''
        login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
        admin_info = Admin.query.filter_by(login_name=nickname).first()
        if admin_info:
            if admin_info.login_pwd == login_pwd:
                resp['code'] = 200
                return jsonify(resp)
            else:
                resp['code'] = 400
                print(login_pwd)
                resp['msg'] = "请输入正确的管理员帐名和密码~~"
                return jsonify(resp)
        else :
            resp = {'code': 400, 'msg': '没有该用户', 'data': {}}
            return jsonify(resp)
#管理员登录
#牟秋宇
@route_index.route( "/adminHome" ,methods = [ "GET","POST" ])
def adminHome():
    if request.method == "GET":
        resp_data = {}
        work_info = Work.query.filter_by(status=1).order_by(Work.id.asc()).all()
        work_list = []
        member_info = Member.query.order_by(Member.id.asc()).all()
        member_list=[]
        for item in work_info:
            tmp_data = {
                'tag': item.tag,
                'time': item.time,
                'nickname': item.nickname,
                'id': item.id
            }
            work_list.append(tmp_data)

        for item in member_info:
            tmp_data = {
                'id': item.id,
                'email': item.email,
                'time': item.created_time,
            }
            member_list.append(tmp_data)
        resp_data['work_list'] = work_list
        resp_data['member_list'] = member_list
        return ops_render( "adminHome.html",resp_data )




#项目介绍
@route_index.route( "/projectIntroduction" )
def projectIntroduction():
    resp_data = {}
    return ops_render( "project-introduction.html",resp_data )

#关于我们
@route_index.route( "/aboutAndContactUs" )
def aboutAndContactUs():
    resp_data = {}
    return ops_render( "aboutAndContactUs.html",resp_data )



@route_index.route("/logout")
def logout():
    response=make_response(redirect(UrlManager.buildUrl("/memberLogin")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response