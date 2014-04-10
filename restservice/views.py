from restservice.models import User
from rest_framework import viewsets
from rest_framework import permissions
from restservice.serializers import UserSerializer
from rest_framework.views import Response, APIView
from rest_framework.decorators import action, link
from restservice.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        """
        Return a list of objects.

        """
        return super(UserViewSet, self).list(request, *args, **kwargs)

    @link()
    def get_email(self, request, pk):
        """Returns a users email of a cigar."""
        user = self.get_object()
        return Response(user.email)

    @link()
    def auth_login(self, request, pk, password):
        """
        Authenticates weather a user exists
        """
        user = self.get_object()

        return Response('True')
