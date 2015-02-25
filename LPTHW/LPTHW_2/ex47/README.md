1. Copy skeleton to ex47.
2. Rename everything with NAME to ex47.
3. Change the word NAME in all the files to ex47.
4. Finally, remove all the *.pyc files to make sure you're clean.


1. in LPTHW_2: cp -r projects/skeleton/* ex47/

2. change NAME dir: mv NAME ex47

3. change tests/NAME_tests.py: mv NAME_tests.py ex47_tests.py

4. go into dir ex47 & tests:
	ls *pyc
	rm *pyc