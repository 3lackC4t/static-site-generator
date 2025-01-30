from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text="", text_type=TextType.NORMAL, url="") -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        text_eq = self.text == node.text
        type_eq = self.text_type = node.text_type
        url_eq = self.url == node.url

        return text_eq and type_eq and url_eq

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
