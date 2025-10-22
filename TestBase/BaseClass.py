from robot.api.deco import keyword
import os


class BaseClass:

    def __init__(self):
        # Get the parent directory of the project correctly
        # BaseClass.py is in TestBase/, so project root is one level up
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Correct path to Resources/config.properties
        self.config_file = os.path.join(project_root, "Resources", "config.properties")
        self.config = self._read_properties()

    def _read_properties(self):
        props = {}
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        with open(self.config_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key_value = line.split("=", 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        props[key.strip()] = value.strip()
        return props

    @keyword
    def fetch_property(self, key):
        return self.config.get(key, None)
