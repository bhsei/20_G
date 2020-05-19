# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db



class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.BigInteger, primary_key=True, info='??id')
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???')
    passwd = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??????')
    sex = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 0??? 1?? 2??')
    avatar = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue(), info='????')
    salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='??salt')
    code = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1??? 0???')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
    email = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??')
    memberOK = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?????? 1?? 0??')
