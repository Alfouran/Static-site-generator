from textnode import TextNode

TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"


def main():
    node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node1)

if __name__ == "__main__":
    main()