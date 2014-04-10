from snippets import views as viewing
from restservice import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin


admin.autodiscover()

router = DefaultRouter()
#router.register(r'snippets', viewing.SnippetViewSet)
#router.register(r'superusers', viewing.UserViewSet)
router.register(r'users', views.UserViewSet)
urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       (r'^api-doc/', include('rest_framework_swagger.urls', namespace='swagger')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += router.urls

