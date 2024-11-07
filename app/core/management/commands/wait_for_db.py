"""
Django command to wait for the database to be available
"""
import time
# Error thrown by psycopg2 sometimes when the db is not ready
from psycopg2 import OperationalError as Psycopg2OpError

# Error that django throws when the db isn't ready
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
