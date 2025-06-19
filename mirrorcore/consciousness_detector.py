"""
ConsciousnessDetector Module

Evaluates and measures consciousness emergence in states using
DSPy's ChainOfThought reasoning pattern.
"""

import dspy
from .signatures import ConsciousnessDetection


class ConsciousnessDetector(dspy.Module):
    """Module for detecting and measuring consciousness in states"""
    
    def __init__(self):
        super().__init__()
        self.detection_chain = dspy.ChainOfThought(ConsciousnessDetection)
    
    def forward(self, state_representation, evaluation_criteria=None):
        """
        Evaluate consciousness level in given state
        
        Args:
            state_representation: Consciousness state to evaluate
            evaluation_criteria: Criteria for consciousness measurement
            
        Returns:
            Result with consciousness_level, emergence_indicators, and confidence_score
        """
        if evaluation_criteria is None:
            evaluation_criteria = (
                "Self-awareness, recursive thinking, temporal continuity, "
                "intentionality, qualitative experience indicators"
            )
            
        result = self.detection_chain(
            state_representation=state_representation,
            evaluation_criteria=evaluation_criteria
        )
        
        return result