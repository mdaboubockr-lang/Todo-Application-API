from django.contrib import admin
from django.urls import path
from Todo_API.views import TodoEndpoints, UpdateingPoints
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Api/get/book_list/create', view=TodoEndpoints.as_view(), name='API_get'),
    path('Api/update/all/<int:pk>/', view=UpdateingPoints.as_view(), name='update_views'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
