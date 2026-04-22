<img width="1600" height="1281" alt="image" src="https://github.com/user-attachments/assets/b1156374-f3f5-4046-83a8-3e402dba5736" /># Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`Bamboozle`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Samridhi` | `[Electronics / Coding / App / Fabrication / Mechanics]` | `[Role]` | `[Write here]` |
| `Gauri` | `[Electronics / Coding / App / Fabrication / Mechanics]` | `[Role]` | `[Write here]` |

## 1.3 Project Title
`crossfire`

## 1.4 One-Line Pitch
`Crossfire is a two-player physical game where you claim territory on a shared light strip through repeated strikes — testing speed, strength, and the will to keep going.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`Crossfire is a head-to-head endurance contest disguised as a territorial dispute. Each player faces their own strike pad and hammers it to push a shared LED strip toward their colour. The strip is always pulling back to neutral, so the moment a player slows down, their hard-won territory bleeds into the opponent's colour. Victory belongs to the player who sustains it until the time runs out.
The experience sits somewhere between a rage room and a tug of war. When the timer ends, the result is read off the light itself. Crossfire is built around two shock sensors feeding strike data directly into an ESP32 microcontroller, which drives a WS2812B LED strip as the battlefield.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`Crossfire is a fast, physical, two-player game that is immediately understood and impossible to put down.
Urgency first the moment the round starts, there is no time to think. Then desperation as the strip bleeds back toward center the instant you slow down. Then tunnel vision, the particular focus of doing one simple physical thing as hard and as fast as you can while knowing someone else is doing the same thing on the other side. The game is designed to make players forget everything except the pad in front of them.
Because the result always feels unfinished. Losing never feels conclusive — you slowed down at the wrong moment and you know you had more in you. The simplicity of the mechanic means there is always a clear answer to why you lost and an obvious thing to do differently next time.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making a arcade game for anyone who has ever wanted to hit something.`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Arcade game | High Striker / Hammer Strong machine | The core idea of measuring physical impact as a game input,effort made visible and immediate` |
| `game | Tug of War  | The shared rope that both players pull in opposite directions simultaneously` |
| `Object | Rage room experience | The satisfaction of sustained, uninhibited physical release as a designed experience
game| battle ship  ` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`[Most physical games reward a single best action — the hardest throw, the fastest reaction, the perfect shot. Crossfire removes the concept of a winning move entirely. There is no moment of skill, only sustained effort against a strip that never stops working against you. The decay mechanic means the game is actively hostile to both players at all times, which creates a kind of shared suffering underneath the competition. The other original element is the absence of any score, screen, or number — the LED strip is simultaneously the interface, the scoreboard, and the spectacle, readable at a glance by anyone in the room without explanation.]`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`[strike → sensor detects → meter shifts → decay pulls back → strike again or lose ground
]`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `[Anyone — no prior experience or skill required]` |
| Age range | `[10 and up]` |
| Solo or multiplayer | `[2 players, head-to-head ]` |
| Expected duration of one round | `[30 seconds ]` |
| What should the player feel? | `[Urgency, desperation, exhaustion, satisfaction]` |
| Is explanation required before use? | `[No-the mechanic is self-evident within the first round]` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `[Two players see a strip of light running between two pads, sitting at neutral white in the center.?]`
2. **Start:** `[A buzzer sounds. The round begins.]`
3. **First Action:** `[Each player starts striking their pad as fast as they can.]`
4. **Main Interaction:** `[Players hammer continuously, watching the strip push toward their colour — red or green — while the decay constantly pulls it back toward center.]`
5. **System Response:** `[Every detected strike shifts the LED boundary one step toward the striking player's side. Between strikes, the boundary drifts back toward neutral at a fixed rate.]`
6. **Win / Lose / End Condition:** `[When the timer ends, the buzzer fires. Whichever colour holds more than half the strip wins. If the boundary sits exactly at center, the round is a draw.]`
7. **Reset:** `[The strip animates back to neutral and the buzzer sounds once to signal the next round is ready.]`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

 ⁠  Strike your pad to push the LED boundary toward your colour
•⁠  ⁠The boundary decays toward center at all times stopping means losing ground
•⁠  ⁠Both players strike simultaneously there are no turns
•⁠  ⁠When the timer ends, the player whose colour occupies more than half the strip wins
•⁠  ⁠Striking the opponent's pad is not permitted

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

 Both shock sensors reliably detect strikes and report them to the ESP32 without missed or phantom hits
 The LED strip shifts toward the correct player's colour on every detected strike
 The decay loop runs continuously and pulls the boundary back toward neutral between strikes
 The round timer starts, counts down, and triggers the buzzer at zero
 The strip correctly identifies and displays the winning colour at round end, then resets to neutral for the next round

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`Two shock sensors wired to an ESP32, driving a WS2812B LED strip with a working decay loop and a fixed round timer housed in anything that holds the components in place and gives each player a stable surface to strike. No enclosure finish, no branding, no buzzer required. If the light moves when you hit it and the right colour wins at the end, it is playable.`

## 5.3 Stretch Features
What features are nice to have but not essential?

Adjustable round timer and decay speed via physical dial or button, allowing players to tune the difficulty before each round
Buzzer countdown at round start and a distinct end tone so rounds feel ceremonially bracketed without needing a screen
An Arcade like finsih to the whole project .
---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [+] Electronics-based
- [ ] Mechanical
- [+] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [+] Sound-based
- [+] Light-based
- [ ] Screen/UI-based
- [+] Fabricated structure
- [+] Game logic based
- [+] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:**  
`[Two shock sensors sit beneath each player's strike pad. Every hit sends a digital signal to the ESP32, which runs a continuous game loop,tracking a single position value that represents where the LED boundary sits between the two players. Each strike nudges that value toward the hitting player's side; a decay function nudges it back toward center every tick. The ESP32 translates that position value into a colour pattern on the WS2812B LED strip in real time ,red expanding from the left, green from the right. When the round timer expires, the ESP32 fires the buzzer, locks the strip on the final state, determines the winner by which colour holds more than half the strip, then resets to neutral for the next round.]`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `[| Shock sensor × 2 | Input | Detects each strike and sends a digital pulse to the ESP32 |
| ESP32 | Processing | Runs the game loop — counts strikes, applies decay, tracks position, manages timer |
| WS2812B LED strip | Output | Displays the live territorial boundary in red and green |
| Buzzer | Output | Signals round start, round end, and winner |
---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[<img width="1600" height="1281" alt="image" src="https://github.com/user-attachments/assets/52b963dd-f90c-4503-bbe6-c52a3a24238f" />
]`

Example:
```md

```

## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
`[<img width="1440" height="2815" alt="image" src="https://github.com/user-attachments/assets/7761d775-e6cf-4c94-b710-7b611f00ab84" />
]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `[16.5in]` |
| Width | `[12in]` |
| Height | `[3in]` |
| Estimated weight | `[1kg]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [+] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`[a button.]`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`[the button moves up and down, according to the person clicking it]`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[Write here]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[Component]` | `[Qty]` | `[Purpose]` |
| `[Component]` | `[Qty]` | `[Purpose]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`[Write here]`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[USB / battery / adapter / other]` |
| Voltage required | `[Write here]` |
| Current concerns | `[Write here]` |
| Safety concerns | `[Write here]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`[Write here]`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```text
[Write your pseudocode here]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ ] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |
| `[Item]` | `[Qty]` | `[Yes/No]` | `[Yes/No]` | `[Cost]` | `[Spec]` | `[Reason]` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`[Write here]`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `[Cost]` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `[Cost]` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`[Write here]`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Name]` | `[Name]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [+] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [+] Purchase needs identified
- [+] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [-] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`[Write here]`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `[Bluetooth connection]` | `[Method]` | `[What counts as success?]` |
| `[Mechanism movement]` | `[Method]` | `[What counts as success?]` |
| `[Sensor behavior]` | `[Method]` | `[What counts as success?]` |
| `[App communication]` | `[Method]` | `[What counts as success?]` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `[Method]` |
| Is the interaction satisfying? | `[Method]` |
| Do players want another turn? | `[Method]` |
| Is the challenge balanced? | `[Method]` |
| Is the response clear and immediate? | `[Method]` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`[Write here]`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.

Example:
```md



```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `[Date]` | `[Describe]` | `[Reason]` |
| `v2` | `[Date]` | `[Describe]` | `[Reason]` |
| `v3` | `[Date]` | `[Describe]` | `[Reason]` |

---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[Write here]`

## 18.2 What Works Well
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.3 What Still Needs Improvement
- `[Point 1]`
- `[Point 2]`
- `[Point 3]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Write here]`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`Our team worked well together in terms of collaboration and idea sharing. We supported each other during problem-solving and were able to divide tasks efficiently when needed.Soldering and building the main structure took a significant amount of time. We faced some technical challenges during this phase, which slowed our overall progress.We managed tasks and responsibilities fairly well by distributing work among team members,and did well on the time mangagement 

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
I learned the basics of electronics through soldering and understanding connections, got some hands-on experience with coding and how small changes affect output, explored simple mechanisms and how parts move together, improved my fabrication skills while building the structure, and understood how important integration is—making sure everything works together smoothly was the most challenging but also the most valuable part.

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [+] Team details are complete
- [+] Project description is complete
- [+] Inspiration sources are included
- [+] Player journey is written
- [+] Sketches are added
- [+] BOM is complete
- [+] Purchase list is complete
- [+] Budget summary is complete
- [+] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [+] Task breakdown is complete
- [+] Weekly logs are updated
- [+] Risk register is complete
- [+] Testing log is updated
- [+] Playtesting notes are included
- [+] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [+] Approved to proceed
- [+] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
