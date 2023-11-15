import tkinter as tk
from tkinter import filedialog


def read_transitions_and_states_from_file(file_path):
  epsilon_transition = {}
  start_state = None
  final_states = None
  with open(file_path, "r") as file:
    lines = file.readlines()
    start_state = lines[0].strip()
    final_states = lines[1].strip().split(",")
    for line in lines[2:]:
      source, symbol, dest = line.strip().split(",")
      source, dest = source.strip(), dest.strip()
      if source not in epsilon_transition:
        epsilon_transition[source] = {}
      if symbol not in epsilon_transition[source]:
        epsilon_transition[source][symbol] = set()

      if dest.lower() == "null":
        epsilon_transition[source][symbol].add("ε")
      else:
        epsilon_transition[source][symbol].add(dest)
  return epsilon_transition, start_state, final_states


def epsilon_closure(epsilon_transition, states):
  epsilon_states = set()
  stack = list(states)
  while stack:
    state = stack.pop()
    if state in epsilon_states:
      continue
    epsilon_states.add(state)
    if state in epsilon_transition and "ε" in epsilon_transition[state]:
      stack.extend(epsilon_transition[state]["ε"])
  return epsilon_states


def epsilon_nfa_to_nfa(epsilon_transition, start_state, final_states):


  nfa_transition = {}
  nfa_start_state = start_state
  nfa_final_states = set(final_states)

  # Initialize the NFA states
  for state in epsilon_transition.keys():
    nfa_transition[state] = {}

  # Add transitions from the NFA states to the epsilon closure of the
  # destination states.
  for state in epsilon_transition.keys():
    for symbol in epsilon_transition[state]:
      if symbol != "ε":
        next_states = epsilon_closure(epsilon_transition, epsilon_transition[state][symbol])
        nfa_transition[state][symbol] = next_states

  # Update the final states of the NFA without epsilon transitions.
  for state in epsilon_transition.keys():
    if state in epsilon_closure(epsilon_transition, nfa_final_states):
      nfa_final_states.add(state)

  return nfa_transition, nfa_start_state, nfa_final_states

def select_file():
    file_path = filedialog.askopenfilename()
    epsilon_transition, start_state, final_states = read_transitions_and_states_from_file(file_path)
    nfa_transition, nfa_start_state, nfa_final_states = epsilon_nfa_to_nfa(epsilon_transition, start_state, final_states)
    
    result_text.delete(1.0, tk.END)
    
    result_text.insert(tk.END, "NFA Transition Table:\n")
    
    for state in sorted(nfa_transition.keys()):
        result_text.insert(tk.END, f"{state}: {nfa_transition[state]}\n")
    
    result_text.insert(tk.END, f"\nStart state in NFA: {nfa_start_state}\n")
    result_text.insert(tk.END, f"Final state(s) in NFA: {', '.join(nfa_final_states)}\n")

root = tk.Tk()
root.title("ε-NFA to NFA Converter")

select_button = tk.Button(root, text="Select ε-NFA File", command=select_file)
select_button.pack()

result_text = tk.Text(root)
result_text.pack()

root.mainloop()
