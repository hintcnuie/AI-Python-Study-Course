# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python beginner's homework collection — 5 standalone exercises, each in its own `.py` file. Each exercise has a corresponding test file in `tests/`.

## Commands

```bash
# Run any single exercise
python 1_count_specific_char.py
python 2_list_operations.py
python 3_string_function.py
python 4_dataframe_operations.py
python 5_bank_customer_data.py

# Run all tests
python -m pytest tests/ -v

# Run tests for a single exercise
python -m pytest tests/test_1_count_char.py -v
```

## Environment

- Python 3.12 via Conda environment named `ai-python-study`
- Dependencies: `numpy>=1.26.0`, `pandas>=2.0.0`, `pytest>=7.0.0`
- Config: `pyproject.toml` (project metadata + pytest options)
- IDE: PyCharm (Community Edition), with the conda env selected as the project interpreter.

To set up from scratch:

```bash
conda create -n ai-python-study python=3.12 -y
conda activate ai-python-study
pip install -r requirements.txt
```

Then point PyCharm at `envs/ai-python-study/bin/python`.

## Project structure

```
├── pyproject.toml           # Project config + pytest settings
├── requirements.txt         # numpy, pandas, pytest
├── N_description.py         # Exercise scripts (1-5)
└── tests/
    ├── conftest.py          # Shared fixtures (_import_module helper, seeded_df, sample_df)
    ├── fixtures/
    │   └── bank_customers.csv  # Test data for exercise 5
    └── test_N_description.py   # Test files (1-5)
```

## Code style

Each exercise script follows this pattern:
- Module-level docstring describing the exercise
- Pure function(s) with the core logic, each with type hints (`str`, `int`, `list`, `None`) and a docstring (Args/Returns/Raises)
- A `main() -> None` entry point
- `if __name__ == "__main__":` guard

Keep the logic simple — `if/else`, basic loops, `print()`. Avoid comprehensions, `lambda`, `map`/`filter`.

## Testing

- Test framework: pytest
- Exercise modules with numeric filenames are imported via `_import_module()` in `tests/conftest.py`
- Exercise 4 tests use `seeded_df` fixture for deterministic results
- Exercise 5 tests use `sample_df` fixture with a 15-row test CSV

## Problem 5 data dependency

`5_bank_customer_data.py` reads `BankCustomer Data.csv` from the current working directory. This file is not in the repo. A smaller test fixture exists at `tests/fixtures/bank_customers.csv` for unit tests.
