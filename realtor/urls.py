from django.urls import path
from .views import AgentDetailView, AgentListView, TopSellerListView,CreateApiView

urlpatterns = [
    path('', AgentListView.as_view(), name='agent'),
    path('AgentPost/', CreateApiView.as_view(), name='agent-post'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('top-seller/', TopSellerListView.as_view(), name='top-seller'),
]