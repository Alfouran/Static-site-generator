import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode


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

    def test_to_html_parent(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"),
                                      LeafNode(None, "Normal text"),
                                      LeafNode("i", "italic text"),
                                      LeafNode(None, "Normal text")
                                      ])
        expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_result)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html_node(self):
        # TextNode with plain text
        text_node = TextNode("Just some text", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.value, "Just some text")
        self.assertIsNone(html_node.tag, "Expected null tag for plain text")

    def test_text_to_html_node_bold(self):
        # TextNode with bold text
        text_node = TextNode("Some bold text", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Some bold text")

    def test_text_to_html_node_italic(self):
        # TextNode with italic text
        text_node = TextNode("Some italic text", "italic")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Some italic text")

    def test_text_to_html_node_code(self):
        # TextNode with code text
        text_node = TextNode("Some code text", "code")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Some code text")

    def test_text_to_html_node_link(self):
        # TextNode with a link
        text_node = TextNode("Its a link", "link", url="https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Its a link")
        self.assertEqual(html_node.props['href'], "https://www.google.com")

    def test_text_to_html_node_image(self):
        #TextNode with an image
        text_node = TextNode("Alt text", "image", url="https://www.its_a_picture.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props['src'], "https://www.its_a_picture.com")

        

if __name__ == "__main__":
    unittest.main()