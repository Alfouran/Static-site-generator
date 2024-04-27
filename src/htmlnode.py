TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        key_value = ""
        if not self.props:
            return ""
        for key, value in self.props.items():
            key_value += f' {key}="{value}"'
        return key_value
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
        
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value cannot be None")
        if self.tag == None:
            return f"{self.value}"
        attrs_str = self.props_to_html()
        return f"<{self.tag}{attrs_str}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag present")
        if not self.children:
            raise ValueError("No children present")
        html_content = ""
        for child in self.children:
            html_content += child.to_html()
        return f"<{self.tag}>{html_content}</{self.tag}>"
        

def text_node_to_html_node(text_node):
    node_type = text_node.text_type

    if node_type == TEXT_TYPE_TEXT:
        return LeafNode(value=text_node.text)
    elif node_type == TEXT_TYPE_BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif node_type == TEXT_TYPE_ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif node_type == TEXT_TYPE_CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif node_type == TEXT_TYPE_LINK:
        props = {"href": text_node.url}
        return LeafNode(tag="a", value=text_node.text, props=props)
    elif node_type == TEXT_TYPE_IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode(tag="img", value="", props=props)
    else:
        raise Exception("Unsupported text type provided")

               
