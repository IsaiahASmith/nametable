from typing import Protocol
from dataclasses import dataclass

from nametable.Pattern import PatternProtocol


class PatternStackProtocol(Protocol):
    stack: tuple[PatternProtocol, ...]

    def __len__(self) -> int:
        ...

    def __getitem__(self, index: int) -> PatternProtocol:
        ...


@dataclass(frozen=True, eq=True)
class PatternStack:
    stack: tuple[PatternProtocol, ...]

    def __len__(self) -> int:
        return len(self.stack)

    def __getitem__(self, index: int) -> PatternProtocol:
        return self.stack[index]
