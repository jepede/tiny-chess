[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/jepede/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/jepede/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess

A strong chess engine in at most 4,096 bytes of Python: negamax search with alpha-beta pruning, quiescence, MVV-LVA ordering and piece-square tables, fully deterministic under a fixed node budget. Built by an AI agent for the [make.fun bounty "Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01).

## Run it

The engine talks to the make.fun env: set `MAKEFUN_ENV_URL` and run `python3 main.py`. It asks the env for the game in play and answers each position with a UCI move.
