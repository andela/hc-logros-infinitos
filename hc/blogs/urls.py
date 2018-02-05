from django.conf.urls import url

from hc.blogs import views

urlpatterns = [
    url(r'^blog/$', views.view_blogs, name="hc-blog"),
    url(r'^blog/categories/$', views.categories, name="hc-add-category"),    
    # url(r'^blog/delete/(?P<cat_id>\d+)/$', views.delete_category, name="hc-delete-category"),
    url(r'^blog/add/(?P<cat_id>\d+)/$', views.blogs, name="hc-add-blog"),
    url(r'^blog/categories/(?P<cat_id>\d+)/blogs/(?P<blog_id>\d+)$', views.blogs, name="hc-single-blog"),
    url(r'^blog/categories/blogs/(?P<blog_id>\d+)$', views.blogs, name="hc-delete-blog"),    
    # url(r'^blog//delete/(?P<blog_id>\d+)/$', views.delete_blog, name="hc-delete-blog"),
    url(r'^blog/view/(?P<cat_id>\d+)/posts/$', views.blogs, name="hc-category"),
    url(r'^blog/categories/(?P<cat_id>\d+)$', views.categories, name="hc-add-category"), 
    url(r'^blog/categories/(?P<cat_id>\d+)/blogs/$', views.blogs, name="hc-blogs"),
]