import unittest

from md_converter import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    text_node_to_html_node,
)
from textnode import TextNode, TextType


class TestNodeConverter(unittest.TestCase):

    def node_to_html_test(self):
        node = TextNode("test of text node", TextType.NORMAL)
        self.assertEqual(node.text, text_node_to_html_node(node).to_html())

    def test_md_to_html_bold(self):
        text_node = TextNode(
            "**This** is not **Bold** but **This** is", TextType.NORMAL
        )

        exp_result = [
            TextNode("This", TextType.BOLD),
            TextNode("is not", TextType.NORMAL),
            TextNode("Bold", TextType.BOLD),
            TextNode("but", TextType.NORMAL),
            TextNode("This", TextType.BOLD),
            TextNode("is", TextType.NORMAL),
        ]

        act_result = split_nodes_delimiter(text_node, "**", TextType.NORMAL)

        self.assertEqual(len(exp_result), len(act_result))

        for index, node in enumerate(act_result):
            self.assertEqual(
                text_node_to_html_node(node).to_html(),
                text_node_to_html_node(exp_result[index]).to_html(),
            )

    def test_image_text(self):
        string_to_be_tested = "[Hello] this is ![image_text](url) with a lot of !(traps) inside ![Don't worry] the [regex ]( should!) only return '(image_text, url)'"

        self.assertEqual(
            extract_markdown_images(string_to_be_tested), [("image_text", "url")]
        )

    def test_link_text(self):
        string_to_be_tested = "[Hello] this is [a](link) that should only ![return](one) line which is '(a, link)'"
        self.assertEqual(extract_markdown_links(string_to_be_tested), [("a", "link")])
