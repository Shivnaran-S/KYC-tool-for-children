from django.urls import path
from .views import Questions,kyc_tool,success

urlpatterns = [
    path('q/',Questions.as_view(),name="questions"),
    path('',kyc_tool,name="kyc_tool"),
    path('success/',success,name="success"),
]