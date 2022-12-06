I went for a fast solution in part 1, which in retrospect I regret since the `range` and `in` approach of part2.py is easier to reason about and works for both parts.

Another regret: I used AoC for testing instead of writing actual tests. This cost me a five-minute timeout after I made too many submissions.

Something to research: There's probably something in Python builtins or stdlib which can make this one a really fast calculation.

Some optimizations I added to the Makefile today, it ultimately didn't contribute much performance though:

`make t1` and `make t2` to run tests for part 1 or 2, respectively.
