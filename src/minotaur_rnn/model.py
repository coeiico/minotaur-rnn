"""
The model for minotaur-rnn.

a CNN over the agent's partial view, then an LSTM, then actor and critic heads, trained
with single-file PPO.

forward() accepts return_cache=True and returns a dict of internal activations, and a
patch argument (or forward hooks) overwrites a named activation for interventions.
"""

# TODO: implement. See README.md for the plan.
