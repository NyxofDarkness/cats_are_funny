from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Cats

class CatsTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Cats.objects.create(
            name = 'here we go, a test-Cat',
            image = 'Green Eggs and Ham',
            description = 'I do not like green eggs and ham, Sam I  am.',
            admin = testuser1
        )
        test_post.save()

    def test_cat_content(self):
        post = Cats.objects.get(id=1)
        actual_name = str(post.name)
        actual_image = str(post.image)
        actual_description = str(post.description)
        self.assertEqual(actual_name, 'here we go, a test-Cat')
        self.assertEqual(actual_image, 'Green Eggs and Ham')
        self.assertEqual(actual_description, 'I do not like green eggs and ham, Sam I  am.')

    