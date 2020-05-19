# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db



class Admin(db.Model):
    __tablename__ = 'admin'

    uid = db.Column(db.BigInteger, primary_key=True, info='??uid')
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???')
    permission = db.Column(db.String(20), nullable=False, server_default=db.FetchedValue(), info='????')
    email = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1?? 2?? 0????')
    login_name = db.Column(db.String(20), nullable=False, unique=True, server_default=db.FetchedValue(), info='?????')
    login_pwd = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='????')
    login_salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='???????????')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='1??? 0???')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
    mobile = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????')
