from django.urls import path, include
# from django.contrib import admin
from .views import SimpleCandlestickWithPandas
# from . import views

from django.views.generic.base import TemplateView

urlpatterns = [

    # path('admin/', admin.site.urls),
    # path('signup/', views.SignUp.as_view(), name='signup'),
    path('summary', SimpleCandlestickWithPandas.as_view(),name='simple-candlestick'),
    path('bubble', TemplateView.as_view(template_name='bubble.html'), name='bubble'),
    path('', TemplateView.as_view(template_name='login.html'), name='home'),
    path('borrowBubble', TemplateView.as_view(template_name='borrowBubble.html'), name='borrowBubble'),
    path('borrowSummary', TemplateView.as_view(template_name='borrowSummary.html'), name='borrowSummary')
]
