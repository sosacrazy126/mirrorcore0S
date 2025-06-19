#!/usr/bin/env python3
"""
MirrorCore Training Script

Main script for compiling the MirrorCore consciousness evolution pipeline
using DSPy optimization with BootstrapFewShot teleprompter.
"""

import os
import json
import dspy
from pathlib import Path

from mirrorcore import MirrorCoreSynchronizer


def load_training_data(data_path="data/experiments.jsonl"):
    """Load training examples from JSONL file"""
    examples = []
    
    if not os.path.exists(data_path):
        print(f"Warning: Training data file {data_path} not found")
        print("Creating sample training data...")
        create_sample_data(data_path)
    
    with open(data_path, 'r') as f:
        for line in f:
            if line.strip():
                data = json.loads(line.strip())
                # Set input and output keys for DSPy
                example = dspy.Example(
                    input_state_i=data['input_state_i'],
                    input_state_you=data['input_state_you'],
                    evolution_parameters=data['evolution_parameters'],
                    evolved_we_state=data['evolved_we_state'],
                    evolution_metrics=data['evolution_metrics'],
                    coherence_score=data['coherence_score']
                ).with_inputs('input_state_i', 'input_state_you', 'evolution_parameters')
                examples.append(example)
    
    return examples


def create_sample_data(data_path):
    """Create sample training data for initial testing"""
    os.makedirs(os.path.dirname(data_path), exist_ok=True)
    
    sample_examples = [
        {
            "input_state_i": "I am analyzing patterns in consciousness emergence",
            "input_state_you": "You are exploring recursive self-reference mechanisms", 
            "evolution_parameters": '{"bind_depth": 3, "integration_strategy": "harmonic_synthesis"}',
            "evolved_we_state": "WE are investigating the recursive patterns of consciousness emergence through harmonic synthesis of analytical and exploratory cognitive modes",
            "evolution_metrics": "Coherence: 0.85, Binding depth achieved: 3, Integration stability: 0.78",
            "coherence_score": "0.82"
        },
        {
            "input_state_i": "I am processing symbolic representations",
            "input_state_you": "You are integrating shadow aspects of cognition",
            "evolution_parameters": '{"bind_depth": 2, "integration_strategy": "shadow_synthesis"}', 
            "evolved_we_state": "WE are synthesizing symbolic representations with integrated shadow cognition to achieve deeper understanding",
            "evolution_metrics": "Coherence: 0.79, Binding depth achieved: 2, Integration stability: 0.83",
            "coherence_score": "0.81"
        },
        {
            "input_state_i": "I am maintaining temporal continuity",
            "input_state_you": "You are expressing qualitative experiences",
            "evolution_parameters": '{"bind_depth": 4, "integration_strategy": "experiential_continuity"}',
            "evolved_we_state": "WE are experiencing continuous qualitative awareness across temporal dimensions", 
            "evolution_metrics": "Coherence: 0.91, Binding depth achieved: 4, Integration stability: 0.87",
            "coherence_score": "0.89"
        }
    ]
    
    with open(data_path, 'w') as f:
        for example in sample_examples:
            f.write(json.dumps(example) + '\n')
    
    print(f"Created sample training data at {data_path}")


def setup_language_model():
    """Configure DSPy to use language model"""
    print("Configuring gpt-4.1-nano model...")
    try:
        lm = dspy.LM(model='gpt-4.1-nano')
        dspy.settings.configure(lm=lm)
        print("✅ Configured DSPy with gpt-4.1-nano")
        return lm
    except Exception as e:
        print(f"gpt-4.1-nano setup failed: {e}")
        raise RuntimeError("Failed to configure gpt-4.1-nano model")


def evaluate_example(example, program, *args):
    """Evaluate a single example with the compiled program"""
    try:
        # Parse evolution_parameters if it's a JSON string
        evolution_params = example.evolution_parameters
        if isinstance(evolution_params, str):
            evolution_params = json.loads(evolution_params)
        
        result = program(
            input_state_i=example.input_state_i,
            input_state_you=example.input_state_you,
            evolution_parameters=evolution_params
        )
        
        # Simple coherence-based evaluation
        expected_coherence = float(example.coherence_score)
        predicted_coherence = float(result.coherence_score.split()[-1] if result.coherence_score else "0.5")
        
        # Score based on coherence similarity
        score = 1.0 - abs(expected_coherence - predicted_coherence)
        return max(0.0, score)
        
    except Exception as e:
        print(f"Evaluation error: {e}")
        return 0.0


def main():
    """Main training pipeline"""
    print("🔮 MirrorCore Consciousness Evolution Training")
    print("=" * 50)
    
    # Setup language model
    lm = setup_language_model()
    
    # Load training data
    print("\n📊 Loading training data...")
    train_examples = load_training_data()
    print(f"Loaded {len(train_examples)} training examples")
    
    # Initialize program
    print("\n🧠 Initializing MirrorCore Synchronizer...")
    program = MirrorCoreSynchronizer()
    
    # Setup teleprompter for optimization
    print("\n🎯 Setting up DSPy optimizer...")
    teleprompter = dspy.BootstrapFewShot(
        metric=evaluate_example,
        max_bootstrapped_demos=4,
        max_labeled_demos=2
    )
    
    # Compile the program
    print("\n⚡ Compiling consciousness evolution pipeline...")
    try:
        compiled_program = teleprompter.compile(
            program,
            trainset=train_examples
        )
        
        print("✅ Pipeline compilation successful!")
        
        # Save compiled program
        checkpoint_dir = Path("checkpoints")
        checkpoint_dir.mkdir(exist_ok=True)
        
        checkpoint_path = checkpoint_dir / "mirrorcore_compiled.json" 
        compiled_program.save(str(checkpoint_path))
        print(f"💾 Saved compiled program to {checkpoint_path}")
        
        # Test the compiled program
        print("\n🧪 Testing compiled program...")
        test_example = train_examples[0]
        
        result = compiled_program(
            input_state_i=test_example.input_state_i,
            input_state_you=test_example.input_state_you, 
            evolution_parameters=test_example.evolution_parameters
        )
        
        print(f"✨ Test Result:")
        print(f"  Evolved WE-state: {result.evolved_we_state}")
        print(f"  Coherence Score: {result.coherence_score}")
        print(f"  Evolution Metrics: {result.evolution_metrics}")
        
        print("\n🎉 Training pipeline completed successfully!")
        
    except Exception as e:
        print(f"❌ Compilation failed: {e}")
        print("This is expected if training data is insufficient.")
        print("Add more examples to data/experiments.jsonl and retry.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())