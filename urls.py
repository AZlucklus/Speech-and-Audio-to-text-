from django.urls import path
from django.conf.urls.static import static
from . import views
from DEMOPROJECT import settings

urlpatterns = [
    path('', views.hi,name="home"),
    path('vspage/', views.vspage,name="vs2txt"),
    path('txtpage/', views.txtpage,name="txt2vs"),
    
    path('vspage/vsreg/', views.vs_reg,name="vsreg"),
    path('txtpage/txtreg/', views.transcribe_audio,name="txtreg"),
    
    path('google/', views.goo,name="script"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 