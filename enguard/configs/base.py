from typing import Literal

from pydantic import BaseModel

AVAILABLE_ROLES = Literal["user", "assistant", "generic"]
AVAILABLE_GUARDRAIL_TYPES = Literal["prompt_injection", "jailbreak"]


class BaseGuardrailConfig(BaseModel):
    name: str
    description: str = ""
    role_index: AVAILABLE_ROLES


class TextClassificationGuardrailConfig(BaseGuardrailConfig):
    guardrail_type: Literal["text_classification"] = "text_classification"
    positive_labels: list[str]
    negative_labels: list[str]


class ImageClassificationGuardrailConfig(BaseGuardrailConfig):
    guardrail_type: Literal["text_classification"] = "text_classification"
    positive_labels: list[str]
    negative_labels: list[str]


class TokenClassificationGuardrailConfig(BaseGuardrailConfig):
    guardrail_type: Literal["token_classification"] = "token_classification"
    positive_labels: list[str]
    negative_labels: list[str]


class TextGenerationGuardrailConfig(BaseGuardrailConfig):
    guardrail_type: Literal["text_generation"] = "text_generation"


class ImageTextToTextGuardrailConfig(BaseGuardrailConfig):
    guardrail_type: Literal["image_text_to_text"] = "image_text_to_text"
    positive_labels: list[str]
    negative_labels: list[str]
