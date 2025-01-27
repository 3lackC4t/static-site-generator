from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main() -> None:
    new_node = TextNode("This is a text node", TextType.BOLD, "https://node.rip")
    print(new_node)
    properties = {"href": "styles.css", "src": "scripts.js", "target": "_blank"}
    new_html_node = HTMLNode(props=properties)
    print(new_html_node.props_to_html())
    print(new_html_node)


if __name__ == "__main__":
    main()
