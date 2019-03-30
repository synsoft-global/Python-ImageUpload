from django.test import TestCase
from django.test.client import RequestFactory
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from main_app import views
from django.test import override_settings
import os

class ImageUploadTest(TestCase):
  # Initiating the request
  def setUp(self):
    self.rq = RequestFactory()

  def test_view(self):
    with open('test_data/images.jpg', 'rb') as img:
      # Post image to the view
      req = self.rq.post('my_view_url', {'my_post': 'data', 'test': 1, 'myfile': img})
      resp = views.index(req)
      # Remove the image after testing
      if os.path.exists("media/images.jpg"):
        os.remove("media/images.jpg")
      # If image gets uploaded the status_code should be 200
      self.assertEqual(resp.status_code, 200)

    def test_uploading_non_image_file_errors(self):
      # set up data
      text_file = SimpleUploadedFile('front.txt', b'this is some text - not an image')
      # Post the dummy text data to the view
      req = self.rq.post('my_view_url', {'my_post': 'data', 'test': 1, 'myfile': text_file})
      resp = views.index(req)
      # If the image does not get uploaded will get 400
      self.assertEqual(resp.status_code, 400)