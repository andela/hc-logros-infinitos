from django.conf.urls import url

from hc.blogs import views

urlpatterns = [
    url(r'^blog/$', views.view_blogs, name="hc-blog"),
    url(r'^blog/category$', views.categories, name="hc-add-category"),    
    url(r'^blog/delete/(?P<cat_id>\d+)/$', views.delete_category, name="hc-delete-category"),
    url(r'^blog/add/(?P<cat_id>\d+)/$', views.blog, name="hc-add-blog"),
    url(r'^blog/category/post/(?P<blog_id>\d+)/$', views.single_blog, name="hc-single-blog"),
    url(r'^blog//delete/(?P<blog_id>\d+)/$', views.single_blog, name="hc-delete-blog"),
    url(r'^blog/view/(?P<cat_id>\d+)/posts/$', views.blog, name="hc-view-category-posts"),
]