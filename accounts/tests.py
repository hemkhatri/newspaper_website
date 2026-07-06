from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username= "testuser",
            email= "test@gmail.com",
            password= "hellocheck12",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username= "testsuperuser",
            email = "testsuper@gmail.com",
            password = "hellotestsuper",
            )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuper@gmail.com")
        self.assertEqual(admin_user.is_active, True)
        self.assertEqual(admin_user.is_staff, True)
        self.assertEqual(admin_user.is_superuser, True)