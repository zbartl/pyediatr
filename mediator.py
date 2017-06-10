class Request:
    @classmethod
    def handler(cls, h):
        cls.handler = h

    def pre(self):
        self.handler.pre(self)

    def handle(self):
        self.handler.handle(self)

    def post(self):
        self.handler.post(self)


def send(request):
    if hasattr(request, 'pre') and callable(getattr(request, 'pre')):
        request.pre()

    result = None
    try:
        result = request.handle()
    except AttributeError:
        print("oops")

    if hasattr(request, 'post') and callable(getattr(request, 'post')):
        request.post()

    result


class Request1(Request):
    def __init__(self):
        self.id = 1
        self.name = 'test'


@Request1.handler
class Request1Handler:
    def pre(request):
        print(f'before, {request.id:d} {request.name:s}')

    def handle(request):
        print(f'{request.id:d} {request.name:s}')

    def post(request):
        print(f'after, {request.id:d} {request.name:s}')

