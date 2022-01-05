#
# Start server.py
#

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher

@dispatcher.add_method
def prime(**kwargs):
    if (kwargs["number"] == 1):
        return False
    i = 2
    while i*i <= kwargs["number"]:
        if kwargs["number"] % i == 0:
            return False
        i += 1
    return True

@Request.application
def application(request):

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 4000, application)
    
#
# End server.py
#