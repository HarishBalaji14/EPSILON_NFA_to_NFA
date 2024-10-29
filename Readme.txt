Overview

This Python script converts an epsilon Non-Deterministic Finite Automaton (NFA) to a standard NFA. Epsilon NFAs are a variant of NFAs that allow transitions on the empty string (ε), whereas standard NFAs do not. This conversion is useful for various applications, such as formal language theory, compiler design, and automata theory.

Functionality

The script takes as input an epsilon NFA represented as a dictionary, where each key is a state and each value is a dictionary of transitions. The transitions are represented as a dictionary where each key is a symbol (including ε) and each value is a list of next states.

The script outputs a standard NFA represented as a dictionary, where each key is a state and each value is a dictionary of transitions. The transitions are represented as a dictionary where each key is a symbol (excluding ε) and each value is a list of next states.

Conversion Algorithm

The script uses the following algorithm to convert the epsilon NFA to NFA:

Remove ε-transitions: Remove all ε-transitions from the epsilon NFA.
Add new transitions: For each state, add new transitions to all states that are reachable from that state via ε-transitions.
Remove unreachable states: Remove all states that are unreachable from the initial state.
		
Requirements

	Python 3.x

Usage

To use the script, simply run python epsilon_nfa_to_nfa.py and provide the epsilon NFA as input. The script will output the converted NFA.