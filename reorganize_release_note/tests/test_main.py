import unittest
from mains.main import reorganize_release_notes


class TestReleaseNotes(unittest.TestCase):
    def test_reorganize_release_notes(self):
        # テスト用の入力
        test_input_md = (
            "## What's Changed\n"
            "* feat: Add new X-feature\n"
            "* fix: Fix A-bug\n"
            "* docs: Update documentation\n"
            "* feat: Add new Y-feature\n"
            "* fix: Fix B-bug\n"
        )

        # 期待される出力
        expected_output_md = (
            "## What's Changed\n"
            "## feat\n"
            "* feat: Add new X-feature\n"
            "* feat: Add new Y-feature\n"
            "## fix\n"
            "* fix: Fix A-bug\n"
            "* fix: Fix B-bug\n"
            "## docs\n"
            "* docs: Update documentation\n"
        )

        # 実際の出力
        actual_output = reorganize_release_notes(test_input_md)

        # 実際の出力と期待される出力を比較
        with self.subTest("リリースノートが整理される"):
            self.assertEqual(actual_output, expected_output_md)


if __name__ == "__main__":
    unittest.main()
