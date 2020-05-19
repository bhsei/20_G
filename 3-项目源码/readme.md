Python 基于Flask框架的艺术创作平台
=====================
##启动
* export ops_config=local|production && python manage.py runserver

##flask-sqlacodegen

        flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --outfile "common/models/model.py"  --flask
        flask-sqlacodegen 'mysql://root:123456@127.0.0.1/food_db' --tables user --outfile "common/models/user.py"  --flask
