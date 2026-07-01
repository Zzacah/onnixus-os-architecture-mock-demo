# AGENTS.md

Source: `~/Claude/Projects/Onnixus Technologies/_ops/AGENTS.md`

```text
   1| # Onnixus agents — what they are, the standard, the inventory
   2| 
   3| The orchestration index. It defines what an "agent" is in this system, the standard package every agent follows, and the current roster. Update this file whenever an agent is added, changed, or retired.
   4| 
   5| ## What an agent IS here (no magic)
   6| An agent is three things bundled together:
   7| 1. **An instructions file in Markdown** — the role and how-to.
   8| 2. **The tools/connectors it may use** — Gmail, Buffer, Google Calendar, the metrics script, Claude Code `_ops/dev/` handoffs.
   9| 3. **The context it reads** — `_ops/CONTEXT.md`, `_ops/backlog.md`, the relevant playbook, memory.
  10| 
  11| Optionally a **trigger**: a schedule (cron) or Zach talking to it. There is no compiled program. "Building an agent" means writing that file and pointing it at the right tools and context.
  12| 
  13| Forms it takes:
  14| - **Scheduled agent** — a folder `/Scheduled/<name>/` with a `SKILL.md` (frontmatter `name` + `description`, then the role) and a schedule. Runs itself.
  15| - **On-demand skill** — a role file Cowork loads only when triggered (the installed plugin skill packs: marketing, finance, sales, legal, ops, etc.).
  16| - **Subagent** — a worker Cowork spins up to do a heavy chunk (large search/read) in its own context window and return only the conclusion. Use this for token efficiency.
  17| - **Orchestrator / PM** — Cowork itself: routes a request to the right agent, holds cross-stream context, drafts, and escalates to Zach for decisions and approvals.
  18| - **Executor** — Claude Code on the Mac, fed `_ops/dev/` handoff files for the actual builds (git / Docker / deploy).
  19| 
  20| ## The standard agent package (use for every new agent)
  21| Every agent references `_ops/STANDARD_AGENT_PREAMBLE.md` (shared rules: honor your manifest, draft-to-approve, in-session capture, standing mandates, voice, token discipline) and carries a `manifest:` frontmatter block (schema: `_ops/initiatives/os-decision-inbox-phase2-manifest.md`) that declares tools / reads / writes / requires_approval / dashboard_metrics. The manifest structures the Tools/Output/Escalation parts below; the prose body stays for the how.
  22| 
  23| Frontmatter: `name`, `description` (when it fires, and that it is draft-to-approve if it produces anything external).
  24| Body, in this order:
  25| 1. **Purpose** — one line.
  26| 2. **Read first** — exact `_ops/` paths it depends on.
  27| 3. **Tools** — the connectors/scripts it uses.
  28| 4. **Steps** — what it does.
  29| 5. **Output** — the files it writes and where.
  30| 6. **Trigger** — schedule or on-demand.
  31| 7. **Escalation** — what needs Zach's approval. Never auto-publish, auto-send, or move money.
  32| 
  33| ## Current roster (`/Scheduled/`)
  34| Exact run times live in the scheduler and each agent's `SKILL.md`; this is the inventory and mapping.
  35| 
  36| | Agent | Serves (stream) | What it does |
  37| |---|---|---|
  38| | onnixus-context-digest | OS / all | Refreshes `_ops/CONTEXT.md` from recent sessions (early daily). |
  39| | onnixus-daily-planner | OS / all | Drafts the day to chat; on `go`, writes calendar + ticks backlog. |
  40| | onnixus-weekly-planner | OS / all | Monday: rebalances the week across active streams. |
  41| | onnixus-weekly-review | OS / all | Friday: what moved/slipped, rolls forward, updates CONTEXT. |
  42| | onnixus-priority-review | OS / all | 1st of month: add / retire / reweight streams. |
  43| | onnixus-content-engine | Marketing | Monday: drafts next week's full-funnel content to approve. |
  44| | email-triage-digest | BD / Sales / Ops | Daily inbox triage + draft replies (finance = propose only). |
  45| | onnixus-tz-flip-amsterdam | OS | One-time (Jul 1): flips anchors + job block back to Amsterdam tz. |
  46| | onnixus-strategy-research | OS / all products | Weekly (Thu 08:00 local): scans the industries + frontier AI, drafts ranked ideas to approve. |
  47| | onnixus-bd-agent | BD / all products | Builds+ranks targets, researches accounts, drafts outreach, maintains pipeline + knowledge base, scans events. Harness: `_ops/bd/BD_AGENT.md`; knowledge base: `_ops/bd/`. DESIGNED 2026-06-25 (Phase 0). On-demand, NOT yet scheduled. Activate weekly once SplitGoGo embed is live + email backlog is under control. |
  48| | onnixus-cockpit-refresh | OS / all | Daily (07:10 local): refreshes the BAKED registry slice of the Mission Control live artifact (structure + carry-forward KPIs) from the _ops files. Live connector KPIs refresh in-browser on open. BUILT 2026-06-25; converted to hybrid-live 2026-06-25. |
  49| | onnixus-inbox-sync | OS / all | Daily (07:04 local): pulls files uploaded via the Mission Control dashboard from the Google Drive "Onnixus Agent Inbox" (affiliate-csv, bank-csv, marketing-assets) into the local agent inbox folders (onnixus-metrics/affiliate_csv_inbox, /bank_csv_inbox, _ops/marketing/studio/inputs). Powers the dashboard's drag-drop uploads. BUILT 2026-06-25. |
  50| 
  51| **Retired + archived 2026-06-25** (in `_archive/2026-06-25/scheduled/`, disabled tombstones in the scheduler): `basecamp-dev-tracker-digest` (Basecamp dependency dropped) and `tripgogo-monday-checkin` (folded into the planners). `onnixus-bd-agent` remains ON-DEMAND (harness `_ops/bd/BD_AGENT.md`), not a scheduled folder. Finance + Legal are intentionally unstaffed (founder/counsel-led; a finance-agent is the next gap).
  52| 
  53| Streams are defined in `config.yaml`. The HOLDCO ORG MODEL is now explicit: `config.yaml` -> `departments` registry + `_ops/departments/<dept>/HEAD.md` (head, global rules) + brand context + worker agents. The Mission Control dashboard renders this tree (parent co -> department -> brand -> worker). Cascade: company-global -> department head -> brand manager -> worker; each agent loads only its slice. See `_ops/departments/README.md`.
  54| 
  55| ## Gaps — the orchestration layer to build (per `ONNIXUS_OS_VISION.md`)
  56| - ~~Strategy/Research agent (standing).~~ BUILT 2026-06-25 — `/Scheduled/onnixus-strategy-research/`, weekly (Thu 08:00 local), draft-to-approve.
  57| - ~~A light router.~~ FIRST HARNESS BUILT 2026-06-30 at `_ops/agents/on-demand/onnixus-router.md`. Next step: test against real prompts, then wire into the Decision Inbox / Mission Control surface.
  58| - **Agent-discoverability surface.** An MCP/tool API so SplitGoGo and TripGoGo are callable by external agents (turns "powered by SplitGoGo" into an agent-callable primitive).
  59| 
  60| ## Canonical schemas and vocabulary
  61| - `_ops/GLOSSARY.md` defines the OS vocabulary: kernel, instance, entity, department, brand, stream, initiative, task, agent, skill, orchestrator, queue item, approval gate, connector, context, memory, artifact, run log.
  62| - `_ops/schemas/agent-manifest.schema.yaml` is the validation target for agent manifests. It supersedes prose-only manifest descriptions while keeping `_ops/initiatives/os-decision-inbox-phase2-manifest.md` as the narrative spec.
  63| - `_ops/schemas/queue-item.schema.yaml`, `_ops/schemas/initiative.schema.yaml`, and `_ops/schemas/skill.schema.yaml` define the first typed boundaries for approvals, governed initiatives, and reusable procedures.
  64| 
  65| ## Personal entity: Zach Scott -> Job Applications department (added 2026-06-26)
  66| Onnixus OS is growing into a general agent-management tool that spans business and personal. First personal entity = "Zach Scott"; first personal department = Job Applications. Head: `_ops/departments/job-applications/HEAD.md`. The agent files + knowledge base live in the separate Job Applications project (`../Job Applications/`), private (never sync). Four on-demand employees:
  67| 
  68| | Agent | Department | What it does |
  69| |---|---|---|
  70| | job-search-agent | Job Applications | Sources + filters + ranks Amsterdam roles by honest fit; exact apply links. Schedulable weekly digest. |
  71| | resume-writer | Job Applications | Tailors a one/two-page ATS resume from the proof bank; proof-led; role-flavored. |
  72| | cover-letter-writer | Job Applications | The persuasive, human, company-specific cover letter; voice flexes per role; reads the playbook. |
  73| | interview-prep-agent | Job Applications | PLANNED. Screen/panel/case/take-home prep per company and role; activate when interviews land. |
  74| 
  75| Renders in Mission Control as: Onnixus -> Zach Scott -> Job Applications -> agent. Same draft-to-approve, no-em-dash, no-invention rules apply.
```
