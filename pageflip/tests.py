from django.test import TestCase
from django.urls import reverse

#testing that the index notifies when no books are in the most popular
class IndexTest(TestCase):
    def test_index_no_books(self):
        response = self.client.get(reverse('pageflip:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No books available.')
        self.assertQuerysetEqual(response.context['books'], [])

#testing when there are no books in the books page
class BookTest(TestCase):
    def test_book_no_books(self):
        response = self.client.get(reverse('pageflip:books'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No books available.')
        self.assertQuerysetEqual(response.context['books'], [])