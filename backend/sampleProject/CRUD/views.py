# myapp/views.py
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Admin
from .serializers import UserSerializer, AdminSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def UserApi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                user = User.objects.get(id=id)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return HttpResponse(status=404)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(status=404)

        user.delete()
        return HttpResponse(status=204)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def AdminApi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                admin = Admin.objects.get(id=id)
                serializer = AdminSerializer(admin)
                return Response(serializer.data)
            except Admin.DoesNotExist:
                return HttpResponse(status=404)
        else:
            admins = Admin.objects.all()
            serializer = AdminSerializer(admins, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        try:
            admin = Admin.objects.get(id=id)
        except Admin.DoesNotExist:
            return HttpResponse(status=404)

        data = JSONParser().parse(request)
        serializer = AdminSerializer(admin, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            admin = Admin.objects.get(id=id)
        except Admin.DoesNotExist:
            return HttpResponse(status=404)

        admin.delete()
        return HttpResponse(status=204)
