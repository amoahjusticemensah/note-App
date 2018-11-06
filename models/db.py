from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")

db.define_table("notes",
               Field('db_topic'),
               Field('db_typenote'))
