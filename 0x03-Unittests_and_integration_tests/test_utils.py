#!/usr/bin/env python3
"""test file for utilis"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access nested map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Tests for the output of access nested map function"""
        actual_result = access_nested_map(nested_map, path)
        self.assertEqual(expected_result, actual_result)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, wrong_output):
        """Test if keyError is raised"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(wrong_output, error.exception)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test Memoize decorator"""

    def test_memoize(self):
        """tests if Memoize is called once"""
        class TestClass:
            """Test class for Memoize"""

            def a_method(self):
                """Test method"""
                return 42

            @memoize
            def a_property(self):
                """decorated Test method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_obj:
            obj = TestClass()
            obj.a_property
            obj.a_property
            mock_obj.assert_called_once()
