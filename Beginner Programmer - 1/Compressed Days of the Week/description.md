# Challenge description

Given an input of a list of days of the week, output the shortest representation of the list.

Each day of the week will be defined as a two character string, Su (Sunday), Mo (Monday), etc.

The input may not necessarily be in sorted order but there will be a maximum of one occurrence per day.

You must sort the input (Sunday is to be considered the start of the week) and then reduce the abbreviations down to one letter as to not introduce ambiguity, e.g.

`[Su, Mo, Tu, We]` => `SMTW`
`[Fr, Th, Sa]` => `TFS`

If the output is `MTWTF` then return `D` (for weekDays).
If the output is `SS` then return `E` (for weekEnd).
If the output is `SMTWTFS` then return `A` (for All)
