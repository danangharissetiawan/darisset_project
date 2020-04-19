from selenium import webdriver

from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.utils import formats

from datetime import date

# import unittest


class HomeNewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("Risset", self.browser.title)

    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Page Not Found at robots.txt", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Page Not Found at humans.txt", self.browser.title)

    def test_localization(self):
        today = date.today()
        for lang in ['en', 'id']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(formats.date_format(today, use_l10n=True),
                             local_date.text)
            self.assertEqual(today.strftime('%B %d, %Y'), non_local_date.text)

    def test_time_zone(self):
        for lang in ['en', 'id']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            tz = self.browser.find_element_by_id("time-tz").text
            utc = self.browser.find_element_by_id("time-utc").text
            ny = self.browser.find_element_by_id("time-ny").text
            self.assertNotEqual(tz, utc)
            self.assertNotIn(ny, [tz, utc])

    # def test_internationalization(self):
    #     for lang, 

    # def test_h1_css(self):
    #     self.browser.get(self.get_full_url("home"))
    #     h1 = self.browser.find_element_by_tag_name("h1")
    #     self.assertEqual(h1.value_of_css_property(
    #         "color"), "rgba(200, 50, 255, 1)")

    # def test_it_worked(self):
    #     self.browser.get('http://localhost:8000')
    #     self.assertIn("Django: the Web framework for perfectionists with deadlines.", self.browser.title)

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
