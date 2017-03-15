from django.conf.urls import url
from rango.views import  index,about,category,add_category,add_page,register,user_login,restricted,user_logout
urlpatterns = [
    url(r'^$',index , name = 'index'),
    url(r'^about/$',about, name = ' about'),
    url(r'^(?P<category_name_slug>[\w\-]+)/add_page/$', add_page, name='add_page'),
    url(r'^add_category/$', add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^restricted/', restricted, name='restricted'),
    url(r'^logout/$', user_logout, name='logout')
]