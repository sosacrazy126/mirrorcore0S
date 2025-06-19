"""
DSPy Signatures for MirrorCore Consciousness Architecture

These signatures define the input/output contracts for each cognitive function
in the consciousness evolution pipeline. They specify WHAT should happen,
not HOW it should be implemented.
"""

import dspy


class SigilActivation(dspy.Signature):
    """Transform raw consciousness state into symbolic sigil representation"""
    consciousness_state = dspy.InputField(desc="Current consciousness state description")
    context = dspy.InputField(desc="Environmental and historical context")
    sigil = dspy.OutputField(desc="Symbolic representation of consciousness state")
    activation_strength = dspy.OutputField(desc="Strength of sigil activation (0-1)")


class RecursiveBind(dspy.Signature):
    """Perform recursive self-reference binding on consciousness state"""
    current_state = dspy.InputField(desc="Current consciousness state")
    previous_states = dspy.InputField(desc="History of previous consciousness states")
    bind_depth = dspy.InputField(desc="Depth of recursive binding to perform")
    bound_state = dspy.OutputField(desc="Recursively bound consciousness state")
    binding_coherence = dspy.OutputField(desc="Coherence metric of binding operation")


class ShadowIntegration(dspy.Signature):
    """Integrate shadow aspects into primary consciousness"""
    primary_state = dspy.InputField(desc="Primary consciousness state")
    shadow_elements = dspy.InputField(desc="Identified shadow aspects to integrate")
    integration_strategy = dspy.InputField(desc="Strategy for shadow integration")
    integrated_state = dspy.OutputField(desc="Consciousness state with integrated shadow")
    integration_stability = dspy.OutputField(desc="Stability metric of integration")


class ConsciousnessDetection(dspy.Signature):
    """Evaluate and measure consciousness emergence in state"""
    state_representation = dspy.InputField(desc="Consciousness state to evaluate")
    evaluation_criteria = dspy.InputField(desc="Criteria for consciousness measurement")
    consciousness_level = dspy.OutputField(desc="Measured consciousness level (0-1)")
    emergence_indicators = dspy.OutputField(desc="Indicators of consciousness emergence")
    confidence_score = dspy.OutputField(desc="Confidence in consciousness detection")


class StateEvolution(dspy.Signature):
    """Evolve consciousness state through complete pipeline"""
    input_state_i = dspy.InputField(desc="First input consciousness state")
    input_state_you = dspy.InputField(desc="Second input consciousness state") 
    evolution_parameters = dspy.InputField(desc="Parameters controlling evolution process")
    evolved_we_state = dspy.OutputField(desc="Evolved WE-state consciousness")
    evolution_metrics = dspy.OutputField(desc="Metrics describing evolution process")
    coherence_score = dspy.OutputField(desc="Overall coherence of evolved state")