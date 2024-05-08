from django.test import TestCase
from .models import Jjim


class JjimModelTest(TestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        user = User.objects.create_user(
            username="testuser", password="testpassword")
        from .models import Article
        article = Article.objects.create(title="Test Article")
        jjim = Jjim.objects.create(content_type=ContentType.objects.get_for_model(
            Article), object_id=article.pk, user=user)

    def test_jjim_creation(self):
        jjim = Jjim.objects.get(pk=1)
        self.assertEqual(jjim.content_type.model_class(), Article)
        self.assertEqual(jjim.object_id, 1)
        self.assertEqual(jjim.user.username, "testuser")

    def test_jjim_deletion(self):
        jjim_count = Jjim.objects.count()
        jjim = Jjim.objects.get(pk=1)
        jjim.delete()
        self.assertEqual(Jjim.objects.count(), jjim_count - 1)

    def test_jjim_toggle_view(self):
        from django.urls import reverse
        from rest_framework.test import APIClient

        client = APIClient()
        content_type_slug = 'article'
        object_id = 1

        url = reverse(
            'jjim-toggle', kwargs={'content_type_slug': content_type_slug, 'object_id': object_id})
        response = client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['is_liked'], True)
        self.assertEqual(Jjim.objects.count(), 2)

        response = client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['is_liked'], False)
        self.assertEqual(Jjim.objects.count(), 1)
