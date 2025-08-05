from django.test import TestCase
from django.contrib.auth.models import User

from core.models import UserProfile, Role

class UserModelTest(TestCase):

    def test_create_user(self):
        username = "testname123"
        password = "testpassword"

        user = User.objects.create_user(username=username)
        user.set_password(password)

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_staff)

    def test_create_user_with_role(self):
        username = "testname123"
        password = "testpassword"
        
        user = User.objects.create_user(username=username, password=password)

        role = Role(name='Farmer')

        userProfile = UserProfile(user=user, role=role)

        self.assertEqual(user.username,  userProfile.user.username)
        self.assertEqual(user.password,  userProfile.user.password)
        self.assertEqual(role.name,  userProfile.role.name)