import unittest
from unittest.mock import patch, MagicMock


from ..session import (
    SESSION_STORAGE,
    user_asked_to_consent_for_project,
    add_project_to_asked_to_consent,
    is_initial_analysis_ran_for_project,
    add_project_to_initial_analysis_ran_list,
)


class TestUtils(unittest.TestCase):
    def test_set_and_get_user_asked_for_consent(self):
        test_path = "/not-existent"
        should_be_false = user_asked_to_consent_for_project(test_path)
        self.assertEqual(should_be_false, False)
        add_project_to_asked_to_consent(test_path)
        should_be_true = user_asked_to_consent_for_project(test_path)
        self.assertEqual(should_be_true, True)

    def test_set_and_get_project_initial_analysis_ran(self):
        test_path = "/not-existent"
        should_be_false = is_initial_analysis_ran_for_project(test_path)
        self.assertEqual(should_be_false, False)
        add_project_to_initial_analysis_ran_list(test_path)
        should_be_true = is_initial_analysis_ran_for_project(test_path)
        self.assertEqual(should_be_true, True)


if __name__ == "__main__":
    unittest.main()
