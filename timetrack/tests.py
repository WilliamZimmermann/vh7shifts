from django.test import TestCase

# Create your tests here.
from timetrack.models import Company, Location


class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(name="McDonalds")
        Company.objects.create(name="BurgerKing")

    def test_company_exists(self):
        #  This test will check if company really exists
        mc_donalds = Company.objects.get(name="McDonalds")
        bk = Company.objects.get(name="BurgerKing")

        self.assertEqual(mc_donalds.name, 'McDonalds')
        self.assertEqual(bk.name, 'BurgerKing')


class CompanyLocationTestCase(TestCase):
    # Tests for the model Company

    def setUp(self):
        # Set up 2 companies to make tests
        company = Company.objects.create(name="StarBucks")
        Location.objects.create(
            id=25753,
            company=company,
            address="7shifts Brazil",
            city="São Paulo",
            country="US",
            lat="34.0522342",
            lng="-118.2436849",
            state="CA",
            timezone="America/Sao_Paulo",
            dailyOvertimeMultiplier=1.5,
            dailyOvertimeThreshold=480,
            overtime=True,
            weeklyOvertimeMultiplier=2,
            weeklyOvertimeThreshold=2400
        )

        company = Company.objects.create(name="Wolly")
        Location.objects.create(
            id=25453,
            company=company,
            address="90 Street",
            city="Saskatchwan",
            country="US",
            lat="34.0522342",
            lng="-118.2436849",
            state="CA",
            timezone="America/Canada",
            dailyOvertimeMultiplier=2.0,
            dailyOvertimeThreshold=400,
            overtime=True,
            weeklyOvertimeMultiplier=2,
            weeklyOvertimeThreshold=2400
        )

    def test_location_exists(self):
        # Test if 2 created locations really exists in database
        location_a = Location.objects.get(id=25753)
        location_b = Location.objects.get(id=25453)
        self.assertEqual(location_a.address, '7shifts Brazil')
        self.assertEqual(location_b.address, '90 Street')

