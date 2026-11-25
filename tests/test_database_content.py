import os
import sqlite3
import tempfile
import unittest

from services import database
from config import Config


class DatabaseContentTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.original_db = Config.DATABASE_PATH
        Config.DATABASE_PATH = os.path.join(self.tmpdir.name, "test_skyfall.db")
        database.init_db()

    def tearDown(self):
        Config.DATABASE_PATH = self.original_db
        self.tmpdir.cleanup()

    def test_seeded_services_and_instagram_posts(self):
        services = database.get_services()
        self.assertGreaterEqual(len(services), 6)
        self.assertEqual(services[0]["title"], "LIVE SOUND")

        posts = database.get_instagram_posts()
        self.assertGreaterEqual(len(posts), 3)
        self.assertTrue(any(post["post_url"].endswith("DExrrUZMbsM/") for post in posts))


if __name__ == "__main__":
    unittest.main()
