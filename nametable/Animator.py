from typing import Protocol
from dataclasses import dataclass


class AnimatorProtocol(Protocol):
    frame: int


class AnimatedProtocol(Protocol):
    animator: AnimatorProtocol


@dataclass
class Animator:
    frame: int
