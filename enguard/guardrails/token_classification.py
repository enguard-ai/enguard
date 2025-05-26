from enguard.configs.base import TextGenerationGuardrailConfig
from enguard.guardrails.base import BaseGuardrail


class TokenClassificationGuardrail(BaseGuardrail):
    def __init__(self, config: TextGenerationGuardrailConfig) -> None:
        super().__init__()
