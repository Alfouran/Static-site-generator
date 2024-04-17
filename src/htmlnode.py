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
        for key, value in self.props.items():
            key_value += f" {key}={value}"
        return key_value
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"
        

