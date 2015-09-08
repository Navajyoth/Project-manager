from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.account.models import User
from apps.projects.models import Project


def console_log(param1='', param2='', param3='', param4=''):
    color1 = '\033[94m'
    color2 = '\033[92m'
    end = '\033[0m'
    print color1 + param1 + end + '  ' + color1 + param2 + end + '  ' +\
        color1 + param3 + end + '  ' + color2 + param4 + end


class BaseViewSetTestMixing(object):

    def test_list(self):
        url_base = '%s:%s' % (self.app_name, self.url_name)
        url = reverse(url_base + '-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log(self.app_name, 'GET', url, 'Get all items')

    def test_retrieve(self):
        url_base = '%s:%s' % (self.app_name, self.url_name)
        url = reverse(url_base + '-detail', kwargs={'pk': self.item.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log(self.app_name, 'GET', url, 'Retrieve item details')

    def test_post(self):
        url_base = '%s:%s' % (self.app_name, self.url_name)
        url = reverse(url_base + '-list')
        self.client.force_authenticate(user=self.user)
        data = self.post_data
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        console_log(self.app_name, 'POST', url, 'Create a new item.')

    def test_update(self):
        url_base = '%s:%s' % (self.app_name, self.url_name)
        url = reverse(url_base + '-detail', kwargs={'pk': self.item.id})
        self.client.force_authenticate(user=self.user)
        data = self.update_data
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        console_log(self.app_name, 'PUT', url, 'Update item details')
