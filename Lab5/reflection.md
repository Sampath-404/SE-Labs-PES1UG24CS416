# Reflection – SAMPATH (PES1UG24CS416)

**1. Which tool found the most issues, and which was most useful?**
Pylint reported the most (about 36 messages, score 4.10/10). Bandit was the most important, because it found the two High severity security flaws (`os.system` and MD5) and the `eval` call. Flake8 mostly confirmed style problems Pylint had already caught.

**2. Did you find any false positives or issues the tools missed?**
Bandit flagged `random` for a parking PIN. The risk is low, but `secrets` was an easy fix. The tools missed the hardcoded gate key (it is printed to the console) and the missing validation of `hours_booked`. I found these only by reading the code.

**3. How would you integrate static analysis into a workflow?**
Run the tools as a pre-commit hook and as a CI step on every pull request. Fail the build on Bandit High/Medium findings and on a Pylint score below 9.5, and keep Flake8 in the editor for instant feedback.

**4. How did your code improve?**
Pylint went from 4.10 to 10.00. Bandit went from 5 issues (2 High, 1 Medium, 2 Low) to 0, and Flake8 from 10 warnings to 0. The code is now safer (no `eval`, no shell, SHA-256, `secrets`, no hardcoded key), more readable (snake_case, docstrings), and has fewer hidden bugs (no mutable default, no swallowed exceptions).