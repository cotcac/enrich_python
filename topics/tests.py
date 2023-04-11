import pytest
from .models import Topics
from django.urls import reverse


# Get all topic
@pytest.mark.django_db
def test_get_all_topic(client):
   url = reverse('get_all_topic')
   response = client.get(url)
   assert response.status_code == 200

# Get one topic
@pytest.mark.django_db
def test_get_one_topic(client):
   Topics.objects.create(id=123,name="book")
   url = reverse('detail', kwargs={'id': 123})
   response = client.get(url)
   assert response.status_code == 200

# Test delete a topic
@pytest.mark.django_db
def test_delete_topic(api_client_auth):
   Topics.objects.create(id=123,name="book")
   url = reverse('delete', kwargs={'id': 123})
   response = api_client_auth.delete(url)
   assert response.status_code == 204

@pytest.mark.django_db
def test_delete_topic_error_404(api_client_auth):
   url = reverse('delete', kwargs={'id': 554325})
   response = api_client_auth.delete(url)
   assert response.status_code == 404

# Test Create a topic
@pytest.mark.django_db
def test_create_topic(api_client_auth):
  url = reverse('create')
  data = {'name': 'Test'}
  response = api_client_auth.post(url, data=data)
  assert response.status_code == 200

# Test Create a topic
@pytest.mark.django_db
def test_create_topic_error_400(api_client_auth):
  url = reverse('create')
  data = {}
  response = api_client_auth.post(url, data=data)
  assert response.status_code == 400

# Test update a topic
@pytest.mark.django_db
def test_update_topic(api_client_auth):
  topic = Topics.objects.create(name="Update me")
  url = reverse('update', kwargs={'id': topic.pk})
  data = {'name': 'Test1'}
  response = api_client_auth.put(url, data=data)
  assert response.status_code == 200

# Test update a topic
@pytest.mark.django_db
def test_update_topic_error_400(api_client_auth):
  topic = Topics.objects.create(name="book")
  url = reverse('update', kwargs={'id': topic.pk})
  data = {}
  response = api_client_auth.put(url, data=data, content_type='application/json')
  assert response.status_code == 200