from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Todoフォルダ内にurlsを使用する。
    path('', include('todo.urls')),
]
