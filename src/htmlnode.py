class HTMLNode:
    def __init__(
        self,
        tag,
        value=None,
        children=None,
        props=None,
    ) -> None:
        # TODO:  Add logic to log a misssing HTML tag
        self.tag = tag
        self.children = children
        self.value = value
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        if self.props:
            result = []
            for property in self.props:
                if self.props[property] == "":
                    result.append(property)
                else:
                    result.append(f'{property}="{self.props[property]}"')

            return f" {' '.join(result).rstrip()}"
        else:
            return ""

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.children}, {self.value}, {self.props})"

    def __eq__(self, node):
        if not isinstance(node, HTMLNode):
            return False

        if self.tag != node.tag:
            return False

        if self.value != node.value:
            return False

        if self.props != node.props:
            return False

        if self.children == node.children == None:
            return True

        if self.children == None or node.children == None:
            return False

        if len(self.children) == len(node.children):
            return all(
                child == other for child, other in zip(self.children, node.children)
            )
        else:
            return False


class LeafNode(HTMLNode):
    def __init__(self, tag, children=None, value=None, props=None) -> None:
        super().__init__(tag=tag, children=None, value=value, props=props)

    def to_html(self):
        if not self.tag:
            print(f"Node does not contain a tag. Skipping")
            return ""

        if self.value:
            if not self.tag:
                return f"{self.value}"

            properties = self.props_to_html()
            return f"<{self.tag}{properties}>{self.value}</{self.tag}>"
        else:
            properties = self.props_to_html()
            return f"<{self.tag}{properties}></{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None) -> None:
        super().__init__(tag=tag, children=children, value=None, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError(f"Error: Missing tag for parent Node {print(self)}")

        if not self.children:
            raise ValueError(
                f"Error: Parent Nodes must have children. No child nodes found for node {print(self)}"
            )

        result = ""

        for child in self.children:
            if isinstance(child, LeafNode) or isinstance(child, ParentNode):
                result += child.to_html()

        return f"<{self.tag}>{result}</{self.tag}>"
