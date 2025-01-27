import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        child_node = HTMLNode()
        node1 = HTMLNode(
            tag="<p>", value="test", children=[child_node], props={"src": "script.js"}
        )
        node2 = HTMLNode(
            tag="<p>", value="test", children=[child_node], props={"src": "script.js"}
        )
        self.assertEqual(node1, node2)

    def test_neq(self):
        node1 = HTMLNode(props={"href": "styles.css"})
        node2 = HTMLNode(tag="<p>")
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node = HTMLNode()
        properties = {
            "src": "script.js",
            "href": "styles.css",
            "target": "_blank",
        }
        node.props = properties
        result_str = 'src="script.js" href="styles.css" target="_blank"'

        self.assertEqual(node.props_to_html(), result_str)


if __name__ == "__main__":
    unittest.main()
