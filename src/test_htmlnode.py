import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode(
            tag="<p>",
            value="test",
            children=[HTMLNode(tag="p")],
            props={"src": "script.js"},
        )
        node2 = HTMLNode(
            tag="<p>",
            value="test",
            children=[HTMLNode(tag="p")],
            props={"src": "script.js"},
        )
        self.assertEqual(node1, node2)

    def test_neq(self):
        node1 = HTMLNode(tag="", props={"href": "styles.css"})
        node2 = HTMLNode(tag="<p>")
        self.assertNotEqual(node1, node2)

    def test_props_to_html(self):
        node = HTMLNode(tag="<p>")
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

    def test_recursive_parent_to_html(self):
        node = ParentNode(
            tag="div",
            children=[
                LeafNode(tag="h1", value="A List"),
                ParentNode(
                    tag="ul",
                    children=[
                        LeafNode(tag="li", value="Item 1"),
                        LeafNode(tag="li", value="Item 2"),
                        LeafNode(tag="li", value="Item 3"),
                    ],
                ),
            ],
        )

        result = "<div><h1>A List</h1><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        self.assertEqual(node.to_html(), result)

    def test_empty_parent_node(self):
        node = ParentNode(tag="p", children=[LeafNode(tag="p")])
        self.assertEqual(node.to_html(), "<p><p></p></p>")


if __name__ == "__main__":
    unittest.main()
