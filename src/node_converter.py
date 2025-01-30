from htmlnode import LeafNode
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
