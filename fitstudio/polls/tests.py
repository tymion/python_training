from django.test import TestCase

from .models import Country, Voivodship

class CountryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Country.objects.create(
                name_text = 'Poland',
                code_int = 616,
                code_alpha_2_text = 'PL',
                code_alpha_3_text = 'POL'
                )

    def test_country_name(self):
        country = Country.objects.get(id = 1)
        expected_str = country.name_text
        self.assertEquals(expected_str, str(country))

class VoivodshipModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        country = Country.objects.create(
                name_text = 'Poland',
                code_int = 616,
                code_alpha_2_text = 'PL',
                code_alpha_3_text = 'POL'
                )
        Voivodship.objects.create(
                name_text = 'Mazowieckie',
                code_int = 14,
                country_key = country
                )

    def test_voivodship_name(self):
        country = Country.objects.get(id = 1)
        voivodship = Voivodship.objects.get(id = 1)
        expected_str = "{0} ({1})".format(voivodship.name_text, country.name_text)
        self.assertEquals(expected_str, str(voivodship))
