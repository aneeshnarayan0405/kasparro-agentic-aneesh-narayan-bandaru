"""
Templates package - output structure definitions
"""

from .base_template import BaseTemplate
from .faq_template import faq_template
from .product_template import product_template
from .comparison_template import comparison_template

__all__ = [
    'BaseTemplate',
    'faq_template',
    'product_template',
    'comparison_template'
]