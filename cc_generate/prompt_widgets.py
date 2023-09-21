
from prompt_toolkit.formatted_text import AnyFormattedText
from typing import Any, Sequence, TypeVar
from prompt_toolkit.styles import BaseStyle
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.layout import Layout
from prompt_toolkit.layout.containers import AnyContainer, HSplit, VSplit
from prompt_toolkit.key_binding.key_bindings import KeyBindings, merge_key_bindings
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.widgets import (
    Button,
    CheckboxList,
    Label,
)


_T = TypeVar("_T")

def checkboxlist_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "Ok",
    cancel_text: str = "Cancel",
    values: Sequence[tuple[_T, AnyFormattedText]] | None = None,
    default_values: Sequence[_T] | None = None,
) -> Application[list[_T]]:
    """
    Display a simple list of element the user can choose multiple values amongst.

    Several elements can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
    if values is None:
        values = []

    def ok_handler() -> None:
        get_app().exit(result=cb_list.current_values)

    cb_list = CheckboxList(values=values, default_values=default_values)

    dialog = HSplit([
            Label(title),
            HSplit(
                [Label(text=text, dont_extend_height=True), cb_list],
                padding=1,
            ),
            VSplit([
                Button(text=ok_text, handler=ok_handler),
                Button(text=cancel_text, handler=_return_none),
            ]),
        ]
    )

    return _create_app(dialog, None)


def _create_app(dialog: AnyContainer, style: BaseStyle | None) -> Application[Any]:
    # Key bindings.
    bindings = KeyBindings()
    bindings.add("tab")(focus_next)
    bindings.add("s-tab")(focus_previous)

    return Application(
        layout=Layout(dialog),
        key_bindings=merge_key_bindings([load_key_bindings(), bindings]),
        mouse_support=True,
        style=style,
        full_screen=False,
    )


def _return_none() -> None:
    "Button handler that returns None."
    get_app().exit()
