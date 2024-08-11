from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mealplan.urls')),
    path("unicorn/", include("django_unicorn.urls")),
]
