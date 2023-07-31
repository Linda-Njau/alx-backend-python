#!/usr/bin/env python3
"""test file for utilis"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access nested map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_result):
        """Tests for the output of access nested map function"""
        actual_result = access_nested_map(map, path)
        self.assertEqual(expected_result, actual_result)
