from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema.message import Message


class CombineTextComponent(Component):
    display_name = "Combine Text"
    description = (
        "Concatenate three text sources into a single text chunk with the delimiter "
    )
    icon = "merge"
    name = "CombineText"

    inputs = [
        MessageTextInput(
            name="text1",
            display_name="First Text",
            info="The first text input to concatenate.",
        ),
        MessageTextInput(
            name="text2",
            display_name="Second Text",
            info="The second text input to concatenate.",
        ),
        MessageTextInput(
            name="text3",
            display_name="Third Text",
            info="The third text input to concatenate.",
        ),
    ]

    outputs = [
        Output(display_name="Combined Text", name="combined_text", method="combine_texts"),
    ]

    def combine_texts(self) -> Message:
        # Delimiter is always '------' across the page with space above and below
        delimiter = "\n\n"
        combined = delimiter.join(
            [
                self.text1,
                self.text2,
                self.text3,
            ]
        )
        self.status = combined
        return Message(text=combined)