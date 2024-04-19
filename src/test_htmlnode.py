import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(None, None, None, {"href": "https://www.google.com", "target": "_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_repr(self):
        node = HTMLNode("p", 
            "This is text in a paragraph", 
            ["child1", "child2"], 
            {"href": "https://www.google.com", "target": "_blank"}
                        )
        expected_result = "p, This is text in a paragraph, ['child1', 'child2'], {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(repr(node), expected_result)

    def test_to_html(self):
        node = LeafNode("p", 
            "This is a paragraph of text.",
            {})
        expected_result = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_result)
        

if __name__ == "__main__":
    unittest.main()