from hc.test import BaseTestCase
from hc.blogs.models import Blog, Category
from django.shortcuts import reverse
from django.utils import timezone

class BlogTest(BaseTestCase):
   def setUp(self):
       super(BlogTest, self).setUp()
       self.client.login(username="alice@example.org", password="password")
       self.category = Category(name='Tech')
       self.category.save()
       self.blog = Blog(
           title='Python',
           author = self.alice,
           body='This is a blog on python',
           category = self.category,
           created_date=timezone.now())
       self.blog.save()
 
   def test_create_category(self):
           url = reverse('hc-add-category')
           data = {'name': ['Design']}
           response = self.client.post(url, data)
           query_category = Category.objects.get(name="Design")
           self.assertEqual('Design', query_category.name)
           self.assertEqual(response.status_code,302)

   def test_create_blog(self):
       """Test to check if blogs are created"""
       url = reverse('hc-blogs', kwargs={'cat_id':self.category.id})
       data = {
           'name': ['Tech'],
           'title': ['Html'],
           'body': ['This is a blog on html'],
           }
       response = self.client.post(url, data)
       query_blog = Blog.objects.get(title="Html")
       self.assertEqual(response.status_code, 302)
       self.assertEqual('Html', query_blog.title)

   def test_home_page_returns_all_blogs(self):
       """Test to check if home page returns all blogs"""
       response = self.client.get(reverse('hc-blog'))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'blogs/view_blog.html')

   def test_home_page_returns_all_categories(self):
       """Test to check if home page returns all categories"""
       response = self.client.get(reverse('hc-add-category'))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'blogs/view_blog.html')

   def test_view_single_blogs(self):
       """Test to check if it returns a single blog"""
       response = self.client.get(reverse('hc-single-blog', kwargs={'cat_id':self.category.id, 'blog_id':self.blog.id}))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'blogs/single_blog.html')

   def test_delete_category(self):
       """Test if it can delete a category"""
       category = Category.objects.filter(name='Tech').first()
       url = reverse('hc-add-category', kwargs={'cat_id':category.id})
       response = self.client.delete(url)
       self.assertEqual(response.status_code, 302)

   def test_share_blog(self):
       """Test to share blogs"""
       response = self.client.get(reverse('hc-share-blog', kwargs={'cat_id':self.category.id, 'blog_id':self.blog.id}))
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'blogs/single_blog.html')
