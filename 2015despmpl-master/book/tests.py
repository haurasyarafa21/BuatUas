from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from book.views import home_page
from book.models import Item 

class TestFunction(TestCase):
    
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.name = 'FirstContact'
        first_item.number = '090909090'
        first_item.save()
	
        second_item = Item()
        second_item.name = 'SecondContact'
        second_item.number = '080808080'
        second_item.save()
	
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
	
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'FirstContact')
        self.assertEqual(first_saved_item.number, '090909090')
        self.assertEqual(second_saved_item.name, 'SecondContact')
        self.assertEqual(second_saved_item.number, '080808080')

    def test_layout_and_styling(self):
        //unit test java script 1
        self.assertIn('The Address Phone', self.browser.title)
        self.assertIn('My Address Phone', header_text)
        self.browser.set_window_size(1024, 768)
        //kelar

        //unit test styling    
        inputbox = self.browser.find_element_by_id('id_new_name')
        inputbox2 = self.browser.find_element_by_id('id_new_number')

        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 
            512,
            delta=5
        )

        self.assertAlmostEqual(
            inputbox2.location['x'] + inputbox.size['width'] / 2, 
            512,
            delta=5
        )

        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Masukkan nama'
        )

        self.assertEqual(
            inputbox2.get_attribute('placeholder'),
            'Masukkan nomor telepon'
        )

    def test_search_items(self):
        nama = Item.objects.create(name=request.POST['name_text'])
        nama2 = Item.objects.get(item.name=nama)
        self.assertEqual(nama,nama2)

	
