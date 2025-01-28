from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main() -> None:
    properties = {"href": "styles.css", "src": "scripts.js", "target": "_blank"}
    leaf = LeafNode(tag="p", value="This is text", props=properties)
    print(leaf.to_html())

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())


if __name__ == "__main__":
    main()
