from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username:'testcase',
            email:'test@gmail.com',
            password='pass'

        )
       self.post=Post.objects.create(
           title='my title',
           body='amazing',
           author='self.user'
       ) 
    def test_string_representation(self):
        post=Post(title'My title')
        self.assertEqual(str(post).post.title)
    def test_post_content(self):
        self. assertEqual(f'{self.post.title}'), 'my article')
        self. assertEqual (f'{self.post.author}'), 'jenny')
        self. assertEqual (f'{self.post.body}', 'amazing')

    def test_post_list_view(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'amazing')
        self.assertTemplateUsed(response,'home.html')


    def text_post_detail_views(self):
        response=self.client.get('./ppost/1/')
        no_response=self.client.get('/post/100000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'My title')
        self.assertTemplateUsed(response, 'post_detail.html')

