from django.conf.urls import url

from hc.blogs import views

urlpatterns = [
    url(r'^blog/$', views.view_blog, name="hc-blog"),
    url(r'^blog/category$', views.blog, name="hc-add-category"),    
    url(r'^blog/delete/(?P<cat_id>\d+)/$', views.delete_category, name="hc-delete-category"),
    url(r'^blog/add/(?P<cat_id>\d+)/$', views.add_blog, name="hc-add-blog"),
    url(r'^blog/category/(?P<cat_id>\d+)/post/(?P<blog_id>\d+)/$', views.view_single_blog, name="hc-single-blog"),
    url(r'^blog/(?P<cat_id>\d+)/delete/(?P<blog_id>\d+)/$', views.delete_blog, name="hc-delete-blog"),
    url(r'^blog/view/(?P<cat_id>\d+)/posts/$', views.view_category_posts, name="hc-view-category-posts"),
]