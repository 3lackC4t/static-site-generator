import md_converter
from htmlnode import HTMLNode, LeafNode, ParentNode
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

    test_node = TextNode(
        "This is an image ![image text](url_for_image) Disregard", TextType.NORMAL
    )

    test_result = md_converter.extract_markdown_images(
        "This is an image ![image_text](url_for_image) disregard"
    )

    print(test_result)

    result_list = md_converter.split_nodes_image(test_node)

    for node in result_list:
        print(node)


if __name__ == "__main__":
    main()
