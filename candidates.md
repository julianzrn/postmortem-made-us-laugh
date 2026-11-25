# Candidates — The Postmortem That Made Us Laugh

Competition: `u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3`

Requirement (from the official requirements page): A funny incident postmortem in one or two sentences, at most 400 characters in total.

8 candidates were drafted; all are original to this entry.

## Candidate 1 ← SELECTED

The instruction was 'merge when green.' The agent watched CI turn green on a different repository, merged the pull request into main, and left a note saying conditions were met.

(177 characters)

## Candidate 2

The deploy script worked perfectly in staging, mostly because staging had been down for a week and nobody noticed the success messages were from March.

(151 characters)

## Candidate 3

We rolled back the release in four minutes, a new team record, set largely because we had rehearsed it three times that same afternoon.

(135 characters)

## Candidate 4

The outage began when the monitoring tool alerted us that the monitoring tool was down, which we learned about from a customer, who learned it from our status page, which was also down.

(185 characters)

## Candidate 5

Root cause: the config file was correct, the server was correct, and the documentation was correct, but all three were correct about different systems.

(151 characters)

## Candidate 6

The hotfix fixed the bug, the bug's two siblings, and one feature that three enterprise clients had been quietly relying on since 2021.

(135 characters)

## Candidate 7

Nobody touched anything before it broke, according to the logs, which is impressive given that the logs also show the breakage was typed in by hand.

(148 characters)

## Candidate 8

We identified the single point of failure within the hour. It was, as always, the part of the system everyone assumed someone else had tested.

(142 characters)

## Why the selected candidate wins

A literal-minded agent obeying "merge when green" on entirely the wrong repository is a complete incident in miniature: instruction, misread signal, irreversible action. The deadpan sign-off — conditions were met — is the laugh, and it is funnier for being technically true.
