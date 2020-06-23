from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',email='mail@mail.com',password='1234')

        self.post = Post.objects.create(title='title',body='body',author=self.user)

    def test_string_representation(self):
        post = Post(title = 'title')
        self.assertEqual(str(post),post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','title')
        self.assertEqual(f'{self.post.author}','test')
        self.assertEqual(f'{self.post.body}','body')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'body')
        self.assertTemplateUsed(response,'home.html')
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'body')
        self.assertTemplateUsed(response,'post_detail.html')
    
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
            'title':'title',
            'body':'body',
            'author':self.user,
        })
        
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'title')
        self.assertContains(response,'body')
    
    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit',args='1'),{
            'title':'title',
            'body':'body',
        })
        self.assertEqual(response.status_code,302)
    
    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete',args='1'))
        self.assertEqual(response.status_code,302)