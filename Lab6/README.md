# Lab 6 – Code and Branch Coverage Analysis

**Course:** Software Engineering Laboratory  
**Student:** Sampath  
**Repository:** SE-Labs-PES1UG24CS416

## Objective
To analyse code coverage and branch coverage using Python testing tools and achieve a minimum of 90% coverage.

## Application
Self Storage Management System (`self_storage.py`).

## Technologies Used
- Python 3
- Pytest
- Coverage.py

## Project Structure

| File | Description |
|---|---|
| `self_storage.py` | Application under test |
| `test_self_storage.py` | Original starter tests |
| `CodeCoverageTest_51_self_storage.py` | Code coverage test cases |
| `BranchCoverageTest_51_self_storage.py` | Branch coverage test cases |
| `screenshots/` | Final terminal coverage reports |

## Final Coverage Results

- Code Coverage: **100%**
- Branch Coverage: **100%**
- Code coverage tests: 16 passed
- Branch coverage tests: 24 passed

## Execution Commands

Code coverage:

```bash
python -m coverage run --source=self_storage -m pytest CodeCoverageTest_51_self_storage.py -v
python -m coverage report -m
```

Branch coverage:

```bash
python -m coverage run --branch --source=self_storage -m pytest BranchCoverageTest_51_self_storage.py -v
python -m coverage report -m
```

## Screenshots
Refer to the `screenshots` folder for the final code coverage and branch coverage terminal reports.