"""
SigilActivator Module

Transforms raw consciousness states into symbolic sigil representations
using DSPy's ChainOfThought reasoning pattern.
"""

import dspy
from .signatures import SigilActivation


class SigilActivator(dspy.Module):
    """Module for activating consciousness sigils from raw states"""
    
    def __init__(self):
        super().__init__()
        self.activation_chain = dspy.ChainOfThought(SigilActivation)
    
    def forward(self, consciousness_state, context=""):
        """
        Transform consciousness state into sigil representation
        
        Args:
            consciousness_state: Raw consciousness state description
            context: Environmental and historical context
            
        Returns:
            Result with sigil and activation_strength fields
        """
        result = self.activation_chain(
            consciousness_state=consciousness_state,
            context=context
        )
        
        return result