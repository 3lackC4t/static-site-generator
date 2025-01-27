from textnode import TextNode, TextType


def main() -> None:
    new_node = TextNode("This is a text node", TextType.BOLD, "https://node.rip")


if __name__ == "__main__":
    main()
