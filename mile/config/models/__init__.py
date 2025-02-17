"""Configuration for deep learning models."""
from mile.config.models.cnns import LeNetConfig, LeNettiConfig
from mile.config.models.fcn import FCNConfig
from mile.config.models.gpt import (
    GPTConfig, AttentionClassifierConfig, 
    EmbeddingClassifierConfig, PretrainedAttentionClassifierConfig,
)

__all__ = [
    'GPTConfig',
    'FCNConfig',
    'LeNetConfig',
    'LeNettiConfig',
    'AttentionClassifierConfig',
    'EmbeddingClassifierConfig',
    'PretrainedAttentionClassifierConfig',
]
