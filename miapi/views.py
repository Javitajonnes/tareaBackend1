from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Ticket
from .serializers import TodoSerializers

class TodoListApiView(APIView):
    #permissions_classes=[permissions.IsAuthenticated]

    def get(self,request, *args, **kwargs):
        todos=Ticket.objects.filter(user=request.user.id)
        serializer=TodoSerializers(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
