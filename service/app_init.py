import pymongo
from flask import g

from service.handlers.register_all_handlers import *  # noqa
from service.shared.resources import rebar


class Initializer():
    def __init__(self, app, env_name) -> None:
        self.app = app
        self.env = env_name
    
    def get_config_object_name(self, env_name):
        # For backwards compatibility...
        # We used to have config files for each of these live environments
        if env_name in ['dev', 'test', 'prod']:
            env_name = 'remote'

        return 'config.{}.Config'.format(env_name)
    
    def init_config(self):
        config_name = self.get_config_object_name(self.env_name)
        self.app.config.from_object(config_name)
        self.app.config['ENV'] = self.env_name
        
    def init_db(self)->None:
        with self.app.app_context():
            client = pymongo.MongoClient(self.app.config.get("MONGO_DB_CONNECTION_HOST", "localhost"), self.app.config.get("MONGO_DB_CONNECTION_PORT", 27017))
        self.app.app_ctx_globals_class.database = client.society
            
    def init_rebar(self)->None:
        rebar.init_app(self.app)


def init(app, env_name='local')->None:
    initializer = Initializer(app, env_name=env_name)
    initializer.init_db()
    initializer.init_rebar()
    app.logger.info('Initialized app with config for env: {}'.format(env_name))
