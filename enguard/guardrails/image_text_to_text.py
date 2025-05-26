from enguard.configs.base import ImageTextToTextGuardrailConfig
from enguard.guardrails.base import BaseGuardrail


class ImageTextToTextGuardrail(BaseGuardrail):
    def __init__(self, config: ImageTextToTextGuardrailConfig) -> None:
        super().__init__()
