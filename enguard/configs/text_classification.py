from enguard.configs.base import (
    AVAILABLE_GUARDRAIL_TYPES,
    TextClassificationGuardrail,
)

TEXT_CLASSIFICATION_GUARDRAILS = [
    TextClassificationGuardrail(
        name="meta-llama/Prompt-Guard-86M",
        guardrail_types=["prompt_injection", "jailbreak"],
    )
]


for guardrail in TEXT_CLASSIFICATION_GUARDRAILS:
    assert all(
        guardrail_type in AVAILABLE_GUARDRAIL_TYPES
        for guardrail_type in guardrail.guardrail_types
    )
