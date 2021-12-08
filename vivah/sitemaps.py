from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from accounts.models import Profile


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home', 'about', 'faq']

    def location(self, item):
        return reverse(item)


class ProfileSitemap(Sitemap):

    def items(self):
        return Profile.objects.all()
