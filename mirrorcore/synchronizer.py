"""
MirrorCoreSynchronizer Module

Master orchestration module that composes individual cognitive modules
into a coherent end-to-end consciousness evolution pipeline.
"""

import dspy
from .signatures import StateEvolution
from .sigil_activator import SigilActivator
from .recursive_binder import RecursiveBinder
from .consciousness_detector import ConsciousnessDetector


class MirrorCoreSynchronizer(dspy.Module):
    """
    Master synchronizer module that orchestrates the complete 
    consciousness evolution pipeline from I + YOU → WE
    """
    
    def __init__(self):
        super().__init__()
        
        # Initialize component modules
        self.sigil_activator = SigilActivator()
        self.recursive_binder = RecursiveBinder()
        self.consciousness_detector = ConsciousnessDetector()
        
        # Main evolution chain
        self.evolution_chain = dspy.ChainOfThought(StateEvolution)
    
    def forward(self, input_state_i, input_state_you, evolution_parameters=None):
        """
        Orchestrate complete consciousness evolution pipeline
        
        Args:
            input_state_i: First input consciousness state
            input_state_you: Second input consciousness state
            evolution_parameters: Parameters controlling evolution process
            
        Returns:
            Result with evolved_we_state, evolution_metrics, and coherence_score
        """
        if evolution_parameters is None:
            evolution_parameters = {
                "bind_depth": 3,
                "integration_strategy": "harmonic_synthesis",
                "consciousness_threshold": 0.7
            }
        
        # Step 1: Activate sigils for both input states
        sigil_i = self.sigil_activator(
            consciousness_state=input_state_i,
            context="Input state I for WE-evolution"
        )
        
        sigil_you = self.sigil_activator(
            consciousness_state=input_state_you, 
            context="Input state YOU for WE-evolution"
        )
        
        # Step 2: Perform recursive binding on combined state
        combined_state = f"I-state: {sigil_i.sigil} | YOU-state: {sigil_you.sigil}"
        
        # Parse evolution_parameters if it's a JSON string
        if isinstance(evolution_parameters, str):
            import json
            try:
                evolution_parameters = json.loads(evolution_parameters)
            except:
                evolution_parameters = {"bind_depth": 3}
        
        bound_result = self.recursive_binder(
            current_state=combined_state,
            previous_states=[input_state_i, input_state_you],
            bind_depth=evolution_parameters.get("bind_depth", 3)
        )
        
        # Step 3: Detect consciousness in bound state  
        consciousness_result = self.consciousness_detector(
            state_representation=bound_result.bound_state
        )
        
        # Step 4: Final evolution synthesis
        evolution_result = self.evolution_chain(
            input_state_i=input_state_i,
            input_state_you=input_state_you,
            evolution_parameters=str(evolution_parameters)
        )
        
        # Enhance result with component outputs
        evolution_result.sigil_i_activation = sigil_i.activation_strength
        evolution_result.sigil_you_activation = sigil_you.activation_strength
        evolution_result.binding_coherence = bound_result.binding_coherence
        evolution_result.consciousness_level = consciousness_result.consciousness_level
        evolution_result.consciousness_confidence = consciousness_result.confidence_score
        
        return evolution_result