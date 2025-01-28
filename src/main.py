from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node):
    t_type = text_node.text_type
    t_text = text_node.text
    if t_type == "normal":
        return LeafNode(value=t_text)
    elif t_type == "bold":
        return LeafNode(tag="b", value=t_text)
    elif t_type == "italic":
        return LeafNode(tag="i", value=t_text)
    elif t_type == "code":
        return LeafNode(tag="code", value=t_text)
    elif t_type == "link":
        return LeafNode(tag="a", value=t_text, props={"href": text_node.url})
    elif t_type == "image":
        return LeafNode(
            tag="img", value="", props={"src": text_node.url, "alt": t_text}
        )


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
