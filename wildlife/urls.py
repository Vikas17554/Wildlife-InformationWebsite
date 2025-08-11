"""
URL configuration for wildlife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wild import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # Include home.urls
    path('wild/',views.index, name='index'),
    path('maharashtra/',views.maharashtra, name='maharashtra'),
    path('jammu/',views.jammu, name='jammu'),
    path('kerala/',views.kerala, name='kerala'),
    path('MP/',views.MP, name='MP'),
    path('gujarat/',views.gujarat, name='gujarat'),
    path('rajasthan/',views.rajasthan, name='rajasthan'),
    path('odisha/',views.odisha, name='odisha'),
    path('tamil_nadu/',views.tamil_nadu, name='tamil_nadu'),
    path('uttarakhand/',views.uttarakhand, name='uttarakhand'),
     path('assam/',views.assam, name='assam'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

