#!/usr/bin/python
# Deploy the MyBook application to the Web Faction server

from django.core.management.base    import BaseCommand
from livebook.test_content import test_contents
from livebook.test_hyperlink import test_hyperlink

class Command(BaseCommand):
    test_contents()
    test_hyperlink()

    exit(0)
