from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.api import serializers
from books import models


class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()
