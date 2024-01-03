from __future__ import annotations

from typing import TYPE_CHECKING

from gradio_client.documentation import document, set_documentation_group

from gradio.blocks import BlockContext
from gradio.component_meta import ComponentMeta

if TYPE_CHECKING:
    from gradio.components.base import Component


set_documentation_group("layout")


@document()
class Accordion(BlockContext, metaclass=ComponentMeta):
    """
    Accordion is a layout element which can be toggled to show/hide the contained content.
    Example:
        with gr.Accordion("See Details"):
            gr.Markdown("lorem ipsum")
    """

    EVENTS = []

    def __init__(
        self,
        label: str | None = None,
        *,
        open: bool = True,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        components: str | Component | list[Component | str] | None = None
    ):
        """
        Parameters:
            label: name of accordion section.
            open: if True, accordion is open by default.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional string or list of strings that are assigned as the class of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, this layout will not be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            components: If component(s) are supplied, then they are automatically rendered within the accordion. This provides an alterative to the context-based syntax (`with gr.Accordion...`) that can be used with a `gr.Interface()` to render input or output components within accordions.
        """
        from gradio.components import get_component_instance
        from gradio.components.base import Component

        self.label = label
        self.open = open
        if components is None:
            self.components = []
        elif isinstance(components, (Component, str)):
            self.components = [get_component_instance(components, unrender=True)]
        elif isinstance(components, list):
            self.components = [get_component_instance(comp, unrender=True) for comp in components]
        else:
            raise ValueError("The parameter to `components` must be a Component or list of Components")
        BlockContext.__init__(
            self,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
        )
        with self:
            for component in self.components:
                component.render()
