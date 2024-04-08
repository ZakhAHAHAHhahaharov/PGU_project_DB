
from django.core.handlers.asgi import ASGIHandler

from django.http import HttpResponse

def index(request: ASGIHandler):
    return HttpResponse("COWBoYz WiTH The M0therFuCKing NUke$")