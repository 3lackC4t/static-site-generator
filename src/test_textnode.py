import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_null_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is not a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_null_types(self):
        node = TextNode(text="This is a text node", url="https://example.com")
        node2 = TextNode("This is not a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_null_text(self):
        node = TextNode(text_type=TextType.BOLD, url="https://example.com")
        node2 = TextNode("This is not a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
