from hc.test import BaseTestCase
from hc.front.models import Blog, Category
from django.shortcuts import reverse
from django.utils import timezone

class BlogTest(BaseTestCase):
    def setUp(self):
        super(BlogTest, self).setUp()
        self.client.login(username="alice@example.org", password="password")
        self.category = Category(name='Tech')
        self.category.save()
        # self.blog = Blog(title='Python',body='This is a blog on python',category = self.category, created_date=timezone.now())
        # self.blog.save()
        # print (self.blog.pk)
   

    def test_add_category(self):
        url = reverse('hc-blog')
        data = {'name': ['Design'], 'add_category': ['']}
        response = self.client.post(url, data)
        query_category = Category.objects.get(name="Design")
        self.assertEqual('Design', query_category.name)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'front/blog.html')


    # def test_create_blog(self):
    #     url = reverse('hc-create_blog')
    #     data = {'category_name': ['Tech'], 'title': ['Html'], 'content': ['This is a blog on html'], 'create_blog': ['']}
    #     response = self.client.post(url, data)
    #     query_blog = Blog_post.objects.get(title="Html")
    #     print (query_blog.id)
    #     print ("dis one")
    #     self.assertEqual('Html', query_blog.title)
    #     self.assertEqual(response.status_code, 302)


    # def test_home_page_returns_all_blogs(self):
    #     response = self.client.get(reverse('hc-blog', kwargs={'filter_by':0}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'front/blog_posts.html')

    # def test_view_one_blog(self):
    #     self.test_create_blog()
    #     response_one = self.client.get(reverse('hc-read_blog', kwargs={'pk':0}))
    #     print ("----")
    #     self.assertEqual(response_one.status_code, 200)
    #     self.assertTemplateUsed(response_one, 'front/read_blog.html')