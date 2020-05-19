# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, String, Text
from sqlalchemy.schema import FetchedValue
from application import db



class Workscomment(db.Model):
    __tablename__ = 'workscomment'

    id = db.Column(db.BigInteger, primary_key=True, info='??ID')
    workid = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??ID')
    uid = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???ID')
    commentUid = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???ID')
    time = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????')
    comment = db.Column(db.Text, info='????')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
