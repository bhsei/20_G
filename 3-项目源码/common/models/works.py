# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db



class Work(db.Model):
    __tablename__ = 'works'

    id = db.Column(db.BigInteger, primary_key=True, info='??id')
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???')
    uid = db.Column(db.String(11), nullable=False, server_default=db.FetchedValue(), info='????id')
    worksOK = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='???? 0???? 1????2?????? 3??????')
    photo_imageurl = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???????')
    transfer_photo_imageurl = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='?????????')
    style = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??')
    tag = db.Column(db.Text, info='????')
    time = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??????')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1????? 0??????')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
