import unittest

from htmlnode import HTMLNode, LeafNode


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
        result_str = ' src="script.js" href="styles.css" target="_blank"'

        self.assertEqual(node.props_to_html(), result_str)

    def test_full_html_node_output(self):
        node = LeafNode(
            tag="h1",
            value="The Final Heading",
            props={
                "style": "color: red; font_weight: heavy;",
                "required": "",
                "class": "leaf-test",
                "id": "leaf-id",
            },
        )

        result_str = '<h1 style="color: red; font_weight: heavy;" required class="leaf-test" id="leaf-id">The Final Heading</h1>'
        self.assertEqual(node.to_html(), result_str)


if __name__ == "__main__":
    unittest.main()
