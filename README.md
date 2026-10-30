# minotaur-rnn

**RL maze explorer.** A CNN + LSTM agent trained with PPO to explore mazes, with its memory probed the same way as tiny-trace-tfm's.

**Status:** not started.

## Question

Does an agent with memory, trained only on reward, learn to explore mazes, and does its memory track what tiny-trace-tfm's does?

## Plan

- **Architecture:** a CNN over the agent's partial view, then an LSTM, then actor and critic heads, trained with single-file PPO.
- **Environment:** MiniGrid, plus a custom environment built on tiny-trace-tfm's maze generator so the two projects use identical mazes.

## Experiments

- Success rate and step count against the tiny-trace-tfm baselines.
- Probes on the LSTM state for position, visited cells and direction to the goal.
- Interventions on that memory.

## Done when

- It solves held-out mazes, and a table compares its probe results with tiny-trace-tfm's.

Plus the general checklist:

Apply this checklist with the project-specific requirements and exceptions in
[CLAUDE.md](CLAUDE.md#project-specific-scope).

- `just quick` runs end to end on CPU in under 5 minutes, as a smoke test.
- The full run fits on one consumer GPU (8–12 GB VRAM) and auto-detects cuda, mps or cpu.
- Each run saves weights, `metrics.json` and its plots to `runs/<run-name>/`.
- This README shows the headline result with plots, compares against baselines, and states negative results plainly.
- Tests cover data generators, tensor shapes and one tiny overfit check.

## Notes

- Part of the ariadne / minotaur / theseus series with tiny-trace-tfm.

## Quickstart

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Everything else, Python 3.12 included, comes from uv.

```sh
just setup              # uv sync, then install the pre-commit hooks
just quick              # CPU smoke test, under 5 minutes
just train              # full run; flags pass through, e.g. --run-name wd1.0-seed0
just analyze <run>      # baselines, probes, interventions and plots
just test               # pytest
just check              # ruff and basedpyright, as in CI
```

Copy `.env.example` to `.env` (gitignored) for `HF_TOKEN` and `HF_USER`.

## Layout

```
minotaur-rnn/
├── README.md                goal, plan, results with plots
├── CLAUDE.md                instructions for coding agents; AGENTS.md points here
├── .agents/                 instructions/ (Python formatting, commits) and plans/
├── pyproject.toml           metadata, dependencies, tool settings
├── uv.lock                  committed lockfile
├── .python-version          pinned by uv
├── justfile                 every routine command
├── .pre-commit-config.yaml
├── .github/workflows/ci.yml
├── src/minotaur_rnn/
│   └── model.py, data.py, analysis.py, utils.py
├── train.py                 CLI; --quick runs the CPU smoke test
├── predict.py               load weights and run inference
├── analyze.py               baselines, probes, interventions, plots
├── notebooks/               marimo notebooks for exploration
├── tests/
└── runs/                    outputs, gitignored
```

## Results

_No results yet._ The headline result with plots, the comparison against baselines, and any negative results go here.

## Sources

- Schulman et al. 2017, PPO
- CleanRL
- Minigrid

## License

MIT
