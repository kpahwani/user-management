from service.handlers.register_all_handlers import *  # noqa

class Initializer():
    def __init__(self, app, env_name) -> None:
        self.app = app
        self.env = env_name
    
    def init_routes(self):
        pass


def init(app, env_name='local'):
    initializer = Initializer(app, env_name=env_name)
    initializer.init_routes()
    app.logger.info('Initialized app with config for env: {}'.format(env_name))