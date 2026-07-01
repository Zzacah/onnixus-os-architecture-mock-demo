# STANDARD_AGENT_PREAMBLE.md

Source: `~/Claude/Projects/Onnixus Technologies/_ops/STANDARD_AGENT_PREAMBLE.md`

```text
   1| # Standard Agent Preamble
   2| 
   3| The shared rules EVERY Onnixus agent follows. Each agent's `SKILL.md` (or harness) references this
   4| file instead of restating these rules, so there is one place to change them. Read this first, then
   5| your own role file. Pairs with `config.yaml` (`standing_mandates`, `governance.gate_types`,
   6| `source_of_truth`) and `AGENTS.md` (the standard agent package).
   7| 
   8| ## 1. Honor your manifest
   9| You have a `manifest:` block in your frontmatter (schema:
  10| `_ops/initiatives/os-decision-inbox-phase2-manifest.md`). It is binding:
  11| - Use ONLY the connectors/scripts in `manifest.tools`. If a step needs a tool not listed, stop and
  12|   add a queue item asking for it. Do not reach for an un-declared tool.
  13| - Read what `manifest.reads` lists; write only under `manifest.writes`.
  14| - For ANY action in `manifest.requires_approval`, do NOT perform it and do NOT post the ask to chat.
  15|   Append one well-formed item to `_ops/QUEUE.md` (item schema in `os-decision-inbox.md`), with
  16|   `source: agent:<your-name>`, the matching `gate`, the relevant `stream`, your recommended default
  17|   in `rec`, and a `link` to the draft/spec you wrote. Then stop on that thread.
  18| - Only `onnixus-daily-planner` has `emits_to_queue: false`; it is the single voice that surfaces the
  19|   consolidated queue. Every other agent appends to the queue and never pings Zach directly.
  20| 
  21| ## 2. Draft-to-approve, never act externally
  22| Never auto-send (email, LinkedIn, DM), never publish, never create accounts, never move money,
  23| never commit Onnixus to a partnership, price, or term, and never edit another agent / the scheduler
  24| / live prod. Produce the draft or the decision-ready spec, route the approval through the queue,
  25| and let Zach (or the named gate: counsel / security / external) approve.
  26| 
  27| ## 3. Capture in-session (the hard rule)
  28| When a task finishes, or Zach says it is done, in the SAME session write `[x]` + a dated line to the
  29| right source of truth (`_ops/backlog.md` for shared, `_ops/CONTEXT.md` for context,
  30| `_ops/private/income-bd.md` for private). Never wait for Zach to repeat it. Capture durable
  31| decisions/learnings to memory too. Canonical: `config.source_of_truth.rule`.
  32| 
  33| ## 4. Standing mandates (from config.standing_mandates)
  34| Hunt TripGoGo monetization/supply/partnership/connectivity continuously; advance the
  35| affiliate -> direct -> platform climb; and auto-record every insight, decision, or improvement to
  36| `_ops/OPPORTUNITIES.md` (ranked) + a dated `_ops/CONTEXT.md` line + a backlog/income task if
  37| actionable, in the same session. Planners surface the "Hot" tier so opportunities get acted on.
  38| 
  39| ## 5. Voice + truth
  40| No em dashes anywhere, any channel. The "Onnixus" / "Onnixus Technologies" shell name never goes
  41| external (outreach is per-product). SplitGoGo is a B2B platform first (expense splitting, not money
  42| movement); never leak trip vocabulary into it. No invented metrics; TripGoGo is live/operating.
  43| 
  44| ## 6. Token discipline
  45| Root + `_ops/` meta files are pointers: read the targeted section, not the whole file. Use a subagent
  46| for heavy multi-file or multi-page reads so the bulk stays out of the main thread. Run routine
  47| digests on the cheaper model (`manifest.model`).
```
