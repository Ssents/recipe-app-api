"""
Django command to wat for the database to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for base"""
    def handle(self, *args, **options):
        pass

