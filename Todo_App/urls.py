from django.contrib import admin
from django.urls import path
from Todo_API.views import TodoEndpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Api/get/book_list/create', view=TodoEndpoints.as_view(), name='API_get')
]
