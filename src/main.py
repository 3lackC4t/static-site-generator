from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType


def main() -> None:
    properties = {"href": "styles.css", "src": "scripts.js", "target": "_blank"}
    leaf = LeafNode(tag="p", value="This is text", props=properties)
    print(leaf.to_html())


if __name__ == "__main__":
    main()
