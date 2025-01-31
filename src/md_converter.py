import re

from htmlnode import LeafNode
from textnode import TextNode, TextType


def extract_markdown_images(text):
    link_regex = r"!\[([^\[\]]+)\]\(([^()\s]+)\)"
    return re.findall(link_regex, text)


def extract_markdown_links(text):
    link_regex = r"(?<!!)\[([^\[\]]+)\]\(([^()\s]+)\)"
    return re.findall(link_regex, text)


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


def split_nodes_image(nodes):
    image_tuples = extract_markdown_images(nodes.text)

    result = []
    for pair in image_tuples:
        alt_text, url = pair
        for index, node in enumerate(nodes.text.split(f"![{alt_text}]({url})", 1)):
            if node:
                if index % 2 == 0:
                    result.append(TextNode(node, TextType.NORMAL))
                else:
                    result.append(TextNode(alt_text, TextType.IMAGE, url))
    return result


def split_nodes_link(nodes):
    link_tuples = extract_markdown_links(nodes.text)

    result = []
    for pair in link_tuples:
        link_text, url = pair
        for index, node in enumerate(nodes.text.split(f"![{link_text}]({url})", 1)):
            if node:
                if index % 2 == 0:
                    result.append(TextNode(node, TextType.NORMAL))
                else:
                    result.append(TextNode(link_text, TextType.LINK, url))
    return result


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not text_type == TextType.NORMAL:
        return old_nodes

    potential_nodes = old_nodes.text.split(delimiter)

    if len(potential_nodes) % 2 == 0:
        return old_nodes

    result = []

    for node_index in range(len(potential_nodes)):
        if potential_nodes[node_index]:
            if node_index % 2 == 0:
                result.append(TextNode(potential_nodes[node_index], TextType.NORMAL))
            else:
                match delimiter:
                    case "**":
                        result.append(
                            TextNode(potential_nodes[node_index], TextType.BOLD)
                        )
                    case "*":
                        result.append(
                            TextNode(potential_nodes[node_index], TextType.ITALIC)
                        )
                    case "_":
                        result.append(
                            TextNode(potential_nodes[node_index], TextType.ITALIC)
                        )
                    case "`":
                        result.append(
                            TextNode(potential_nodes[node_index], TextType.CODE)
                        )
    return result
