from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'dz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('news.urls', namespace="news")),
    url(r'^contacts/', include('contacts.urls', namespace="contacts")),
    url(r'^partners/', include('partners.urls', namespace="partners")),
]
