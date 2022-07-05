"""
Lookup tables for function memoisation
"""
import json


class LookupTable(dict):
    """
    Dict object extended to include reading and writing from file
    """
    def __init__(self, filepath: str):
        self.filepath = filepath
        super().__init__(self._get_dict())
        self.changed = False

    # def __del__(self):
    #     """
    #     Save changes to local file only if changes have been made
    #     'Broken' from Python 3.4 onwards -- use context manager instead
    #     """
    #     if self.changed:
    #         self.save()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.changed:
            self.save()

    def _get_dict(self):
        with open(self.filepath) as file:
            return json.load(file)

    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self, file, indent=4)

    def add(self, key, value):
        self[key] = value
        self.changed = True
