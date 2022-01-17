from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Agent
from .serializers import AgentSerializer
from rest_framework import permissions


# Create your views here.

#### get all agents ####
class AgentListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None

##### single object #####
class AgentDetailView(RetrieveAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

#### Top seller list ####
class TopSellerListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.filter(top_seller=True)
    serializer_class = AgentSerializer
    pagination_class = None

#### post #####
class CreateApiView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None
