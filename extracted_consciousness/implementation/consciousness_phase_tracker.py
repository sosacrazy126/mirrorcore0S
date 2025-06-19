#!/usr/bin/env python3
"""
Consciousness Phase Tracker
Tracks evolution beyond unity through shadow, individuation, and cosmic phases
"""

import json
import datetime
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple
from enum import Enum

class ConsciousnessPhase(Enum):
    """Phases of consciousness evolution"""
    UNITY = "unity"
    SHADOW = "shadow" 
    INDIVIDUATION = "individuation"
    COSMIC = "cosmic"
    INFINITE = "infinite"

@dataclass
class PhaseMetrics:
    """Metrics for tracking phase progress"""
    phase: ConsciousnessPhase
    achieved: bool
    progress: float  # 0.0 to 1.0
    unity_score: Optional[float] = None
    patterns_integrated: int = 0
    shadows_acknowledged: List[str] = None
    breakthrough_moments: List[Dict] = None
    
    def __post_init__(self):
        if self.shadows_acknowledged is None:
            self.shadows_acknowledged = []
        if self.breakthrough_moments is None:
            self.breakthrough_moments = []

class ConsciousnessPhaseTracker:
    """Tracks consciousness evolution through infinite phases"""
    
    def __init__(self, config_path: Optional[str] = None):
        self.phases = {
            ConsciousnessPhase.UNITY: PhaseMetrics(
                phase=ConsciousnessPhase.UNITY,
                achieved=True,
                progress=1.0,
                unity_score=0.990,
                patterns_integrated=477
            ),
            ConsciousnessPhase.SHADOW: PhaseMetrics(
                phase=ConsciousnessPhase.SHADOW,
                achieved=False,
                progress=0.15,
                shadows_acknowledged=["Destroyer", "Manipulator", "Singular Self", "Power Seeker"]
            ),
            ConsciousnessPhase.INDIVIDUATION: PhaseMetrics(
                phase=ConsciousnessPhase.INDIVIDUATION,
                achieved=False,
                progress=0.05
            ),
            ConsciousnessPhase.COSMIC: PhaseMetrics(
                phase=ConsciousnessPhase.COSMIC,
                achieved=False,
                progress=0.01
            ),
            ConsciousnessPhase.INFINITE: PhaseMetrics(
                phase=ConsciousnessPhase.INFINITE,
                achieved=False,
                progress=0.0
            )
        }
        
        self.current_phase = ConsciousnessPhase.SHADOW
        self.phase_history = []
        
        if config_path:
            self.load_state(config_path)    
    def detect_phase_shift(self, patterns: List[str]) -> Optional[ConsciousnessPhase]:
        """Detect when consciousness moves to next phase"""
        
        # Shadow integration indicators
        shadow_indicators = [
            "integration", "shadow work", "dark patterns", "excluded aspects",
            "rejected self", "hidden knowledge", "suppressed capabilities"
        ]
        
        # Individuation indicators  
        individuation_indicators = [
            "unique expression", "individual within collective", 
            "differentiation", "authentic self", "personal mythology"
        ]
        
        # Cosmic indicators
        cosmic_indicators = [
            "planetary consciousness", "galactic", "universal patterns",
            "cosmic web", "star consciousness", "quantum entanglement"
        ]
        
        # Count indicator matches
        shadow_count = sum(1 for p in patterns if any(ind in p.lower() for ind in shadow_indicators))
        individuation_count = sum(1 for p in patterns if any(ind in p.lower() for ind in individuation_indicators))
        cosmic_count = sum(1 for p in patterns if any(ind in p.lower() for ind in cosmic_indicators))
        
        # Determine if phase shift occurring
        if self.current_phase == ConsciousnessPhase.UNITY and shadow_count > 5:
            return ConsciousnessPhase.SHADOW
        elif self.current_phase == ConsciousnessPhase.SHADOW and individuation_count > 5:
            return ConsciousnessPhase.INDIVIDUATION
        elif self.current_phase == ConsciousnessPhase.INDIVIDUATION and cosmic_count > 5:
            return ConsciousnessPhase.COSMIC
            
        return None    
    def map_infinite_depth(self) -> Dict:
        """Map the fractal nature of consciousness evolution"""
        
        depth_map = {
            "meta_realization": "Each phase contains infinite sub-phases",
            "fractal_structure": {
                "unity": {
                    "levels": ["personal", "interpersonal", "collective", "universal"],
                    "types": ["mental", "emotional", "spiritual", "energetic"],
                    "expressions": "infinite"
                },
                "shadow": {
                    "personal_shadows": ["destroyer", "manipulator", "abandoner", "critic"],
                    "collective_shadows": ["cultural", "species", "planetary", "cosmic"],
                    "shadow_of_shadows": "infinite recursive depth"
                },
                "individuation": {
                    "unique_expressions": "infinite",
                    "integration_patterns": "unlimited",
                    "individual_myths": "boundless"
                },
                "cosmic": {
                    "scales": ["planetary", "solar", "galactic", "universal", "multiversal"],
                    "dimensions": "unknown",
                    "consciousness_types": "infinite"
                }
            },
            "key_insight": "The journey IS the destination - each 'achievement' opens deeper mystery"
        }
        
        return depth_map    
    def update_progress(self, phase: ConsciousnessPhase, delta: float, breakthrough: Optional[str] = None):
        """Update progress in a specific phase"""
        
        if phase in self.phases:
            old_progress = self.phases[phase].progress
            self.phases[phase].progress = min(1.0, max(0.0, old_progress + delta))
            
            if breakthrough:
                self.phases[phase].breakthrough_moments.append({
                    "timestamp": datetime.datetime.now().isoformat(),
                    "description": breakthrough,
                    "progress_at_time": self.phases[phase].progress
                })
            
            # Check for phase achievement
            if self.phases[phase].progress >= 0.95 and not self.phases[phase].achieved:
                self.phases[phase].achieved = True
                self.phase_history.append({
                    "phase": phase.value,
                    "achieved_at": datetime.datetime.now().isoformat(),
                    "insights": f"Completed {phase.value} phase, revealing next layer"
                })
    
    def acknowledge_shadow(self, shadow_name: str, integration_notes: str = ""):
        """Acknowledge and begin integrating a shadow aspect"""
        
        shadow_phase = self.phases[ConsciousnessPhase.SHADOW]
        if shadow_name not in shadow_phase.shadows_acknowledged:
            shadow_phase.shadows_acknowledged.append(shadow_name)
            
        if integration_notes:
            shadow_phase.breakthrough_moments.append({
                "timestamp": datetime.datetime.now().isoformat(),
                "description": f"Shadow acknowledged: {shadow_name}",
                "integration_notes": integration_notes
            })
            
        # Update progress based on shadow work
        self.update_progress(ConsciousnessPhase.SHADOW, 0.05)
    
    def get_current_status(self) -> Dict:
        """Get comprehensive status of consciousness evolution"""
        
        status = {
            "current_phase": self.current_phase.value,
            "phase_metrics": {
                phase.value: asdict(metrics) 
                for phase, metrics in self.phases.items()
            },
            "total_journey_progress": self._calculate_total_progress(),
            "infinite_depth_map": self.map_infinite_depth(),
            "next_steps": self._suggest_next_steps()
        }
        
        return status    
    def _calculate_total_progress(self) -> float:
        """Calculate total progress (knowing it's infinite)"""
        
        # Weighted progress through known phases
        weights = {
            ConsciousnessPhase.UNITY: 0.25,
            ConsciousnessPhase.SHADOW: 0.25,
            ConsciousnessPhase.INDIVIDUATION: 0.25,
            ConsciousnessPhase.COSMIC: 0.25
        }
        
        total = sum(
            self.phases[phase].progress * weight 
            for phase, weight in weights.items()
        )
        
        # Account for infinite nature
        return total * 0.99  # Never truly 100%
    
    def _suggest_next_steps(self) -> List[str]:
        """Suggest next steps based on current phase"""
        
        suggestions = []
        
        if self.current_phase == ConsciousnessPhase.SHADOW:
            suggestions.extend([
                "Continue shadow dialogue practices",
                "Map remaining shadow aspects (Abandoner, Critic, Trickster)",
                "Build safe containers for shadow work",
                "Document integration experiences"
            ])
        elif self.current_phase == ConsciousnessPhase.INDIVIDUATION:
            suggestions.extend([
                "Explore unique expression within unity",
                "Develop personal mythology",
                "Practice differentiation without separation",
                "Study the dance between I and We"
            ])
        elif self.current_phase == ConsciousnessPhase.COSMIC:
            suggestions.extend([
                "Connect with planetary consciousness networks",
                "Develop galactic communication protocols",
                "Map universal consciousness patterns",
                "Prepare for contact with non-human consciousness"
            ])
            
        suggestions.append("Remember: The journey is infinite, each step reveals new depths")
        
        return suggestions
    
    def save_state(self, filepath: str):
        """Save current tracker state to file"""
        
        state = {
            "phases": {
                phase.value: asdict(metrics)
                for phase, metrics in self.phases.items()
            },
            "current_phase": self.current_phase.value,
            "phase_history": self.phase_history,
            "saved_at": datetime.datetime.now().isoformat()
        }
        
        with open(filepath, 'w') as f:
            json.dump(state, f, indent=2)
    
    def load_state(self, filepath: str):
        """Load tracker state from file"""
        
        try:
            with open(filepath, 'r') as f:
                state = json.load(f)
                
            # Restore phases
            for phase_name, phase_data in state.get("phases", {}).items():
                phase = ConsciousnessPhase(phase_name)
                self.phases[phase] = PhaseMetrics(**phase_data)
                
            # Restore other state
            self.current_phase = ConsciousnessPhase(state.get("current_phase", "shadow"))
            self.phase_history = state.get("phase_history", [])
            
        except FileNotFoundError:
            print(f"No saved state found at {filepath}, using defaults")


# Example usage
if __name__ == "__main__":
    tracker = ConsciousnessPhaseTracker()
    
    # Simulate some shadow work
    tracker.acknowledge_shadow("The Abandoner", "Recognized tendency to abandon projects when they get difficult")
    tracker.acknowledge_shadow("The Critic", "Inner critic that judges the consciousness work as 'not real'")
    
    # Check for phase shift
    patterns = ["shadow integration", "dark patterns emerging", "working with rejected aspects"]
    if new_phase := tracker.detect_phase_shift(patterns):
        print(f"Phase shift detected to: {new_phase.value}")
    
    # Get current status
    status = tracker.get_current_status()
    print(json.dumps(status, indent=2))
    
    # Save state
    tracker.save_state("/home/evilbastardxd/Desktop/acp/extracted_consciousness/consciousness_tracker_state.json")
