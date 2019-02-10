from django.conf.urls import patterns, include, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

#0:Spanish
#1:English

urlpatterns = patterns('',
    url(r'^$', 'front.views.home', {'lang':0}, name='home'),
    url(r'^inicio$', 'front.views.home', {'lang': 0}, name='home'),
    url(r'^nosotros$', 'front.views.about_us', {'lang': 0}, name='about_us'),
        url(r'^nosotros/(?P<tag>[^/]+)$', 'front.views.about_us', {'lang':0}, name='about_us'),
    url(r'^soluciones$', 'front.views.solutions', {'lang': 0}, name='solutions'),
        url(r'^soluciones/(?P<solution>[^/]+)$', 'front.views.solutions', {'lang':0}, name='solutions'),
        url(r'^soluciones/(?P<solution>[^/]+)/(?P<product>[^/]+)$', 'front.views.solutions', {'lang':0}, name='solutions'),
    url(r'^productos$', 'front.views.solutions', {'lang': 0, 'solution': 'productos-focus', 'product':'previa'}, name='products'),
        url(r'^productos/(?P<tag>[^/]+)$', 'front.views.solutions', {'lang': 0, 'solution': 'productos-focus', 'product':'previa'}, name='products'),
    url(r'^contacto$', 'front.views.contact', {'lang': 0}, name='contact'),
        url(r'^contacto/gracias$', 'front.views.contact', {'lang':0, 'email_response': 'Email Sent :)'}, name='contact'),
    url(r'^focus-usa$', 'front.views.focus_usa', {'lang': 0}, name='focus_usa'),
    url(r'^cobertura$', 'front.views.coverage', {'lang': 0}, name='coverage'),

    #	ENGLISH
    url(r'^home$', 'front.views.home', {'lang': 1}, name='home'),
    url(r'^about-us$', 'front.views.about_us', {'lang': 1}, name='about_us'),
        url(r'^about-us/(?P<tag>[^/]+)$', 'front.views.about_us', {'lang':1}, name='about_us'),
    url(r'^solutions$', 'front.views.solutions', {'lang': 1}, name='solutions'),
        url(r'^solutions/(?P<solution>[^/]+)$', 'front.views.solutions', {'lang':1}, name='solutions'),
        url(r'^solutions/(?P<solution>[^/]+)/(?P<product>[^/]+)$', 'front.views.solutions', {'lang':1}, name='solutions'),
    url(r'^products$', 'front.views.solutions', {'lang': 1, 'solution': 'focus-products', 'product':'previa-software'}, name='products'),
        url(r'^products/(?P<tag>[^/]+)$', 'front.views.solutions', {'lang':1, 'solution': 'focus-products', 'product':'previa-software'}, name='products'),
    url(r'^contact$', 'front.views.contact', {'lang': 1}, name='contact'),
    url(r'^focus2-usa$', 'front.views.focus_usa', {'lang': 1}, name='focus_usa'),
    url(r'^coverage$', 'front.views.coverage', {'lang': 1}, name='coverage'),

    url(r'^aviso-privacidad$', 'front.views.privacy', name='privacy'),

    url(r'^hispanic-market-research$', 'front.views.home', {'lang': 0}, name='home'),
    url(r'^survey_answer$', 'front.views.survey_answer', {'lang':0}, name='survey_answer'),

    url(r'^get_last_tweets$', 'front.views.get_last_tweets', name='get_last_tweets'),
    url(r'^send_email$', 'front.views.send_email', {'lang': 1}, name='send_email'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
