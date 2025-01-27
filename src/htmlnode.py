class HTMLNode:
    def __init__(
        self,
        tag=None,
        value=None,
        children=None,
        props=None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        if self.props:
            result = " ".join(
                [f'{property}="{self.props[property]}"' for property in self.props]
            )

            return result.rstrip()
        else:
            raise Exception("HTMLNode has no properties")

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

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
