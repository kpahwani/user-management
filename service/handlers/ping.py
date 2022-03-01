from main import app
from service.shared.resources import registry


@registry.handles(
    rule="/"
)
def ping():
    return 'Ping pong'
