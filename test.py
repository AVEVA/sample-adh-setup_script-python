"""This script tests the setup script"""

import unittest

from program import cleanup, readAppsettings, run, setup


class SampleE2ETests(unittest.TestCase):
    """Tests for the setup script sample"""

    @classmethod
    def test_end_to_end(cls):
        """End to end test for main function"""
        appsettings = readAppsettings()

        setup(appsettings)
        run(appsettings, True)
        cleanup(appsettings)


if __name__ == '__main__':
    unittest.main()
