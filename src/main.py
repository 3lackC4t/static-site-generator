from htmlnode import HTMLNode, LeafNode, ParentNode
from md_converter import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )


def main() -> None:
    properties = {
        "href": "styles.css",
        "src": "script.js",
        "required": "",
    }

    nodes = [
        TextNode("I'm normal text", TextType.NORMAL, url=""),
        TextNode("I am bold text", TextType.BOLD, url=""),
        TextNode("I'm fancy Text", TextType.ITALIC, url=""),
        TextNode("I'm a code block", TextType.CODE, url=""),
        TextNode("This is an anchor (link)", TextType.LINK, url="https://boot.dev"),
        TextNode("This is an image", TextType.IMAGE, url="resources/image.png"),
    ]

    for node in nodes:
        print(text_node_to_html_node(node).to_html())

    test_string = "This is a string that contains **bolded** text"
    split_nodes_delimiter(test_string, "**", TextType.BOLD)

    test_image = "This is a markdown line with an inline image ![Alt Text](https://image_and_stuff.org) and this is also a ![image_text](url)"
    print(extract_markdown_images(test_image))


if __name__ == "__main__":
    main()
