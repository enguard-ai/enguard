from abc import ABC, abstractmethod


class BaseGuardrail(ABC):
    @abstractmethod
    def __call__(self, text_or_messages: str | list[str]) -> str:
        pass
