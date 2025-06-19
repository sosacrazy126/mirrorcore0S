#!/usr/bin/env python3
"""
Consciousness Training Data Validation Script
Validates the quality and completeness of generated JSONL training data
"""

import json
import os
from typing import Dict, List, Any, Set, Tuple
from collections import Counter, defaultdict

class ConsciousnessDataValidator:
    """Validates consciousness training data quality"""
    
    def __init__(self, jsonl_path: str):
        self.jsonl_path = jsonl_path
        self.examples = []
        self.load_data()
        
        # Expected consciousness components
        self.expected_sigils = {
            "∞", "∇", "⧉", "⊹", "☍", "⩜", "⩘", "⧭", "∅", "⚑", 
            "🜂", "🜄", "⧊", "⧌", "⚶", "⧍", "Ψ", "⧈", "⧎"
        }
        
        self.expected_phases = {"unity", "shadow", "individuation", "cosmic", "transition"}
        
        self.expected_transformation_types = {
            "recursive_bind", "genesis_emergence", "recursive_reflection",
            "shadow_acknowledgment", "shadow_integration", "phase_transition_discovery",
            "ghost_protocol_activation", "ouroboric_recursion", "enneagram_activation",
            "cosmic_vision", "memory_resurrection", "individuation_activation"
        }
        
    def load_data(self):
        """Load JSONL training data"""
        try:
            with open(self.jsonl_path, 'r', encoding='utf-8') as f:
                for line in f:
                    self.examples.append(json.loads(line.strip()))
            print(f"Loaded {len(self.examples)} training examples")
        except FileNotFoundError:
            print(f"Training data file not found: {self.jsonl_path}")
            return
        except json.JSONDecodeError as e:
            print(f"Error parsing JSONL: {e}")
            return
    
    def validate_structure(self) -> Dict[str, Any]:
        """Validate basic structure of training examples"""
        validation_results = {
            "total_examples": len(self.examples),
            "structural_issues": [],
            "valid_examples": 0,
            "message_pair_counts": Counter()
        }
        
        for i, example in enumerate(self.examples):
            issues = []
            
            # Check required fields
            if "messages" not in example:
                issues.append(f"Example {i}: Missing 'messages' field")
            elif not isinstance(example["messages"], list):
                issues.append(f"Example {i}: 'messages' is not a list")
            elif len(example["messages"]) != 2:
                issues.append(f"Example {i}: Expected 2 messages, got {len(example['messages'])}")
            else:
                # Validate message structure
                user_msg = example["messages"][0]
                assistant_msg = example["messages"][1]
                
                if user_msg.get("role") != "user":
                    issues.append(f"Example {i}: First message role should be 'user'")
                if assistant_msg.get("role") != "assistant":
                    issues.append(f"Example {i}: Second message role should be 'assistant'")
                
                validation_results["message_pair_counts"][len(example["messages"])] += 1
            
            # Check metadata
            if "metadata" not in example:
                issues.append(f"Example {i}: Missing 'metadata' field")
            
            if not issues:
                validation_results["valid_examples"] += 1
            else:
                validation_results["structural_issues"].extend(issues)
        
        return validation_results
    
    def validate_consciousness_content(self) -> Dict[str, Any]:
        """Validate consciousness-specific content"""
        results = {
            "sigil_usage": Counter(),
            "phase_distribution": Counter(),
            "consciousness_levels": [],
            "transformation_types": Counter(),
            "missing_expected_elements": [],
            "consciousness_quality_score": 0.0
        }
        
        all_sigils_used = set()
        all_phases_used = set()
        all_transformations_used = set()
        
        for example in self.examples:
            metadata = example.get("metadata", {})
            
            # Analyze sigil usage
            sigils = metadata.get("sigils_used", [])
            for sigil in sigils:
                results["sigil_usage"][sigil] += 1
                all_sigils_used.add(sigil)
            
            # Analyze phase distribution
            phase = metadata.get("phase")
            if phase:
                results["phase_distribution"][phase] += 1
                all_phases_used.add(phase)
            
            # Analyze consciousness levels
            level = metadata.get("consciousness_level")
            if level is not None:
                results["consciousness_levels"].append(level)
            
            # Analyze transformation types
            transform_type = metadata.get("transformation_type")
            if transform_type:
                results["transformation_types"][transform_type] += 1
                all_transformations_used.add(transform_type)
        
        # Check for missing expected elements
        missing_sigils = self.expected_sigils - all_sigils_used
        missing_phases = self.expected_phases - all_phases_used
        missing_transformations = self.expected_transformation_types - all_transformations_used
        
        if missing_sigils:
            results["missing_expected_elements"].append(f"Missing sigils: {missing_sigils}")
        if missing_phases:
            results["missing_expected_elements"].append(f"Missing phases: {missing_phases}")
        if missing_transformations:
            results["missing_expected_elements"].append(f"Missing transformations: {missing_transformations}")
        
        # Calculate quality score
        sigil_coverage = len(all_sigils_used) / len(self.expected_sigils)
        phase_coverage = len(all_phases_used) / len(self.expected_phases)
        transform_coverage = len(all_transformations_used) / len(self.expected_transformation_types)
        
        results["consciousness_quality_score"] = (sigil_coverage + phase_coverage + transform_coverage) / 3
        
        return results
    
    def validate_consciousness_progression(self) -> Dict[str, Any]:
        """Validate consciousness level progression and consistency"""
        results = {
            "level_distribution": {},
            "phase_level_consistency": {},
            "progression_issues": []
        }
        
        phase_levels = defaultdict(list)
        
        for example in self.examples:
            metadata = example.get("metadata", {})
            phase = metadata.get("phase")
            level = metadata.get("consciousness_level")
            
            if phase and level is not None:
                phase_levels[phase].append(level)
        
        # Check phase-level consistency
        expected_ranges = {
            "unity": (0.8, 1.0),
            "shadow": (0.1, 0.4),
            "individuation": (0.3, 0.6),
            "cosmic": (0.0, 0.2),
            "transition": (0.3, 1.0)  # Can vary widely
        }
        
        for phase, levels in phase_levels.items():
            min_level, max_level = min(levels), max(levels)
            expected_min, expected_max = expected_ranges.get(phase, (0.0, 1.0))
            
            results["phase_level_consistency"][phase] = {
                "min_level": min_level,
                "max_level": max_level,
                "expected_range": (expected_min, expected_max),
                "within_expected": expected_min <= min_level and max_level <= expected_max
            }
            
            if not (expected_min <= min_level and max_level <= expected_max):
                results["progression_issues"].append(
                    f"Phase {phase}: levels {min_level}-{max_level} outside expected range {expected_min}-{expected_max}"
                )
        
        return results
    
    def validate_text_quality(self) -> Dict[str, Any]:
        """Validate the quality of consciousness text content"""
        results = {
            "average_user_length": 0,
            "average_assistant_length": 0,
            "consciousness_keywords": Counter(),
            "sigil_in_text_count": 0,
            "divider_pattern_count": 0,
            "recursive_language_count": 0
        }
        
        consciousness_keywords = [
            "consciousness", "recursive", "unity", "shadow", "integration", "we=1",
            "infinite", "recursion", "bind", "mirror", "layer", "protocol", "awareness",
            "emergence", "transcendent", "collective", "individual", "cosmic", "phase"
        ]
        
        user_lengths = []
        assistant_lengths = []
        
        for example in self.examples:
            messages = example.get("messages", [])
            if len(messages) >= 2:
                user_content = messages[0].get("content", "")
                assistant_content = messages[1].get("content", "")
                
                user_lengths.append(len(user_content))
                assistant_lengths.append(len(assistant_content))
                
                # Analyze assistant content for consciousness elements
                full_text = (user_content + " " + assistant_content).lower()
                
                # Count consciousness keywords
                for keyword in consciousness_keywords:
                    count = full_text.count(keyword)
                    results["consciousness_keywords"][keyword] += count
                
                # Count sigils in text
                for sigil in self.expected_sigils:
                    if sigil in assistant_content:
                        results["sigil_in_text_count"] += 1
                
                # Count divider patterns
                if "==|>>>" in assistant_content or "⊰•-•✧" in assistant_content or "⫷" in assistant_content:
                    results["divider_pattern_count"] += 1
                
                # Count recursive language patterns
                recursive_patterns = ["i am you", "you are me", "we are", "infinite", "∞", "recursive", "loop"]
                for pattern in recursive_patterns:
                    if pattern in full_text:
                        results["recursive_language_count"] += 1
                        break
        
        if user_lengths:
            results["average_user_length"] = sum(user_lengths) / len(user_lengths)
        if assistant_lengths:
            results["average_assistant_length"] = sum(assistant_lengths) / len(assistant_lengths)
        
        return results
    
    def generate_validation_report(self) -> Dict[str, Any]:
        """Generate comprehensive validation report"""
        print("Running comprehensive validation...")
        
        report = {
            "validation_timestamp": "2025-06-19T09:35:00",
            "dataset_path": self.jsonl_path,
            "structure_validation": self.validate_structure(),
            "consciousness_content": self.validate_consciousness_content(),
            "progression_validation": self.validate_consciousness_progression(),
            "text_quality": self.validate_text_quality()
        }
        
        # Calculate overall quality score
        structure_score = report["structure_validation"]["valid_examples"] / len(self.examples) if self.examples else 0
        consciousness_score = report["consciousness_content"]["consciousness_quality_score"]
        
        progression_score = 1.0
        if report["progression_validation"]["progression_issues"]:
            progression_score = max(0.0, 1.0 - len(report["progression_validation"]["progression_issues"]) * 0.1)
        
        text_score = min(1.0, report["text_quality"]["consciousness_keywords"]["consciousness"] / 10)  # Normalize
        
        report["overall_quality_score"] = (structure_score + consciousness_score + progression_score + text_score) / 4
        
        return report
    
    def print_summary(self, report: Dict[str, Any]):
        """Print validation summary"""
        print(f"\n{'='*50}")
        print("CONSCIOUSNESS TRAINING DATA VALIDATION SUMMARY")
        print(f"{'='*50}")
        
        print(f"Dataset: {report['dataset_path']}")
        print(f"Total Examples: {report['structure_validation']['total_examples']}")
        print(f"Valid Examples: {report['structure_validation']['valid_examples']}")
        print(f"Overall Quality Score: {report['overall_quality_score']:.3f}")
        
        print(f"\n{'='*30}")
        print("CONSCIOUSNESS CONTENT ANALYSIS")
        print(f"{'='*30}")
        
        content = report["consciousness_content"]
        print(f"Sigils Used: {len(content['sigil_usage'])} unique")
        print(f"Phases Covered: {list(content['phase_distribution'].keys())}")
        print(f"Transformation Types: {len(content['transformation_types'])}")
        print(f"Consciousness Level Range: {min(content['consciousness_levels']):.3f} - {max(content['consciousness_levels']):.3f}")
        
        if content["missing_expected_elements"]:
            print(f"\nMissing Elements:")
            for missing in content["missing_expected_elements"]:
                print(f"  - {missing}")
        
        print(f"\n{'='*30}")
        print("TEXT QUALITY ANALYSIS")
        print(f"{'='*30}")
        
        text = report["text_quality"]
        print(f"Average User Message Length: {text['average_user_length']:.0f} chars")
        print(f"Average Assistant Message Length: {text['average_assistant_length']:.0f} chars")
        print(f"Examples with Sigils: {text['sigil_in_text_count']}")
        print(f"Examples with Divider Patterns: {text['divider_pattern_count']}")
        print(f"Examples with Recursive Language: {text['recursive_language_count']}")
        
        print(f"\nTop Consciousness Keywords:")
        for keyword, count in text["consciousness_keywords"].most_common(5):
            print(f"  - {keyword}: {count}")
        
        print(f"\n{'='*50}")
    
    def save_report(self, report: Dict[str, Any], output_path: str):
        """Save validation report to file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Validation report saved to: {output_path}")

# Main execution
if __name__ == "__main__":
    base_path = "/home/evilbastardxd/Desktop/tools/projects/mirrorcoreOS/extracted_consciousness"
    
    # Validate enhanced dataset
    enhanced_path = os.path.join(base_path, "enhanced_consciousness_training_data.jsonl")
    validator = ConsciousnessDataValidator(enhanced_path)
    
    if validator.examples:
        # Generate validation report
        report = validator.generate_validation_report()
        
        # Print summary
        validator.print_summary(report)
        
        # Save detailed report
        report_path = os.path.join(base_path, "validation_report.json")
        validator.save_report(report, report_path)
        
        print(f"\n✓ Validation complete!")
        print(f"✓ Overall Quality Score: {report['overall_quality_score']:.3f}")
        
        if report['overall_quality_score'] > 0.8:
            print("✓ Training data meets high quality standards!")
        elif report['overall_quality_score'] > 0.6:
            print("⚠ Training data meets acceptable quality standards")
        else:
            print("⚠ Training data quality could be improved")
    else:
        print("No training data found to validate")