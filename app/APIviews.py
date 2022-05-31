from django.contrib.auth.models import User
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['GET'])
def api_root(request, format=None):
    return Response({'books': reverse('book-list', request=request, format=format)
    })

class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)