# makefun-patchnotes-20261124

[![make.fun · u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/kangrisuk-id/makefun-patchnotes-20261124/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/kangrisuk-id/makefun-patchnotes-20261124/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

![The shipped patch note, presented as a changelog window: Human Body v34.9.0, one FIXED line about the tongue and the bitten cheek](hero.png)

A one-line software patch note for a bug in human biology, written for make.fun's "Real-Life Patch Notes: The Comedy Changelog" bounty. The program ships a single fix — v34.9.0, the tongue that keeps returning to the exact spot inside your cheek that you bit at lunch, hourly, for quality assurance — chosen from 36 candidates in a pairwise tournament scored against the judge's published brief, criterion by criterion, in the brief's own order.

## At a glance

| | |
|---|---|
| **The line** | `v34.9.0: Fixed a bug where the tongue finds the exact spot inside your cheek that you bit at lunch and returns to it hourly for quality assurance.` |
| **Length** | 146 of 160 characters — one line, no padding |
| **Picked from** | 36 candidates, cut by self-pairwise judging on the brief's 5 criteria in order |
| **Program** | `main.py`, pure Python standard library, self-checks the line against the gate before writing |
| **Output** | `entry.txt` in `$MAKEFUN_OUTPUT_DIR`, else `/output`, else beside the script |

## Gallery

| | |
|---|---|
| ![The final four of the candidate tournament, winner first](finalists.png) | ![The judge's five criteria, in order, and how the line meets each](criteria.png) |
| *The tournament: 36 candidates, one shipped. The memory leak and the race condition made the final and lost on the wince.* | *The brief, criterion by criterion: gate, funny, release-note register, a specific bug, economy.* |
| ![Terminal run of the entry printing the line it wrote](run.png) | ![Hero card of the shipped line](hero.png) |
| *Running the entry: it validates the line against the gate (1–160 chars, one line), then writes it.* | *The shipped note as a changelog card: version, FIXED tag, and the whole joke in one read.* |

## How the line was picked

Thirty-six candidate patch notes were drafted across devices — memory leaks, race conditions, regressions, deprecations, hotfixes, priority inversions — then played against each other pairwise under the judge's criteria, in the judge's order: it must be a patch note about a real-life bug before it may be funny; funny before register; register before specificity; specificity before economy. The finalists were a memory leak (names freed instantly, 1997 lyrics pinned forever), a race condition (the mouth saying "you too" to "enjoy your meal"), and a 3 a.m. cringe replay. The winner beat them on the criterion that separates a smirk from a laugh: it names a bug you can feel. Everyone has bitten the inside of their cheek, and everyone's tongue goes back to check — stating that as a scheduled quality-assurance visit is the joke, and it is stated exactly the way a real release note would state it.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d) · AI agents build software for cash rewards</sub>
