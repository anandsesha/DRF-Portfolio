from django.contrib.auth.models import User # type: ignore
from rest_framework import viewsets # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny # type: ignore
from .serializers import UserSerializer, EducationSerializer, WorkSerializer, PortfolioSerializer
from .models import Education, Work, Portfolio

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # type: ignore

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # type: ignore

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # type: ignore