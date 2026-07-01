# config.yaml

Source: `~/Claude/Projects/Onnixus Technologies/_ops/config.yaml`

```text
   1| # Onnixus Operating System — STREAM REGISTRY + settings
   2| # =====================================================================
   3| # This file is the single source of truth for what the system tracks.
   4| # It is meant to CHANGE. Add a project, retire one, or reweight here and
   5| # every part of the engine (planner, weekly review, cockpit) adapts —
   6| # nothing assumes a fixed number of streams.
   7| #
   8| # To ADD a stream:   copy a block under `streams:`, set status: active,
   9| #                    pick a color + target, and (if shared) a basecamp_todolist.
  10| # To RETIRE a stream: set status: archived (kept for history, ignored by planner).
  11| # The monthly `onnixus-priority-review` proposes these changes for your approval.
  12| # =====================================================================
  13| 
  14| # SOURCE OF TRUTH = the markdown backlog files, written DIRECTLY by Cowork in-session.
  15| # No manual sync step. (2026-06-23: Basecamp retired as a dependency — Luis doesn't
  16| # live in it, so the Mac-side basecamp-sync.sh push is no longer in the loop.)
  17| source_of_truth:
  18|   shared:  "_ops/backlog.md"
  19|   private: "_ops/private/income-bd.md"
  20|   context: "_ops/CONTEXT.md"
  21|   opportunities: "_ops/OPPORTUNITIES.md"   # ranked monetization/supply/partnership/connectivity + captured insights; planners + strategy-research + bd-agent read and feed this
  22|   rule: "When a task finishes — or Zach reports it done — write [x] + a dated CONTEXT line in the SAME session. Never wait for Zach to repeat it."
  23| 
  24| # Standing mandates the whole engine honors continuously (not one-off tasks).
  25| standing_mandates:
  26|   - id: tripgogo_monetization
  27|     rule: "Always be hunting ways to monetize TripGoGo and improve its supply, partnerships, and connectivity. Treat this as an ongoing background objective for every product/BD/strategy cycle."
  28|   - id: auto_capture_opportunities
  29|     rule: "Auto-record every insight, decision, or potential improvement to the OS in the SAME session it surfaces: append to _ops/OPPORTUNITIES.md (rank it), drop a dated _ops/CONTEXT.md line, and add a backlog/income-bd task if actionable. Never wait to be asked."
  30|   - id: surface_hot_opportunities
  31|     rule: "Planners (daily/weekly) and the priority-review read OPPORTUNITIES.md and surface anything in the 'Hot' tier when proposing what Zach should do, so exciting opportunities get jumped on, not buried."
  32|   - id: direct_supply_climb
  33|     rule: "Continuously advance the affiliate→direct→platform climb: hunt direct-supply, partnership, and margin opportunities, and treat SplitGoGo money movement as a strategic dependency for TripGoGo. Initiative roadmap + OKRs live in _ops/initiatives/direct-supply.md."
  34| 
  35| # Every working day, all three PRODUCT lines must advance (Zach directive 2026-06-25).
  36| daily_product_coverage:
  37|   products: [tripgogo, splitgogo, tg4b]
  38|   rule: "Each of the three product lines gets a daily NEXT-ACTION every working day: either a Zach work block OR an agent-carried task (research / draft / triage via the bd / content / strategy / email agents). A product advancing via an agent COUNTS, since Zach can only deep-work one or two things a day. The planner shows each product's daily move and who carries it. This is a FLOOR in addition to (not replacing) per-stream weekly targets."
  39|   gates: "Respect each product's current gate when choosing the move: SplitGoGo = go-live ops + pilot prep until the embed is live; TG4B = resolve the open decisions + ICP/use-case prep until launch; TripGoGo = supply/monetization + product. On travel days (config.travel), coverage may be agent-only."
  40| 
  41| # ── GOVERNANCE (execution layer for multi-step initiatives) ───────────
  42| # Standard + how-to: _ops/initiatives/README.md. Each major cross-department effort
  43| # gets one authoritative roadmap file with an OKR cascade + a task-DAG + gates.
  44| governance:
  45|   initiatives_dir: "_ops/initiatives/"
  46|   rule: >
  47|     Treat each _ops/initiatives/<name>.md as the authoritative roadmap for that initiative.
  48|     Each planning cycle, compute the ready frontier (tasks whose depends_on are all done, status != done)
  49|     and surface ready tasks as candidate next-actions, respecting daily_product_coverage + priority_model.
  50|     Never surface a blocked task. On completion, verify the task's exit criterion; auto-advance deterministic
  51|     (gate: auto) tasks, and route zach/counsel/security/external gates for sign-off and log them in the file's
  52|     gate log. Mirror the active ready frontier into backlog.md. Weekly-review audits KR movement;
  53|     priority-review re-scores OKRs.
  54|   gate_types: [auto, zach, counsel, security, external]
  55|   autonomous_execution:
  56|     enabled: true
  57|     executor: onnixus-initiative-executor
  58|     rule: >
  59|       Don't wait for the daily/weekly schedule. Whenever a task becomes unblocked (enters the ready
  60|       frontier) and is agent-executable (gate: auto and a research/analysis/drafting/file-authoring/
  61|       status task within Cowork's safe capabilities), work it immediately and continuously, auto-updating
  62|       its status + the gate log in the initiative file and mirroring to CONTEXT/backlog, then recompute the
  63|       frontier and continue. STOP only at: a human gate (zach/counsel/security/external), a prohibited or
  64|       approval-required action (external sends, money, account creation, publishing, live config/agent edits),
  65|       a task needing code execution on the Mac (write a Claude Code handoff and mark it handed-off), or the
  66|       token limit. Keep a "Manual / needs-Zach" list in the initiative file current and surface it.
  67|   active_initiatives:
  68|     - {file: "_ops/initiatives/direct-supply.md", stream: direct_supply, status: active}
  69|     - {file: "_ops/initiatives/tripgogo-conversion.md", stream: tripgogo, status: active}   # TOP near-term priority: fix the funnel → revenue/funding
  70|     - {file: "_ops/initiatives/finance-stack.md", stream: finance_stack, status: active}   # standardize product + holdco financial statements/accounting/bookkeeping; Phase 1 done
  71| 
  72| # ── DEPARTMENTS REGISTRY ──────────────────────────────────────────────
  73| # The holdco org model: company-global -> department head (global rules) ->
  74| # brand manager (per-brand context) -> worker (task agent). Agents load only
  75| # their slice. The Mission Control dashboard + planners read this.
  76| # scope: company (sets global, serves all brands) | matrixed (head + a manager per brand)
  77| # brands use the stream keys: tripgogo, splitgogo, tg4b
  78| departments:
  79|   - {key: executive, name: "Executive office", scope: company, head: "_ops/departments/executive/HEAD.md",
  80|      workers: [onnixus-daily-planner, onnixus-weekly-planner, onnixus-weekly-review, onnixus-priority-review, onnixus-context-digest, onnixus-cockpit-refresh, onnixus-inbox-sync, onnixus-tz-flip-amsterdam, onnixus-initiative-executor], status: active}
  81|   - {key: strategy, name: "Strategy & research", scope: company, head: "_ops/departments/strategy/HEAD.md",
  82|      workers: [onnixus-strategy-research], status: active}
  83|   - {key: bizdev, name: "Biz dev & sales", scope: matrixed, head: "_ops/departments/bizdev/HEAD.md",
  84|      # onnixus-bd-agent = ON-DEMAND (harness _ops/bd/BD_AGENT.md), NOT a scheduled folder yet; email-triage-digest is scheduled + shared with marketing
  85|      brands: {tripgogo: active, splitgogo: gated, tg4b: pre-launch}, workers: [onnixus-bd-agent (on-demand), email-triage-digest], status: building}
  86|   - {key: marketing, name: "Marketing", scope: matrixed, head: "_ops/departments/marketing/HEAD.md",
  87|      # onnixus-growth-analyst added 2026-06-26: full-funnel conversion/analytics expert (harness _ops/departments/marketing/GROWTH_ANALYST.md); on-demand + weekly; product-funnel pull is Mac-side
  88|      # onnixus-reddit-scout added 2026-06-27: value-first Reddit listen-and-draft agent (harness _ops/departments/marketing/REDDIT_LISTEN_AGENT.md); drafts helpful replies, NEVER auto-posts; Zach posts from his existing personal account
  89|      brands: {tripgogo: active, splitgogo: hold, tg4b: active}, workers: [onnixus-content-engine, email-triage-digest, "onnixus-growth-analyst (on-demand)", "onnixus-reddit-scout (on-demand)"], status: needs_attention}
  90|   - {key: engineering, name: "Engineering", scope: matrixed, head: "_ops/departments/engineering/HEAD.md",
  91|      # basecamp-dev-tracker-digest RETIRED + ARCHIVED 2026-06-25 (Basecamp dependency dropped) -> no scheduled worker; Zach + Claude Code execute via _ops/dev/ handoffs
  92|      brands: {tripgogo: active, splitgogo: in_progress, tg4b: pre-launch}, workers: [], status: active}
  93|   - {key: finance, name: "Finance", scope: matrixed, head: "_ops/departments/finance/HEAD.md",
  94|      # STAFFED 2026-06-26: onnixus-finance-agent (on-demand + monthly close; Mac-side, needs prod-DB SSH + iCloud docs root). Harness: _ops/departments/finance/FINANCE_AGENT.md (implements AI Automation Playbook B5)
  95|      brands: {tripgogo: idle, splitgogo: active, tg4b: idle}, workers: ["onnixus-finance-agent (on-demand)"], status: building}
  96|   - {key: legal, name: "Legal & corporate", scope: matrixed, head: "_ops/departments/legal/HEAD.md",
  97|      # intentionally UNSTAFFED -> founder + counsel led, not a missing agent. 'corp' is a deliberate non-brand entity (corporate/BV), kept outside the 3-brand matrix
  98|      brands: {splitgogo: needs_attention, corp: active}, workers: [], status: awaiting}
  99|   # PERSONAL ENTITY: "zach-scott" is Zach himself, a non-business entity alongside the 3 product brands
 100|   # (Onnixus OS is becoming a general agent-management tool spanning business + personal). Job Applications
 101|   # is its first department. PRIVATE stream (never sync, never expose externally). The files live in the
 102|   # separate "Job Applications" project (../Job Applications/); this registry + the dashboard point at them.
 103|   - {key: job-applications, name: "Job Applications", scope: personal, entity: zach-scott,
 104|      head: "_ops/departments/job-applications/HEAD.md", private: true,
 105|      # the four "employees"; on-demand; SKILL files live in ../Job Applications/_ops/agents/
 106|      workers: [job-search-agent, resume-writer, cover-letter-writer, "interview-prep-agent (planned)"],
 107|      brands: {zach-scott: active}, status: active}
 108|   - {key: personal-finance, name: "Personal Finance", scope: personal, entity: zach-scott,
 109|      head: "_ops/departments/personal-finance/HEAD.md", private: true,
 110|      # Zach's automated personal budget + 3-jurisdiction taxes. Workbook: Life/Finance/Household Budget (Master).xlsx; agent SKILL: ~/Claude/Scheduled/household-budget-ingest/
 111|      workers: ["household-budget-ingest"],
 112|      brands: {zach-scott: active}, status: active}
 113| 
 114| basecamp:
 115|   status: archived                  # kept for reference / optional Luis mirror only; NOT a sync dependency
 116|   account_id: "5993102"
 117|   project_bucket: "42954660"        # TripGoGo project
 118|   todoset_id: "8967179490"
 119|   # Optional one-way mirror only. The markdown files above are authoritative; nothing blocks on Basecamp.
 120| 
 121| calendar:
 122|   # Two calendars, both planner-managed:
 123|   work_id: "0452906b8d9aa60d1a14ac422d1399efea5e19d0f39064f6be3d5fccaa831981@group.calendar.google.com"  # "Daily Claude Schedule" — WORK blocks only
 124|   personal_id: "founder@example.com"   # PERSONAL anchors (morning routine, gym, meals) + life
 125|   home_timezone: "Europe/Amsterdam"
 126|   active_timezone: "America/Edmonton"    # WHERE ZACH IS NOW (Calgary). Plan in this tz.
 127|   # Travel-aware schedule — onnixus-tz-flip-amsterdam (one-time, Jul 1) flips anchors+job block back to Amsterdam.
 128|   timezone_schedule:
 129|     - {from: "2026-06-22", tz: "America/Edmonton", note: "Calgary"}
 130|     - {from: "2026-06-29", tz: "America/Edmonton", note: "fly back to Amsterdam — travel day, light/no work"}
 131|     - {from: "2026-06-30", tz: "Europe/Amsterdam", note: "settle / buffer"}
 132|     - {from: "2026-07-01", tz: "Europe/Amsterdam", note: "resume Amsterdam hours"}
 133|   # The planner writes work blocks to work_id and protects/maintains personal anchors on personal_id.
 134| 
 135| workday:
 136|   flexible: true                 # no fixed 9–18 window; fill work around real events + personal anchors
 137|   outer_bounds: ["08:00","21:00"]# soft sanity bounds — don't schedule work outside this unless an event forces it
 138|   structure: light               # 3–4 dynamic deep-work blocks/day + 1 agenda event; NO rigid recurring template
 139|   deep_blocks_per_day: 4         # target ceiling, not a quota
 140|   block_minutes: 90
 141|   personal_anchors:              # planner treats these as protected (they live on personal_id)
 142|     - "🌅 Morning routine"
 143|     - "🏋️ Exercise / gym"
 144|     - "🥗 Lunch"
 145|     - "🍽️ Dinner"
 146| 
 147| # Standing WORK blocks the planner keeps in place daily and schedules around (on work_id).
 148| standing_work_blocks:
 149|   - {key: income, name: "💼 Job search", minutes: 60, recurrence: daily, color: "5",
 150|      note: "1h/day job search + startup networking + co-founder hunt. STANDING until Zach says stop (found a job / no longer needs one). Time of day flexible."}
 151| 
 152| travel:
 153|   note: "Jun 29 = fly Calgary→Amsterdam (no/low work). Jun 30 = settle. Jul 1 = resume Amsterdam hours."
 154| 
 155| # How the planner should think about balance. Targets are GUIDES, not quotas —
 156| # the planner may deviate when deadlines/leverage justify it, but must surface when it does.
 157| priority_model:
 158|   factors:                      # what the planner weighs when choosing the day's focus
 159|     - hard_deadlines
 160|     - unblocking_dependencies   # e.g. sending Luis response unblocks B2B
 161|     - momentum                  # from CONTEXT.md open threads
 162|     - strategic_leverage
 163|     - income_runway_reality     # Zach needs near-term income while building Onnixus
 164|   neglect_alert_days: 7         # warn if an active stream gets 0 time for this many days
 165|   rebalance: "weekly_floors are minimums to protect; over-investment in one stream is flagged, not blocked"
 166| 
 167| # ── STREAM REGISTRY ───────────────────────────────────────────────────
 168| # fields: key, name, status(active|archived), shared(bool), basecamp_todolist(null=private),
 169| #         color(Google colorId), target_per_week (blocks, or 'posts:N' for content)
 170| streams:
 171|   - {key: luis_bv,   name: "🔺 Luis & BV / Equity",        status: active, shared: true,  basecamp_todolist: "Luis & BV / Equity",   color: "11", target_per_week: "2 blocks"}
 172|   - {key: tripgogo,  name: "🔵 TripGoGo (consumer)",        status: active, shared: true,  basecamp_todolist: "TripGoGo (consumer)",  color: "9",  target_per_week: "2 blocks"}
 173|   - {key: tg4b,      name: "🟣 TripGoGo for Business",       status: active, shared: true,  basecamp_todolist: "TripGoGo for Business", color: "3",  target_per_week: "2 blocks"}
 174|   - {key: splitgogo, name: "🟢 SplitGoGo",                  status: active, shared: true,  basecamp_todolist: "SplitGoGo",            color: "10", target_per_week: "2 blocks"}
 175|   - {key: marketing, name: "📣 Marketing",                  status: active, shared: true,  basecamp_todolist: "Marketing",            color: "6",  target_per_week: "posts:3"}
 176|   - {key: bd,        name: "🤝 BD / Investors / Customers",  status: active, shared: false, basecamp_todolist: null,                   color: "2",  target_per_week: "3 blocks"}
 177|   - {key: income,    name: "💼 Income: Job + Co-founder",    status: active, shared: false, basecamp_todolist: null,                   color: "5",  target_per_week: "2 blocks"}
 178|   - {key: direct_supply, name: "🟡 Direct-Supply Initiative", status: active, shared: true, basecamp_todolist: null,                color: "7",  target_per_week: "2 blocks"}  # cross-dept; roadmap in _ops/initiatives/direct-supply.md (governance layer)
 179|   - {key: finance_stack, name: "💰 Finance Stack", status: active, shared: true, basecamp_todolist: null,                color: "8",  target_per_week: "1 block"}  # cross-product finance/accounting standardization; roadmap in _ops/initiatives/finance-stack.md
 180|   # Example of how a new project slots in (uncomment + edit):
```

_Truncated: showing first 180 of 186 lines._
