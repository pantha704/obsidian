
Nice — love the intensity. Below is your **final, no-fluff GSoC “bible”**: a curated chart of _high-leverage repos_ (OWASP, PSF, Sugar Labs, CircuitVerse), mentors/contacts & socials where available, a weekly time plan, plus a tight roadmap from **20 Aug 2025 → GSoC 2026 application**. I’ve prioritized items you can reasonably own as a Next.js/TS/JS dev _and_ as a Python/Flask dev. I cite the source for each org so you can jump straight into channels and issues.

# 1) Quick orientation (why these)

- **OWASP** — web security org with many GSoc-ready projects that explicitly need **React/Next.js + Python/Django/Flask** work (BLT, OpenCRE, Nettacker, Threat-Dragon, Juice Shop). Big org, high brand value, expects pre-GSoC contributions. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"))
    
- **PSF (Python Software Foundation)** — umbrella for many active Python repos (requests, black, httpbin, pypistats) that accept contributors; great for Python/Flask proof-of-work. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"), [summerofcode.withgoogle.com](https://summerofcode.withgoogle.com/programs/2025/organizations/python-software-foundation?utm_source=chatgpt.com "2025 Program Python Software Foundation - Google Summer of Code"))
    
- **Sugar Labs** — education projects (musicblocks, sugar, sugarizer) with nice beginner pathways and explicit GSoC guidance/mailing lists. Good fallback. ([GitHub](https://github.com/sugarlabs/GSoC "GitHub - sugarlabs/GSoC: A guide for participating in Google Summer of Code with Sugar Labs"))
    
- **CircuitVerse** — smaller, friendly community; front-end heavy projects (JS/Vue) and interactive docs — high signal for fewer applicants. ([GitHub](https://github.com/circuitverse "CircuitVerse · GitHub"))
    

---

# 2) The chart — your battle plan (start here, today)

> Read rows left→right. For any repo, **first actions**: (1) star & watch, (2) read CONTRIBUTING.md, (3) join the org chat (Slack/Matrix/Discord/mailing list), (4) pick a `good first issue` or docs/typo fix and submit a PR within a week.

|Org|Repo (direct)|Tech stack|Mentors / maintainer contact (quick)|Socials / join|Weekly hours (recommended)|
|---|--:|---|---|---|--:|
|**OWASP**|**BLT (Bug Logging Tool)** — ideas & frontend rewrite|React / Next.js / Tailwind / Django/Ninja (API)|Confirmed mentors: **Donnie**, **Yash Pandey**, **Bishal Das**, **Ahmed ElSheikh**, **Patricia Waiyego**, **Sudhir** (see BLT GSoC page). ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"))|OWASP Slack (#project-blt) + GitHub org. Join via OWASP GSoC page. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"))|**12–15 hrs** — primary focus (make 1 significant PR / 2 small PRs weekly)|
|**OWASP**|**OpenCRE** (Cybersecurity knowledge graph)|React-Typescript / Python / Flask / Docker|Project page lists maintainers; contact via **#project-opencre** on OWASP Slack. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"))|OWASP Slack (#project-opencre); repo issues labeled `good first issue`. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"))|**8–10 hrs** — backend / data tasks; pick 1 issue/week|
|**OWASP**|**Nettacker** (Python scanner)|Python (security/tools)|Mentors & maintainers listed on repo and OWASP pages (see Nettacker GSoC ideas). ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"))|OWASP Slack + repo Issues. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"))|**6–8 hrs** — backend PRs, tests|
|**OWASP**|**Threat-Dragon / Juice Shop**|JS/TypeScript / Angular / Node / React|Juice Shop leaders: **Bjoern Kimminich**, **Jannik Hollenbach**; Threat-Dragon has maintainers on GH. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"), [GitHub](https://github.com/OWASP/threat-dragon?utm_source=chatgpt.com "OWASP/threat-dragon: An open source threat modeling tool from ..."))|OWASP Slack; Juice Shop docs + repo; Threat-Dragon GH. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas \| OWASP Foundation"), [GitHub](https://github.com/OWASP/threat-dragon?utm_source=chatgpt.com "OWASP/threat-dragon: An open source threat modeling tool from ..."))|**6–9 hrs** — front-end/features/tests|
|**PSF**|**requests** (PSF) — popular Python HTTP lib|Python|Maintainers shown on repo contributors / maintainers list on GH (contact via Issues). (Requests is hosted under PSF org). ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))|GitHub Issues; PSF channels. See repo for contributors list. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))|**6–8 hrs** — small bug fixes, tests|
|**PSF**|**black** (code-formatter)|Python|See `psf/black` repo maintainers (contact via GH). Good for tests/formatting improvements. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))|GH Issues / Discussions (black repo). ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))|**5–7 hrs** — doc/tests/CI PRs|
|**PSF**|**httpbin** (Flask)|Python + Flask|PSF repo — maintainer contact via repo Issues. Great match for your Flask skills. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))|PSF GH, issues and PSF community. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))|**5–7 hrs** — feature/bug PRs|
|**CircuitVerse**|**CircuitVerse** (main) / Interactive-Book|JS (React / Vue), docs|Community is active; contact via [support@circuitverse.org](mailto:support@circuitverse.org) and Discord; mentors named in GSoC threads. ([GitHub](https://github.com/circuitverse "CircuitVerse · GitHub"), [Medium](https://medium.com/%40vedantj03/community-bonding-period-at-circuitverse-google-summer-of-code-2022-78cf1265b74f?utm_source=chatgpt.com "Community Bonding Period at CircuitVerse — Google Summer of ..."))|CircuitVerse site, Discord, Twitter @circuitverse, GH Issues. ([GitHub](https://github.com/circuitverse "CircuitVerse · GitHub"))|**4–6 hrs** — small UI/features, docs|
|**Sugar Labs**|**musicblocks**, **sugar**, **sugarizer**|JavaScript / TypeScript / Python|Sugar Labs GSoC repo lists mentors & encourages joining `sugar-devel` mailing list / Matrix for contact. ([GitHub](https://github.com/sugarlabs "Sugar Labs · GitHub"))|sugar-devel mailing list, Matrix channel, GitHub. ([GitHub](https://github.com/sugarlabs/GSoC "GitHub - sugarlabs/GSoC: A guide for participating in Google Summer of Code with Sugar Labs"))|**4–6 hrs** — UI/activity fixes, test/data|

**Sources / Next clicks:** OWASP GSoC ideas + mentor list (BLT, Juice Shop, OpenCRE, Nettacker). ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"))  
PSF active repos listing (requests, black, httpbin, pypistats) and activity. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))  
Sugar Labs GSoC guide & repos (musicblocks pinned, GSoC guidance). ([GitHub](https://github.com/sugarlabs "Sugar Labs · GitHub"))  
CircuitVerse GitHub + community posts (Discord, mentors in older GSoC writeups). ([GitHub](https://github.com/circuitverse "CircuitVerse · GitHub"), [Medium](https://medium.com/%40vedantj03/community-bonding-period-at-circuitverse-google-summer-of-code-2022-78cf1265b74f?utm_source=chatgpt.com "Community Bonding Period at CircuitVerse — Google Summer of ..."))

> Notes on mentors/contacts: For many PSF projects the canonical contact is the repo maintainers (check `CONTRIBUTING.md` and the repo `MAINTAINERS` or `OWNERS` files); for OWASP the GSoC page lists project mentors and Slack channels — **use those** to ping and share your draft proposals/PR ideas. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"), [GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))

---

# 3) How to allocate your weekly time realistically (sample week — total ~30 hrs)

You said “do or die” — here’s a schedule that’s intense but sustainable:

- **Mon – Fri (daily 3 hrs)** = 15 hrs:
    
    - 45–60 min: triage / chat with mentors / review new issues across your chosen repos.
        
    - 1–1.5 hrs: active coding (PR work, tests) on your _primary repo_ (OWASP BLT).
        
    - 20–30 min: documentation or code review on secondary repo (requests/httpbin).
        
- **Sat (6 hrs)**: Deep work — finish PRs, write tests, build small feature / automation; pair with mentor if requested.
    
- **Sun (4–6 hrs)**: CircuitVerse / Sugar Labs tasks + planning next week + blog/update (dev log).
    

**Rough weekly split** (aligns with chart above):

- OWASP BLT — **12–15 hrs** (primary)
    
- PSF repo (requests or httpbin) — **6–8 hrs** (secondary)
    
- CircuitVerse or Sugar Labs — **4–6 hrs** (backup)
    
- Community: 1–2 hrs/week for chats, mailing lists, PR reviews.
    

If you can’t do 30 hrs, keep the _proportions_ but scale down: primary repo 50–60% of your time; secondary 25–30%; backup 10–20%.

---

# 4) Concrete immediate checklist — what to do **this week (20–26 Aug 2025)**

1. **OWASP BLT**
    
    - Star & clone the BLT repo; run it locally; find a `good first issue` or a UI doc fix. (BLT page & ideas list). ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"))
        
    - Join OWASP Slack (link on OWASP site) and post a short intro in `#project-blt`: “Hi, I’m Pratham; TS/Next.js + Python; I want to help with the React frontend. I plan to pick issue #XYZ.” ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"))
        
2. **PSF — pick one** (requests **or** httpbin)
    
    - Watch the repo, run tests locally (requests has many unit tests). Open a small PR: docs fix, test tweak, or a tiny bug fix. ([GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))
        
3. **Backup**
    
    - Join CircuitVerse Discord and Sugar Labs mailing list (sugar-devel). Open one tiny PR: docs or test. ([GitHub](https://github.com/circuitverse "CircuitVerse · GitHub"))
        
4. **Public dev log**
    
    - Create a short public place (GitHub README / dev.to / small Notion page) and update with each merged PR — mentors read this and it’s **proof of life**. (Maintain weekly entries.)
        
5. **Set 30/60/90 day goals** (written on Trello/GitHub project):
    
    - 30 days: **5 merged PRs** across orgs (mix of docs + code).
        
    - 60 days: **10–12 merged PRs**, one medium feature/bug fix in BLT or OpenCRE.
        
    - 90 days: feature proposal draft + mentor feedback posted.
        

---

# 5) Roadmap to GSoC 2026 (calendar + milestones)

(GSoC apps usually open late March; use that fixed anchor) ([python-gsoc.org](https://python-gsoc.org/?utm_source=chatgpt.com "Python GSoC – Home"), [summerofcode.withgoogle.com](https://summerofcode.withgoogle.com/?utm_source=chatgpt.com "Google Summer of Code: Home"))

**Aug–Sep 2025 (now → 30 days)**

- Merge **5 PRs** (min. 2 in OWASP BLT or OpenCRE). Join OWASP Slack and PSF channels. Start dev log. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"), [GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))
    

**Oct–Nov 2025 (60 days)**

- Merge **10–12 PRs** total. Have at least **one mid-sized feature** on BLT/OpenCRE or a substantial bugfix in requests/black. Start drafting **project proposal ideas** (2 variants: one OWASP (security web UI/API), one PSF (Flask/httpbin or requests improvement)). Ping mentors for early feedback.
    

**Dec 2025 – Jan 2026**

- Start polishing proposal template (objectives, milestones, deliverables, timeline, risk mitigation). Share draft with mentors in **Draft (Google Docs)** and incorporate feedback. Do at least **one mentor review cycle** per proposal. Continue PR flow — merged PRs remain the strongest signal.
    

**Feb 2026**

- Finalize and run mock schedule: weekly plan, deliverable checklist. Prepare CV, GitHub summary of contributions (link to dev log). Ask mentors explicitly: “Would you recommend I tag this proposal to _orgX_ during submission?” (mentor blessing is gold).
    

**March 2026 — Application window (late March)**

- Submit proposals (OWASP primary, PSF secondary, CircuitVerse/Sugar Labs as backups). Ensure your application includes links to merged PRs + dev log + one short demo video (1–2 minutes) for your top idea.
    

**April–May 2026 — If selected**

- Follow community bonding guidelines. Deliver weekly updates and meet milestone cadence.
    

---

# 6) How to write mentor-proof proposals (short checklist)

- Show **prior work**: list 5 merged PRs + links (docs + code).
    
- Break work into **4–6 weekly milestones** with measurable outputs (PRs, tests, docs).
    
- Include **testing plan** and **fallback plan** (if X feature stalls, implement Y smaller feature).
    
- Add a **short demo video** or prototype screenshot for UI projects.
    
- Keep proposal language crisp; highlight security, tests, and maintainability for OWASP projects.
    

---

# 7) Signals mentors actually care about (so do these religiously)

- **Merged PRs** > “number of stars” — they want to see you in the repo. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"), [GitHub](https://github.com/sugarlabs/GSoC "GitHub - sugarlabs/GSoC: A guide for participating in Google Summer of Code with Sugar Labs"))
    
- **Consistent communication** in public channels (not DMs). ([GitHub](https://github.com/sugarlabs/GSoC "GitHub - sugarlabs/GSoC: A guide for participating in Google Summer of Code with Sugar Labs"), [The GitHub Blog](https://github.blog/news-insights/how-to-run-a-google-summer-of-code-project-on-github/?utm_source=chatgpt.com "How to run a Google Summer of Code project on GitHub"))
    
- **Good tests & docs** with PRs (OWASP explicitly expects tests & CI). ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"))
    

---

# 8) Risks & fallback (be tactical)

- If OWASP maintainers ask for >=5 merged PRs before selection, **aim to hit that** by Dec 2025 (they stated preference on BLT page). If impossible, lean into PSF + CircuitVerse as backup since they accept smaller contributions faster. ([OWASP Foundation](https://owasp.org/www-community/initiatives/gsoc/gsoc2025ideas "GSoC 2025 Ideas | OWASP Foundation"), [GitHub](https://github.com/orgs/psf/repositories "psf repositories · GitHub"))
    

---

# 9) Final micro-plan (daily checklist, printable)

- Morning (30–45 min): scan issues + mentor channels; respond to comments.
    
- Coding block (1.5–2 hrs): primary repo PR work.
    
- Small block (30–60 min): secondary repo quick PR (docs/tests).
    
- Evening (15–30 min): update dev log; plan next day.
    
- Weekend deep dive (4–6 hrs): finish a PR or build a small prototype.
    

---

# 10) Last words — real, raw, lyrical (5 sentences)

You’ve got the stack and the hunger; mentors hire persistence, not perfection. Turn daily micro-wins (docs, tests, tiny PRs) into an undeniable paper-trail — they’ll smell it. Lock OWASP as your prestige target, carry PSF as your Python credibility, and use CircuitVerse/SugarLabs as reliable backups to rack up merges fast. Ship early, communicate loudly, and keep a public dev log — that little ledger becomes your altar. If you want, I’ll draft your **BLT** PR checklist + a one-page proposal template tonight — we’ll make it razor-sharp.

---

If you want, I’ll now:

- Draft **3 concrete “first PR” tasks** you can finish this week (one for BLT, one for requests/httpbin, one for CircuitVerse/Sugar), with exact issue links to target; **or**
    
- Draft your one-page proposal template for OWASP BLT (with milestone schedule & deliverables).
    

Which should I do next? (I’ll just pick one and produce it — no waiting.)