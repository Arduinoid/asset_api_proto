from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from rest_framework import status 
from warranty.models import Server 
from warranty.serializers import ServerSerializer 

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def server_list(request):
    if request.method == 'GET':
        servers = Server.objects.all()
        servers_serializer = ServerSerializer(servers, many=True)
        return JSONResponse(servers_serializer.data)

    elif request.method == 'POST':
        server_data = JSONParser().parse(request)
        servers_serializer = ServerSerializer(data=server_data)
        if servers_serializer.is_valid():
            servers_serializer.save()
            return JSONResponse(servers_serializer.data,
            status=status.HTTP_201_CREATED)
        return JSONResponse(servers_serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def server_detail(request, pk):
    try:
        server = Server.objects.get(pk=pk)
    except Server.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        servers_serializer = ServerSerializer(server)
        return JSONResponse(servers_serializer.data)

    elif request.method == 'PUT':
        server_data = JSONParser().parse(request)
        servers_serializer = ServerSerializer(server, data=server_data)
        if servers_serializer.is_valid():
            servers_serializer.save()
            return JSONResponse(servers_serializer.data)
        return JSONResponse(ServerSerializer.errors,
        status=status.HTTP_400_BAD_RQUEST)

    elif request.method == 'DELETE':
        server.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


