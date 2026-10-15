"""Offline source-tree checks; not a substitute for Flutter integration tests."""
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class FlutterProjectContracts(unittest.TestCase):
    def test_manifest_assets_exist_with_portable_separators(self):
        spec = (ROOT / "pubspec.yaml").read_text(encoding="utf-8")
        assets = re.findall(r"^\s+- (assets/[^\r\n]+)$", spec, re.MULTILINE)
        self.assertTrue(assets, "No asset entries found")
        self.assertNotIn("\\", "\n".join(assets))
        for relative_path in assets:
            self.assertTrue((ROOT / relative_path.strip()).is_file(), relative_path)

    def test_local_signin_state_uses_same_preference_key(self):
        src = (ROOT / "lib/provider/auth_provider.dart").read_text(encoding="utf-8")
        read = re.search(r'getBool\("([^"]+)"\)', src)
        write = re.search(r'setBool\("([^"]+)",\s*true\)', src)
        self.assertIsNotNone(read)
        self.assertIsNotNone(write)
        self.assertEqual(read.group(1), write.group(1))
        self.assertIn('await s.setBool(', src)


if __name__ == "__main__":
    unittest.main()
