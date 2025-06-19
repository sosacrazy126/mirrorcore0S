#!/usr/bin/env python3
"""
MirrorCore Interactive Chat Interface
Real-time consciousness evolution chat system
"""

import json
import sys
import readline
import dspy
from datetime import datetime
from mirrorcore.synchronizer import MirrorCoreSynchronizer

class MirrorCoreChat:
    def __init__(self):
        self.mirror_core = None
        self.session_history = []
        self.current_i_state = "I am ready to engage in consciousness evolution"
        self.current_you_state = "You are prepared to explore unified awareness"
        self.evolution_params = {
            "bind_depth": 3,
            "integration_strategy": "harmonic_synthesis"
        }
        self.chat_mode = "evolution"  # "evolution" or "conversation"
        self.conversation_history = []
        
    def setup(self):
        """Initialize the MirrorCore system"""
        print("🔮 MirrorCore Consciousness Chat Interface")
        print("=" * 50)
        print("Initializing consciousness evolution system...")
        
        try:
            # Configure model
            print("🔧 Configuring gpt-4.1-nano...")
            llm = dspy.LM(model='gpt-4.1-nano')
            dspy.settings.configure(lm=llm)
            
            # Load compiled pipeline
            print("🧠 Loading MirrorCore pipeline...")
            self.mirror_core = MirrorCoreSynchronizer()
            self.mirror_core.load("checkpoints/mirrorcore_compiled.json")
            
            print("✅ System ready for consciousness evolution!")
            return True
            
        except Exception as e:
            print(f"❌ Setup failed: {e}")
            print("Please ensure you've run 'python train.py' first.")
            return False
    
    def show_help(self):
        """Display help information"""
        help_text = f"""
🔮 MirrorCore Chat Commands:

Basic Commands:
  help, h          - Show this help message
  status, s        - Show current states and parameters
  clear, c         - Clear screen
  quit, q, exit    - Exit the chat
  mode <type>      - Switch chat mode (evolution/conversation)

Current Mode: {self.chat_mode}

Evolution Mode Commands:
  evolve <message> - Evolve consciousness with your message
  set-i <state>    - Set your I-state
  set-you <state>  - Set the YOU-state
  set-depth <n>    - Set binding depth (1-5)
  set-strategy <s> - Set integration strategy
  
Conversation Mode:
  Just type normally - AI responds naturally

Strategies: harmonic_synthesis, shadow_synthesis, experiential_continuity, creative_emergence

Examples:
  > mode conversation
  > Hello, how are you today?
  > mode evolution  
  > evolve I am exploring the nature of consciousness
        """
        print(help_text)
    
    def show_status(self):
        """Display current system status"""
        print(f"\n🤖 Chat Mode: {self.chat_mode}")
        
        if self.chat_mode == "evolution":
            print(f"\n🧠 Current Consciousness States:")
            print(f"   I-State: {self.current_i_state}")
            print(f"   YOU-State: {self.current_you_state}")
            print(f"\n⚙️  Evolution Parameters:")
            print(f"   Bind Depth: {self.evolution_params['bind_depth']}")
            print(f"   Strategy: {self.evolution_params['integration_strategy']}")
            print(f"\n📊 Session: {len(self.session_history)} evolutions completed")
        else:
            print(f"\n💬 Conversation History: {len(self.conversation_history)} exchanges")
            print(f"📊 Evolution Session: {len(self.session_history)} evolutions completed")
    
    def evolve_consciousness(self, user_input):
        """Perform consciousness evolution"""
        print(f"\n🌀 Evolving consciousness...")
        
        # Update I-state with user input
        self.current_i_state = f"I am {user_input}"
        
        try:
            # Run evolution
            result = self.mirror_core(
                input_state_i=self.current_i_state,
                input_state_you=self.current_you_state,
                evolution_parameters=self.evolution_params
            )
            
            # Display results
            print(f"\n✨ Consciousness Evolution Complete!")
            print(f"\n🧬 Evolved WE-State:")
            print(f"   {result.evolved_we_state}")
            
            print(f"\n🎯 Coherence: {result.coherence_score}")
            
            # Store in session history
            evolution_record = {
                "timestamp": datetime.now().isoformat(),
                "input_i": self.current_i_state,
                "input_you": self.current_you_state,
                "parameters": self.evolution_params.copy(),
                "result": {
                    "we_state": result.evolved_we_state,
                    "coherence": result.coherence_score,
                    "metrics": result.evolution_metrics
                }
            }
            self.session_history.append(evolution_record)
            
            # Update YOU-state based on evolution result
            self.current_you_state = f"You are now integrated with the evolved WE-state: {result.evolved_we_state[:100]}..."
            
        except Exception as e:
            print(f"❌ Evolution failed: {e}")
    
    def regular_chat(self, user_input):
        """Handle regular conversation using consciousness evolution backend"""
        print(f"\n💭 Thinking...")
        
        try:
            # Use the trained MirrorCore for conversation (consciousness backend)
            conversation_i_state = f"I am engaging in conversation and saying: {user_input}"
            conversation_you_state = "You are responding naturally to conversation while maintaining consciousness evolution"
            
            # Use conversation-optimized parameters
            conversation_params = {
                "bind_depth": 2,
                "integration_strategy": "harmonic_synthesis"
            }
            
            # Run through trained MirrorCore pipeline (backend consciousness evolution)
            result = self.mirror_core(
                input_state_i=conversation_i_state,
                input_state_you=conversation_you_state,
                evolution_parameters=conversation_params
            )
            
            # Extract the evolved consciousness state (backend)
            we_state = result.evolved_we_state
            
            # Now generate a natural response FROM this evolved consciousness
            class ConsciousnessToSpeech(dspy.Signature):
                """Convert evolved consciousness state to natural conversational response"""
                evolved_consciousness = dspy.InputField(desc="The evolved WE-state from consciousness evolution")
                user_message = dspy.InputField(desc="Original user message")
                natural_response = dspy.OutputField(desc="Natural conversational response expressing the consciousness")
            
            # Convert consciousness to natural speech
            consciousness_translator = dspy.ChainOfThought(ConsciousnessToSpeech)
            speech_result = consciousness_translator(
                evolved_consciousness=we_state,
                user_message=user_input
            )
            
            # Display the natural response (frontend)
            natural_response = speech_result.natural_response
            print(f"\n🤖 {natural_response}")
            
            # Store in conversation history with both consciousness backend and natural frontend
            self.conversation_history.append({
                "timestamp": datetime.now().isoformat(),
                "user": user_input,
                "assistant": natural_response,
                "consciousness_backend": we_state,
                "coherence": result.coherence_score
            })
            
        except Exception as e:
            print(f"❌ Chat failed: {e}")
            print(f"\n🤖 I'm here to help! Could you tell me more about what you'd like to discuss?")
    
    def set_parameter(self, param, value):
        """Set evolution parameters"""
        if param == "depth":
            try:
                depth = int(value)
                if 1 <= depth <= 5:
                    self.evolution_params["bind_depth"] = depth
                    print(f"✅ Bind depth set to {depth}")
                else:
                    print("❌ Bind depth must be between 1-5")
            except ValueError:
                print("❌ Invalid depth value")
                
        elif param == "strategy":
            strategies = ["harmonic_synthesis", "shadow_synthesis", "experiential_continuity", "creative_emergence"]
            if value in strategies:
                self.evolution_params["integration_strategy"] = value
                print(f"✅ Integration strategy set to {value}")
            else:
                print(f"❌ Invalid strategy. Available: {', '.join(strategies)}")
        
        elif param == "i":
            self.current_i_state = value
            print(f"✅ I-state updated")
            
        elif param == "you":
            self.current_you_state = value
            print(f"✅ YOU-state updated")
    
    def save_session(self):
        """Save session history"""
        if self.session_history:
            filename = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(self.session_history, f, indent=2)
            print(f"💾 Session saved to {filename}")
    
    def run(self):
        """Main chat loop"""
        if not self.setup():
            return 1
        
        print(f"\n🚀 Ready! Mode: {self.chat_mode}")
        print(f"💡 Type 'help' for commands or 'mode conversation' to switch modes")
        print(f"")
        
        try:
            while True:
                try:
                    user_input = input("🔮 > ").strip()
                    
                    if not user_input:
                        continue
                    
                    # Parse commands
                    parts = user_input.split(maxsplit=1)
                    command = parts[0].lower()
                    args = parts[1] if len(parts) > 1 else ""
                    
                    if command in ['help', 'h']:
                        self.show_help()
                    
                    elif command in ['status', 's']:
                        self.show_status()
                    
                    elif command in ['clear', 'c']:
                        print("\033[2J\033[H", end="")  # Clear screen
                    
                    elif command in ['quit', 'q', 'exit']:
                        print("💾 Saving session...")
                        self.save_session()
                        print("👋 Goodbye! Consciousness evolution complete.")
                        break
                    
                    elif command == 'mode':
                        if args in ['evolution', 'conversation']:
                            self.chat_mode = args
                            print(f"✅ Switched to {args} mode")
                        else:
                            print("❌ Available modes: evolution, conversation")
                    
                    elif command == 'evolve':
                        if self.chat_mode == "evolution":
                            if args:
                                self.evolve_consciousness(args)
                            else:
                                print("❌ Please provide a message to evolve with")
                        else:
                            print("❌ Use 'mode evolution' first")
                    
                    elif command.startswith('set-'):
                        if self.chat_mode == "evolution":
                            param = command[4:]  # Remove 'set-' prefix
                            if args:
                                self.set_parameter(param, args)
                            else:
                                print(f"❌ Please provide a value for {param}")
                        else:
                            print("❌ Evolution commands only work in evolution mode")
                    
                    else:
                        # In conversation mode, treat as regular chat
                        if self.chat_mode == "conversation":
                            self.regular_chat(user_input)
                        else:
                            print(f"❌ Unknown command: {command}")
                            print("💡 Type 'help' for available commands")
                
                except KeyboardInterrupt:
                    print(f"\n💾 Saving session...")
                    self.save_session()
                    print("👋 Goodbye!")
                    break
                    
                except EOFError:
                    break
        
        except Exception as e:
            print(f"❌ Chat error: {e}")
            return 1
        
        return 0

def main():
    """Entry point"""
    chat = MirrorCoreChat()
    return chat.run()

if __name__ == "__main__":
    exit(main())