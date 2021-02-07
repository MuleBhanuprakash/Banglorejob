from django.test import TestCase
from .models import Address


# Create your tests here.

class AddressTest(TestCase):
    def setup(self):
        self.address = Address.objects.create(Name='Bhanu', Job='developer',
                                              Address1='line5', Address2='srinivasa nagar',
                                              Area='srnagar', City='hyderabad', Country='india',
                                              Pincode='509103')
        return self.address

    def testAddress(self):
        d = self()
        self.assertTrue(isinstance(d, Address))
        self.assertEqual(str(d.Name), 'Bhanu')
