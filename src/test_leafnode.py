import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_init_empty(self):
        node = LeafNode(tag="p", value="Hello")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_props(self):
        props = {"class": "container", "id": "main"}
        node = LeafNode(tag="div", value="Hello", props=props)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello")
        self.assertIsNone(node.children)
        self.assertEqual(node.props, props)

    def test_repr_basic(self):
        node = LeafNode(tag="p", value="Hello")
        self.assertEqual(repr(node), "LeafNode(p, Hello, None)")

    def test_repr_with_props(self):
        node = LeafNode(
            tag="div",
            value="Hello",
            props={"class": "greeting"}
        )
        self.assertEqual(repr(node), "LeafNode(div, Hello, {'class': 'greeting'})")

    def test_to_html_basic(self):
        node = LeafNode(tag="p", value="Hello")
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_to_html_with_props(self):
        node = LeafNode(
            tag="div",
            value="Hello",
            props={"class": "greeting", "id": "message"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" id="message">Hello</div>'
        )

    def test_to_html_text_only(self):
        node = LeafNode(tag=None, value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_to_html_no_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception),
            "Invalid HTML: no value"
        )


if __name__ == '__main__':
    unittest.main()