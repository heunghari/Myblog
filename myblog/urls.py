from django.contrib import admin
from django.urls import path
import posts.views
from django.conf.urls.static import static
from django.conf import settings
import sitepages.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.home, name='home'),
    path('posts/<int:post_id>/', posts.views.post_details, name="post_details"),
    path('about/', sitepages.views.about, name="about")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
