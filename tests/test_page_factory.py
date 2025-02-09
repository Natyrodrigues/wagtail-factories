import pytest
from wagtail_factories.blocks import RichTextBlockFactory

def test_default_richtextblock():

    result = RichTextBlockFactory()
    assert isinstance(result, str)
    assert result.startswith("<p>")
    assert result.endswith("</p>")

def test_richtextblock_with_custom_text():

    custom_text = "Hello, Rich Text!"
    result = RichTextBlockFactory(text=custom_text)
    assert result == f"<p>{custom_text}</p>"

def test_richtextblock_with_custom_wrapper():
    custom_text = "Wrapper Test"
    wrapper = "div"
    result = RichTextBlockFactory(text=custom_text, wrapper=wrapper)
    assert result == f"<{wrapper}>{custom_text}</{wrapper}>"

    