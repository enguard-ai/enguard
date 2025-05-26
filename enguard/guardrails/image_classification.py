from enguard.configs.base import ImageClassificationGuardrailConfig
from enguard.guardrails.base import BaseGuardrail


class ImageClassificationGuardrail(BaseGuardrail):
    def __init__(self, config: ImageClassificationGuardrailConfig) -> None:
        super().__init__()
