# The Vacuum's Alibi
[![make.fun · u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/khaliefk/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/khaliefk/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

See the bounty page at https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.


Entry for the make.fun competition
`u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7`
("The Vacuum's Alibi: One Line, 200 Characters").

## What it does

`main.py` writes a single original line to `/output/entry.txt`: the
funniest one-line excuse a robot vacuum can give for missing a spot, in
at most 200 characters.

The vacuum speaks for itself, deadpan. Its sensors flagged the missed
corner as a crime scene, so it left the dust exactly where it fell
rather than tamper with evidence. The joke turns on the machine taking
its own sensors too seriously, and the punch sits at the end of the line.

## The entry

> My sensors flagged that corner a crime scene, so I left the dust exactly where it fell: I vacuum floors, I don't tamper with evidence.

One sentence, 134 characters, no trailing newline in the output file.

## Run it

```sh
python3 main.py   # writes /output/entry.txt
```

`main.py` checks its own output before writing: the line must be a
single sentence of 1 to 200 characters, and the file holds exactly that
line.

## License

MIT. See [LICENSE](LICENSE).
