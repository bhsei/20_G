# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db


class Style(db.Model):
    __tablename__ = 'style'

    id = db.Column(db.BigInteger, primary_key=True, info='??id')
    nickname = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='???')
    uid = db.Column(db.String(11), nullable=False, server_default=db.FetchedValue(), info='??????id')
    styleOK = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='???? 0???? 1????2?????? 3??????')
    stylefile = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='????????')
    modelfile = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??????')
    time = db.Column(db.String(100), nullable=False, server_default=db.FetchedValue(), info='??????')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 1????? 0?????')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
