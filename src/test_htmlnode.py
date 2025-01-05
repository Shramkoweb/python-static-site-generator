import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_init_empty(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_init_with_parameters(self):
        tag = "div"
        value = "Hello"
        children = [HTMLNode(tag="p", value="Child")]
        props = {"class": "container", "id": "main"}

        node = HTMLNode(tag=tag, value=value, children=children, props=props)

        self.assertEqual(node.tag, tag)
        self.assertEqual(node.value, value)
        self.assertEqual(node.children, children)
        self.assertEqual(node.props, props)

    def test_repr_empty(self):
        node = HTMLNode()
        # TODO: think about an empty repl
        self.assertEqual(repr(node), "HTMLNode(tag:None, value:None, children:None, props:None)")

    def test_repr_full(self):
        node = HTMLNode(
            tag="div",
            value="Hello",
            children=[HTMLNode(tag="span", value="World")],
            props={"class": "greeting"}
        )
        # TODO: Fragile. Think about to make more robust variant
        expected = "HTMLNode(tag:div, value:Hello, children:[HTMLNode(tag:span, value:World, children:None, props:None)], props:{'class': 'greeting'})"
        self.assertEqual(repr(node), expected)

    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()
        self.assertEqual(
            str(context.exception),
            "to_html method not implemented"
        )

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "container", "id": "main"})
        self.assertEqual(
            node.props_to_html(),
            ' class="container" id="main"'
        )

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")


if __name__ == '__main__':
    unittest.main()
