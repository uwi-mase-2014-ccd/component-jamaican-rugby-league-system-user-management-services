from snippets import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin


admin.autodiscover()

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

