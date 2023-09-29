from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from . import models, serializers


class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserRegisterSerializer


class UserLogIn(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token_key': token.key,
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'contact_number': user.contact_number,
        })


class PostCreateView(generics.CreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.CreatePostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.PostListSerializer
    # model = models.Post
    queryset = models.Post.objects.all()

    # def get_queryset(self):
    #     """If User is login then only show there added post. If public user then show all the post."""
    #     token_key = self.request.auth.key if self.request.auth else None
    #     if token_key:
    #         try:
    #             user = Token.objects.get(key=token_key).user
    #         except Exception as e:
    #             return Response("Invalid User")
    #         else:
    #             return self.model.objects.filter(author=user)
    #
    #     return self.model.objects.all()


"""
Write the API to provide user count based on date.
date = Todat , return all the user which are created before today.
"""


class UerListByDateView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = serializers.UserListSerializer

    def get_queryset(self):
        date = self.request.query_params.get('date')
        return models.User.objects.filter(date_joined__date__lte=date)

    def get(self, request, *args, **kwargs):
        if not self.request.query_params.get('date'):
            return Response("You must have to pass the date")

        return self.list(request, *args, **kwargs)


