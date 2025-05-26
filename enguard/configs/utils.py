from enguard.configs.base import TextClassificationGuardrail
from enguard.configs.text_classification import TEXT_CLASSIFICATION_GUARDRAILS


def get_guardrails_from_architecture(
    architecture: str,
) -> TextClassificationGuardrail:
    potential_guardrails = []
    for guardrail in TEXT_CLASSIFICATION_GUARDRAILS:
        if guardrail.name == architecture:
            potential_guardrails.append(guardrail)
    if len(potential_guardrails) == 0:
        raise ValueError(f"Guardrail for architecture {architecture} not found")
    return potential_guardrails


def get_guardrail_from_type(
    guardrail_type: AVAILABLE_GUARDRAIL_TYPES,
) -> BaseGuardrail:
    for guardrail in TEXT_CLASSIFICATION_GUARDRAILS:
        if guardrail.guardrail_type == guardrail_type:
            return guardrail
    raise ValueError(f"Guardrail type {guardrail_type} not found")
