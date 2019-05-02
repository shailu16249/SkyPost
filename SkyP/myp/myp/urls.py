
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import posts_list, posts_detail, posts_create, posts_update, posts_delete, home, about, userProfile
from contact.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts_list, name = 'Home'),
    path('home/', home, name=''),
    path('about/', about, name = 'about'),
    path('profile/', userProfile, name = 'profile'),
    path('contact/', contact, name = 'contact'),
   
    path('create/', posts_create),
    path('<slug:slug>/update/', posts_update),
    path('<slug:slug>/delete/', posts_delete),
    path('<slug:slug>/', posts_detail),
    path('accounts/', include('allauth.urls')),
     

 ]   
  
    
    


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)



