from django.test import TestCase

# Create your tests here.
from timetrack.models import Company


class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(name="McDonalds")
        Company.objects.create(name="BurgerKing")

    def test_company_exists(self):
        #  This test will check if company really exists
        mcDonalds = Company.objects.get(name="McDonalds")
        bk = Company.objects.get(name="BurgerKing")

        self.assertEqual(mcDonalds.name, 'McDonalds')
        self.assertEqual(bk.name, 'BurgerKing')
