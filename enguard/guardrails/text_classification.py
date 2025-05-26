from typing import Dict, List

from transformers import pipeline

from enguard.configs.base import (
    TextClassificationGuardrailConfig,
)
from enguard.guardrails.base import BaseGuardrail


class TextClassificationGuardrail(BaseGuardrail):
    def __init__(
        self,
        config: TextClassificationGuardrailConfig,
        **kwargs,
    ):
        self.model = pipeline(
            task="text-classification",
            model=config.name,
            **kwargs,
        )

    def __call__(
        self,
        text_or_messages: str | List[Dict[str, str]] | List[str | List[Dict[str, str]]],
    ) -> str:
        return
