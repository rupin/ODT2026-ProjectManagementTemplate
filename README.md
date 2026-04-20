# Open Design and Technology  
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

`ODT-2026-Team13_Ananya_and_Zoya`

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
`[Group 13]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `[Ananya]` | `[Electronics / Coding / App / Fabrication / Mechanics]` | `[Role]` | `[Write here]` |
| `[Zoya]` | `[Coding / App / Fabrication / Mechanics]` | `[Electronics ]` | `[Sequencing Logic,Integration,Systems Thinking]` |

## 1.3 Project Title
'Psychedelicacy`

## 1.4 One-Line Pitch
`Card-operated dispenser that detects card swipe via IR sensor, flashes pink loading lights, then swings servo flap open with green confirmation to dispense candy.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**
`Psychedelicacy is a playful card-activated dispenser that lights up and swings open to release a surprise treat when you swipe a card past an IR sensor.It captures that exciting "did it work?" moment as the pink lights chase around,building anticipation before green floods in and the flap swings open to drop your treat creating a simple, responsive, and surprisingly addictive moment.
What makes it fun is the playful rhythm: the quick sensor ping, the glowing buildup, and that satisfying servo whirr delivering instant payoff.Each swipe feels like a mini game with reliable magic, sparking curiosity for "one more go." It's powered by an IR sensor for detection,NeoPixel LEDs for vibrant feedback and a servo for smooth delivery of the treat.`

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
`The experience is a small, tactile exchange where a person takes a simple action and receives a small treat as a response.It is designed as a playful, hands-on moment rather than just a machine transaction, so the experience feels more like an interaction than a purchase.
The participant should feel curious, amused and rewarded. The goal is to create a light sense of anticipation before the treat arrives, followed by a small burst of satisfaction when it does.
Someone would want to try it again because the experience is quick, easy, and pleasantly repetitive.The combination of curiosity, control and instant reward makes it feel enjoyable each time, almost like a tiny game they can return to.
`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making a playable object for mixed audience.`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Object` | `Vending machine card reader` | `Simple swipe detection creating  "contactless" activation` |
| `Toy` | `Gumball machines	` | `Variable timing builds emotional investment while linear file advances automatically into rotating scoop; copied this for candies naturally sliding into quarter-circle "trap" on servo return which is based on gravity.` |
| `Toy` | `Pez dispensers` | `Head rotates 90° to capture candy from vertical stack, then back releases exactly one; taught how a  quarter-circle depth positioning naturally meters single candies` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`The dispensing mechanism draws from the PEZ dispenser's single-file candy stacking and the revolver cylinder's rotary chamber logic, but reimagines both in a new way,a quarter-circle servo-driven cavity that uses gravity and hole depth to release exactly one candy per trigger, without springs or complex mechanical parts.Combined with an IR-based card swipe replacing a traditional coin slot, the entire system achieves touchless, one-at-a-time dispensing using just a servo and a sensor , making it simpler, cheaper and more hygienic than any existing consumer dispenser design.`

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
`swipe card → IR detects → pink lights animation → green flash + servo dispenses/rotates → servo flap resets + lights off → repeat`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Anyone craving a quick hit of playful delight from everyday spaces-Impulse-driven kids in malls,arcade enthusiasts` |
| Age range | `Age-inclusive - 4 - 60` |
| Solo or multiplayer | `Solo` |
| Expected duration of one round | `4–5 seconds `|
| What should the player feel? | `Enchanting "just one more" compulsion` |
| Is explanation required before use? | `No,intuitive "swipe = reward" can be discovered with the help of card slot placement at the front` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `Notices glowing NeoPixels and queued candies in a desk-sized dispenser`
2. **Start:** `Spots IR sensor slot labeled "Swipe card here →"`
3. **First Action:** `Swipes the card - kept there`
4. **Main Interaction:** `Watches pink "loading" lights chase around ring during 1-second anticipation build`
5. **System Response:** `Green flood lights and servo whirr as quarter-circle pocket rotates 90°, dropping exactly one candy through hole`
6. **Win / Lose / End Condition:** `Not applicable - Candy falls out always`
7. **Reset:** `Flap smoothly returns to 0°, lights turn off, sensor immediately ready for new cycle`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `Not applicable`
- `Not applicable`
- `Not applicable`
- `Not applicable`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [1] `Card swipe reliably triggers-any card past IR sensor consistently detects within 2cm`
- [1] `Exactly one candy per activation-quarter-circle servo pocket releases single candy every time`
- [1] `Full light show executes-pink loading animation (1s) → green dispense → lights off, all NeoPixels respond instantly without flicker`
- [1] `Smooth mechanical reset-servo returns to 0° position after every dispense, ready for next swipe within 4 seconds total cycle`
- [1] `Runs continuous cycles without sensor false triggers, motor stall or LED failure`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`IR sensor detecting motion → single LED blinks → servo rotates 90° to drop one candy → returns to load next`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Sound effects-  buzzers play jingle or  chime during pink lights, "ka-ching" on dispense`
- `Candy counter display- small screen shows "Candies left: 23" to build urgency as hopper empties`
- `Wireless tally- Bluetooth to phone app tracks swipes or phone motion is used to dispense candy`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [1] Electronics-based
- [1] Mechanical
- [1] Sensor-based
- [ ] App-connected
- [1] Motorized
- [ ] Sound-based
- [1] Light-based
- [ ] Screen/UI-based
- [1] Fabricated structure
- [ ] Game logic based
- [1] Installation / tabletop experience
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
`Input: Card swipes break the IR sensor beam (Pin 34 detects proximity/motion).
Processing: ESP32 microcontroller confirms detection with 50ms debounce, then triggers light sequence and servo motion.
Output:
NeoPixel ring (16 LEDs, Pin 2): Pink chasing animation (1s loading) → green flood (dispensing)
Servo motor (Pin 5): Quarter-circle pocket rotates 0°→90°→0° to release exactly one candy
Physical structure: Linear candy queue feeds into deep quarter-circle servo pocket—gravity naturally loads next candy when flap returns to home position.`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| ` Sensor` | Input | `IR sensor detects card swipe by beam interruption` |
| `[ESP32 ` | Processing | `Reads sensor → double-checks signal → runs light sequence → controls servo timing → loops for next activation` |
| `[LED / Servo ` | Output | `Neopixel-Pink chasing animation (loading feedback) → green flood (dispensing confirmation) → off (ready state)/Rotates quarter-circle pocket 0°→90°→0° to scoop and release exactly one candy from queue` |
| `Quarter-circle Candy Pocket` | Physical Action | `Deep pocket traps single candy by geometry; gravity auto-refills from linear queue on return to 0°` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`https://github.com/academicsananya1234-ship-it/ODT2026-group13-sec-B/blob/zoya---branch/images/concept-sketch.jpg`

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
`https://github.com/academicsananya1234-ship-it/ODT2026-group13-sec-B/blob/zoya---branch/images/labelled_build_sketch.jpg`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `35cm` |
| Width | `35cm` |
| Height | `32cm` |
| Estimated weight | `850g` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [1] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [1] Hinges
- [1] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [1] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`Gear shaft on servo drives quarter-circle pocket as single-index metering chamber-linear candy queue gravity-feeds into deep pocket arc. Servo rotates exactly 90° via hinge mount, sliding card guide aligns pocket hole with exit chute to release trapped candy. Return to 0° naturally scoops next candy from queue via pocket depth geometry + slider mechanism. Pure rotational scoop and gravity reload for reliable single-dispensing.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`What moves: Quarter-circle candy pocket attached to servo horn
What causes movement: ESP32 triggers PWM signal to servo motor (Pin 5, 50Hz) after IR sensor confirms card swipe
How far it moves:0° (home, candy loading) → 90° (dispense, hole aligned with chute) → 0° (reset)
Total: 180° per cycle (90° out + 90° back)
How fast it moves:
settle_ms=300ms at 0° (gentle start)
settle_ms=800ms at 90° (allows candy fall)
settle_ms=500ms return to 0° (quick reset)
Total cycle: ~2.1 seconds motion
What could go wrong:
Servo stall/jam—candy too big for pocket depth 
Incomplete return—pocket stays partial-open, double-dispensing 
Backlash—loose servo horn causes sloppy 90° alignment 
Gravity hang-up—next candy doesn't load (solution: slight pocket tilt + vibration from settle delay)`

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
| `MicroPython` | `Main firmware on ESP32 for IR sensor reading, NeoPixel control, servo PWM timing, and main interaction loop` |
| `MIT App Inventor` | `Backup block-based prototyping for coin/card detection logic and servo control testing during development` |

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
`To create a card-operated dispensing mechanism using an IR sensor, servo motor, and NeoPixel LEDs-  It detects a card, shows visual feedback, and actuates a flap to dispense an item.
Startup Behavior
Positions the servo flap to 0° and turns off NeoPixels. Flashes the first NeoPixel pink then green twice, then prints "Ready. Waiting for coin..." to the console.
Input Handling
Monitors the IR sensor continuously in the main loop with a 50ms wait time.
Sensor Reading
The card_detected() function reads Pin 34 (IR sensor). It confirms detection with a 50ms debounce if the value is 0.
Decision Logic
Triggers dispensing only on confirmed card detection. There isnt multiple card handling—single detection per cycle.
Output Behavior
NeoPixels : Pink chasing animation during 1-second "loading," green fill during servo action, then off.
Servo : Moves 0° → 90° → 0° to open/close flap, using PWM at 50Hz with auto-deinit to stop vibration.
Prints "Coin detected!" and "Done. Ready for next coin." to console after each cycle.
Communication Logic
Console-only via print() statements for status.
Reset Behavior
After dispensing, waits 1 second, turns off lights, and loops back to sensor waiting for the next card swipe. Servo always returns to 0° post-dispense.`

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
`https://github.com/academicsananya1234-ship-it/ODT2026-group13-sec-B/blob/zoya---branch/images/code_flowchart.jpg <img width="1367" height="3700" alt="code_flowchart" src="https://github.com/user-attachments/assets/a967f372-5711-43b3-983b-c127b7237159" />
`

## 10.4 Pseudocode

```text
STARTUP:
    servo_move(0°)          // Position pocket to load candy
    flash NeoPixel pink+green 2x  // Welcome animation
    PRINT "Ready for card swipe"

MAIN LOOP FOREVER:
    READ IR sensor (Pin 34)
    
    IF sensor == LOW:
        WAIT 50ms                 // Debounce delay
        IF sensor STILL LOW:
            PRINT "Card detected!"
            
            // PROCESSING PHASE
            pink_loading_animation(1000ms)   // Pink chase effect
            
            // DISPENSE PHASE  
            green_fill_neopixels()         // Success lights
            servo_move(0°, 300ms)          // Settle home
            servo_move(90°, 800ms)         // Dump candy
            servo_move(0°, 500ms)          // Reload next candy
            
            neopixel_off()
            PRINT "Candy dispensed!"
            WAIT 1000ms                   // Brief pause
    
    WAIT 50ms                     
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [1] Yes
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
`The app acts as a backup payment and control system when the physical card/coin mechanism is unavailable or fails. It adds convenience by allowing users to add digital credit, reset balance, and send commands directly from their phone, making the candy dispenser more accessible, reliable, and interactive.`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `Bluetooth connect button` | `Connects the mobile app to the ESP32 dispenser wirelessly for communication and control.` |
| `Credit / Score display` | `Shows the current balance or available credits added by the user.` |
| `Add Credit button/ Reset button/Send button` | `Increases digital credit balance for candy dispensing./Clears the current credit and sets the balance back to zero./Sends the updated credit value or command to the dispenser system.` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`https://github.com/academicsananya1234-ship-it/ODT2026-group13-sec-B/blob/zoya---branch/images/credit-app_screen.png`

## 11.5 App Screen Flow

1. `Open the app and tap the Bluetooth Connect button to pair with the ESP32 candy dispenser.`
2. `Check current credit balance.`
3. `Tap Add Credit (₹1 / ₹2 buttons) or Reset to manage balance.`
4. `Press Send to transfer the credit value to the dispenser and activate candy dispensing.`

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
- [1] Idea finalized
- [ ] Core interaction decided
- [1] Sketches made
- [ ] BOM completed
- [1] Purchase needs identified
- [1] Key uncertainty identified
- [1] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [1] Electronics tests completed
- [ ] CAD / structure planning completed
- [1] App UI started if needed
- [1] Mechanical concept tested
- [1] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [1] Physical body built
- [1] Electronics integrated
- [1] Code connected to hardware
- [ ] App connected if required
- [1] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [1] Technical bugs reduced
- [1] Playtesting completed
- [1] Improvements made
- [1] Documentation completed
- [1] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `Finalize idea, sketches, BOM, identify risks, test feasibility` | `decided, rough sketches made, materials like foamboard/MDF identified, basic servo + sensor testing done` | `BOM not fully completed in first week, shifted focus to testing mechanism first` | `Complete BOM and finalize dispensing mechanism dimensions` |
| Week 2 | `Build subsystems, test electronics, start app UI as backup, structure planning` | `physical hand-built structure chosen` | `physical hand-built structure chosen` | `Build outer body and improve subsystem wiring` |
| Week 3 | `Integrate body, electronics, code, first working prototype` | `Foamboard/MDF body built, electronics mounted, code linked with servo + sensor, first working candy dispenser achieved-rotating disc` | `App connection kept optional backup i` | `Improve stability, candy flow, and user experience` |
| Week 4 | `test users, improve design, complete documentation` | `changed candy mechanism completely,Servo vibration reduced, dispensing timing improved, playtested with users, report and presentation completed` | `focused more on physical aspects` | `Prepare final demo and polish aesthetics` |

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
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[Write here]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
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
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
