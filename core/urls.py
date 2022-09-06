from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('file_upload/', csrf_exempt(views.file_upload_view)),
    path('create/', views.ArticleCreateView.as_view(), name='create'),
    path('edit/<int:pk>', views.ArticleEditView.as_view(), name='edit'),
    path('category/<str:category_name>', views.CategoryListView.as_view(), name='category'),
]