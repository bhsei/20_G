# -*- coding: utf-8 -*-
import time
from application import app

class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        release_version = app.config.get( 'RELEASE_VERSION' )
        ver = "%s"%( int( time.time() ) ) if not release_version else release_version
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildimageUrl( path ):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD_CV']['prefix_url'] + path
        return url

    @staticmethod
    def buildCVIMGUrl(path):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['DOWNLOAD_CV']['prefix_url'] + path
        return url

    @staticmethod
    def buildbannerImageUrl( path ):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD_BANNER']['prefix_url'] + path
        return url
    @staticmethod
    def buildbannerDetailImageUrl( path ):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD_DETAILBANNER']['prefix_url'] + path
        return url
    @staticmethod
    def buildNewsImageUrl( path ):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD_NEWS']['prefix_url'] + path
        return url
    @staticmethod
    def buildLOGOImageUrl( path ):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['UPLOAD_LOGO']['prefix_url'] + path
        return url
    @staticmethod
    def buildCurtainImageUrl( path ):
        app_config = app.config['APP']
        url = app_config['domain'] + app.config['CURTAIN']['prefix_url'] + path
        return url