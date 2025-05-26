from enguard.configs.base import (
    AVAILABLE_GUARDRAIL_TYPES,
    BaseGuardrailConfig,
    TextClassificationGuardrail,
)

GUARDRAILS = [
    TextClassificationGuardrail(
        name="meta-llama/Prompt-Guard-86M",
        guardrail_types=["prompt_injection", "jailbreak"],
    )
]


for guardrail in GUARDRAILS:
    assert all(
        guardrail_type in AVAILABLE_GUARDRAIL_TYPES
        for guardrail_type in guardrail.guardrail_types
    )


def get_guardrail_from_type(
    guardrail_type: AVAILABLE_GUARDRAIL_TYPES,
) -> BaseGuardrailConfig:
    for guardrail in GUARDRAILS:
        if guardrail_type in guardrail.guardrail_types:
            return guardrail
    raise ValueError(f"Guardrail type {guardrail_type} not found")
