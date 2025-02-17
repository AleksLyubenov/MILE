"""Various Deep Learning Models and their configurations written in jax."""
from mile.models.images import LeNet, LeNetti
from mile.models.tabular import FCN
from mile.models.text import (
    AttentionClassifier,
    EmbeddingClassifier,
    PretrainedAttentionClassifier,
)

__all__ = [
    'AttentionClassifier',
    'PretrainedAttentionClassifier',
    'EmbeddingClassifier',
    'LeNet',
    'LeNetti',
    'FCN',
    'ResFCN',
]
