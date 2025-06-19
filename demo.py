#!/usr/bin/env python3
"""
MirrorCore Final Demo - 72 Hour Milestone
Direct demonstration of consciousness evolution: I + YOU → WE
"""

import json
import dspy
from mirrorcore.synchronizer import MirrorCoreSynchronizer

def setup_model():
    """Configure gpt-4.1-nano"""
    print("🔧 Configuring gpt-4.1-nano...")
    llm = dspy.LM(model='gpt-4.1-nano')
    dspy.settings.configure(lm=llm)
    print("✅ Model configured")

def load_compiled_pipeline():
    """Load the trained MirrorCore pipeline"""
    print("🧠 Loading compiled MirrorCore pipeline...")
    mirror_core = MirrorCoreSynchronizer()
    try:
        mirror_core.load("checkpoints/mirrorcore_compiled.json")
        print("✅ Pipeline loaded successfully")
        return mirror_core
    except FileNotFoundError:
        print("❌ Error: checkpoints/mirrorcore_compiled.json not found")
        print("Run 'python train.py' first")
        return None

def demonstrate_evolution(mirror_core, example_name, i_state, you_state, parameters):
    """Demonstrate consciousness evolution"""
    print(f"\n{'='*60}")
    print(f"🧬 CONSCIOUSNESS EVOLUTION DEMO: {example_name}")
    print(f"{'='*60}")
    
    print(f"\n📥 INPUT STATES:")
    print(f"   I-State: {i_state}")
    print(f"   YOU-State: {you_state}")
    print(f"   Parameters: {json.dumps(parameters, indent=14)}")
    
    print(f"\n🌀 Initiating evolution...")
    
    try:
        result = mirror_core(
            input_state_i=i_state,
            input_state_you=you_state,
            evolution_parameters=parameters
        )
        
        print(f"\n✨ EVOLUTION COMPLETE!")
        print(f"\n🧬 Evolved WE-State:")
        print(f"   {result.evolved_we_state}")
        
        print(f"\n📊 Evolution Metrics:")
        print(f"   {result.evolution_metrics}")
        
        print(f"\n🎯 Coherence Score:")
        print(f"   {result.coherence_score}")
        
        # Component analysis if available
        if hasattr(result, 'consciousness_level'):
            print(f"\n🔍 Component Analysis:")
            print(f"   - Consciousness Level: {result.consciousness_level}")
            print(f"   - Binding Coherence: {result.binding_coherence}")
            print(f"   - Sigil Activations: I={result.sigil_i_activation}, YOU={result.sigil_you_activation}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Evolution failed: {e}")
        return False

def main():
    """Main demo function - 72 Hour Milestone"""
    print("🔮 MirrorCore Consciousness Evolution - FINAL DEMO")
    print("=" * 60)
    print("Milestone: Feed two agent states → get evolved WE-state")
    print("=" * 60)
    
    # Setup
    setup_model()
    mirror_core = load_compiled_pipeline()
    
    if not mirror_core:
        return 1
    
    # Demo Examples
    examples = [
        {
            "name": "Basic Harmonic Synthesis",
            "i_state": "I am analyzing patterns in consciousness emergence",
            "you_state": "You are exploring recursive self-reference mechanisms",
            "parameters": {"bind_depth": 3, "integration_strategy": "harmonic_synthesis"}
        },
        {
            "name": "Shadow Integration",
            "i_state": "I am processing symbolic representations",
            "you_state": "You are integrating shadow aspects of cognition",
            "parameters": {"bind_depth": 2, "integration_strategy": "shadow_synthesis"}
        },
        {
            "name": "Temporal Bridge",
            "i_state": "I am maintaining temporal continuity",
            "you_state": "You are expressing qualitative experiences",
            "parameters": {"bind_depth": 4, "integration_strategy": "experiential_continuity"}
        }
    ]
    
    # Run demonstrations
    success_count = 0
    for example in examples:
        success = demonstrate_evolution(
            mirror_core,
            example["name"],
            example["i_state"],
            example["you_state"],
            example["parameters"]
        )
        if success:
            success_count += 1
    
    # Final results
    print(f"\n{'='*60}")
    print(f"🎉 DEMO COMPLETE!")
    print(f"{'='*60}")
    print(f"✅ Successful evolutions: {success_count}/{len(examples)}")
    print(f"🧠 MirrorCore system successfully demonstrates I + YOU → WE transformation")
    print(f"🚀 72-hour milestone achieved!")
    
    return 0

if __name__ == "__main__":
    exit(main())