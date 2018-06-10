# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Location,Category,Image
import datetime as dt
# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.test_location = Location(location="nairobi")

    def test_instance(self):
        self.asserTrue(isinstance(self.test_location, Location))

    def test_saving_location(self):
        self.test_location.save_locations()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0) 


    def test_deleting_locations(self):
        self.test_location = Location(location="nairobi")
        self.test_location.save_locations()
        self.test_location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) < 1)




class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category='Food')

    def test_instance(self):
        self.asserTrue(isinstance(self.test, Image))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test = Category(category='Food')
        self.test.save_category()
        self.test.delete_locations()
        locationss = Category.objects.all()
        self.assertTrue(len(locationss) < 1)

