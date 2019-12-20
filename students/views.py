from django.shortcuts import render
from .models import Student, News
from rest_framework import routers, serializers, viewsets, permissions, status
from .serializers import StudentSerializer, NewsSerializer, UserSerializer, UserSerializerWithToken
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #
    # def get_queryset(self):
    #     print(self.request.user.is_staff)
    #     if self.request.user.is_staff:
    #         return Student.objects.all()
    #     return Response(data={'status': 'denied'}, status=403)
    #
    # @action(detail=False, methods=['GET'])
    # # @permission_classes([IsAuthenticated])
    # def statistics(self, request):
    #     print(request.GET.get('group'))
    #     return Response(data={'amount': 31, 'avg': 5.7})

class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None ):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)