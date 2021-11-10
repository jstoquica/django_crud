# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from rest_framework import permissions
# from djangocrud.api.serializers import UserSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

from rest_framework import viewsets
from djangocrud.api.serializers import MovieSerializer  # ,MovieMiniSerializer
from djangocrud.api.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def list(self, request, *args, **kwargs):
    #     movies = Movie.objects.all()
    #     serializer = MovieMiniSerializer(movies, many=True)
    #     return Response(serializer.data)
