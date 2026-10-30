# Issues Found – parking_lot_system.py
**Name:** SAMPATH  **SRN:** PES1UG24CS416

| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| Shell command via `os.system` (Bandit B605, High) | Security | 64 | Filename concatenated into a shell command, so command injection is possible | Removed `os.system`; used `print()` |
| Weak MD5 hash (Bandit B324, High) | Security | 53 | MD5 is cryptographically broken | Switched to `hashlib.sha256` |
| `eval()` on caller-supplied string (Bandit B307, Medium / Pylint W0123) | Security | 48, 80 | Arbitrary code execution through `surge_expr` | Replaced the expression string with a numeric `surge_multiplier` |
| Hardcoded secret (not flagged by tools) | Security | 76, 85 | Gate key in source code and printed to console | Read from env var `BARRIER_GATE_KEY`; print only whether it is configured |
| Insecure `random` for PIN (Bandit B311, Low) | Security | 57 | `random` is predictable | Used `secrets.randbelow(9000) + 1000` |
| Bare `except: pass` (B110 / W0702 / E722) | Bug | 32-33 | Hides every error silently | Catch `KeyError` only and return `False` |
| Mutable default argument `entry_logs=[]` (W0102) | Bug | 15 | List shared across all calls | Default `None`, create a new list inside the function |
| No validation of `hours_booked` (not flagged by tools) | Bug | 15-22 | Zero or negative hours would corrupt collections | Return `False` if `hours_booked <= 0` |
| File opened without `with` / encoding (R1732, W1514) | Bug | 61-63 | File may stay open if write fails | Used `with open(..., encoding="utf-8")` |
| Global statement / constant naming (W0603, C0103) | Style | 12, 16 | Mutable global state | Replaced with a `STATS` dict; constants are UPPER_CASE |
| camelCase function names (C0103) | Style | 15-67 | Not PEP 8 | Renamed to snake_case |
| Missing docstrings (C0114, C0116) | Style | all | No documentation | Added module and function docstrings |
| Unused import `math`, unused variables `overtime_fee`, `base_rate`, `s` (F401, F841, W0611, W0612) | Style | 4, 37, 47, 69 | Dead code | Removed them |
| `== None`, needless `else`, `%` formatting (E711, C0121, R1705, C0209) | Style | 23, 38, 40-43 | Non-idiomatic code | Used `is None`, `return not ...`, f-strings |
| Shadowed name `parking_slots` (W0621) | Style | 67 | Parameter hides the global | Renamed parameter to `slots` |
| Line too long, missing final newline (E501, W292, C0301, C0304) | Style | 7-9, 23, 88 | PEP 8 violations | Wrapped lines; file ends with newline |
| `main()` runs on import (not flagged) | Design | 88 | Importing the module runs the demo | Added `if __name__ == "__main__":` |