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
`NARAYANI & SHARANNYA`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `SHARANNYA` | `[Electronics, Coding, Mechanics]` | `Equal` | `Materail handelling, coding, product design` |
| `NARAYANI` | `[Electronics, Coding, Mechanics]` | `Equal` | `coding, mechanics, product design` |

## 1.3 Project Title
`"DUNK IT" BOT`

## 1.4 One-Line Pitch
`DUNK IT- A cardboard robot that watches you shoot, reacts to every point, and happily cheers when you win`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`“Dunk It” is an interactive robot built around an ESP32 that transforms a simple basketball dunk into a responsive, game-like experience. Using an IR sensor, the system detects whether a shot is successful and triggers coordinated feedback through servo-driven movements, buzzer sounds, an OLED display, and NeoPixel LEDs. The robot doesn’t just register input, it reacts with expressive, almost character-like behavior, turning each attempt into a small performance rather than a passive outcome.

What makes the experience engaging is its immediacy and personality. A successful dunk is met with exaggerated celebration, while a miss resets the system, encouraging repeated attempts and adding a subtle competitive edge. This combination of physical interaction, real-time feedback, and playful animation creates a loop that is satisfying, slightly unpredictable, and hard to ignore, making the project both technically interactive and emotionally engaging.`

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
`“Dunk It” is a physical, interactive game where a player attempts to score a basket while the robot detects the outcome and responds instantly with movement, light, and sound. It turns a simple dunk into a reactive performance, where every attempt triggers a visible and audible reaction from the system.

A mix of anticipation, satisfaction, and mild pressure. The instant feedback creates excitement, the exaggerated celebration makes success feel rewarding, and the reset on failure adds just enough tension to keep it from feeling trivial.

Because it creates a tight feedback loop. Success feels disproportionately rewarding, failure is immediate but not punishing, and the system’s reactions make each attempt feel slightly different. That combination of challenge, response, and quick reset naturally pushes people to keep trying for a better outcome.`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making a playful interactive game for teens and young adults, especially in social or exhibition settings`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `CARDBOARD ROBOT` | `https://pin.it/1nHEcxNN6` | `2. Eyes = instant character; Those oversized, slightly awkward eyes do most of the emotional work. We were building something people subconsciously treat like a character. Our bot should “look back” at the user in some way. Material honesty matters; It’s clearly cardboard, and it doesn’t try to hide it. That raw, DIY aesthetic makes it approachable and playful instead of intimidating. For our project, visible components can actually make it more engaging, not less. Imperfection adds charm; It’s slightly wonky, a bit handmade, and that’s exactly why it feels alive. If our robot is too polished, it risks feeling like a product. A little roughness makes it feel like a creation.` |
| `AI CAR BOT` | `https://youtu.be/e-nbSGRFP4Q?si=4eBdy8xb-hPkSWW_` | `Screen → expressive face idea. The car uses a digital face to create emotion and personality. We didn’t literally copy the screen, but we translated that idea into a physical face with a single eye. Same goal, different execution. The focus is still on making the robot feel “alive,” not just functional. Visible tech as part of the aesthetic. The car bot openly shows sensors and components, making the tech part of the design. Our robot does this too, especially with the chest flap revealing internals. It adds curiosity instead of hiding everything. Simplified, playful form language. The car is not trying to look realistic. It’s chunky, minimal, almost toy-like. Our blue robot follows that same direction with bold shapes, bright colors, and a slightly exaggerated body. Emotional feedback loop. The biggest takeaway: interaction = reaction. Car explores → reacts. User dunks → robot reacts. Same loop, just adapted to a game context.` |
| `BASKET BALL` | `https://youtu.be/llVb-GMf-_g?si=U66pq5BbUfGLg1OE` | `We learned from basketball to design a simple, goal-driven interaction where a clear objective, immediate feedback, and quick reset create a satisfying loop of attempt, failure, and success that keeps users engaged and motivated to try again.` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`Our project becomes original through the way it tests reflexes and attention rather than just aiming skill. The button-enabled interaction forces quick decision-making, where the player has to respond at the right moment while processing multiple inputs at once, like visual cues on the OLED, timing, and the robot’s changing states. It shifts the experience from a simple physical task to a layered challenge that engages both reaction speed and focus.
 we brought together multiple different forms, mechanical parts, electronics, and interaction points, into one stable, cohesive structure.  Stability here isn’t just structural, it’s also experiential. Nothing feels disconnected or random.

By integrating reflex based gameplay, layered inputs, and even elements like the magnified OLED into a single system, we create a unified object where form, function, and interaction support each other. The result is something that feels intentional and complete, rather than a set of separate features awkwardly forced into the same box.
We also extend this interaction through small but thoughtful details, like using a magnifying glass over the tiny OLED to enlarge and emphasize visual feedback. This not only makes the display more readable but adds a slightly unusual, almost playful way of engaging with the system. Together, these elements create a more immersive experience where players are not just playing, but actively interpreting, reacting, and adapting in real time.`

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
`idle (blink) → button window opens → player presses → mouth opens → ball detected / missed → robot reacts (score or reset) → game restarts or continues
The interaction loop follows a cycle of anticipation, timed input, physical action, sensor detection, and expressive feedback, encouraging repeated play through immediate response and reset.`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `children and teenagers` |
| Age range | `8-15` |
| Solo or multiplayer | `solo` |
| Expected duration of one round | `3 minutes` |
| What should the player feel? | `Excited, curious` |
| Is explanation required before use? | `Yes` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `The player notices a small robot facing them, with a visible “face” and a prompt on the OLED screen. The blinking eyes and idle behavior signal that it’s waiting to be interacted with.`
2. **Start:** `The game begins automatically after the initial “READY?” and countdown sequence, drawing the player in without requiring setup.`
3. **First Action:** `The player watches for the “SHOOT!” prompt and quickly presses the button within the limited time window.`
4. **Main Interaction:** `After pressing, the robot opens its mouth (flap), and the player must immediately dunk or place the ball so it passes the IR sensor. This sequence repeats, requiring quick timing, coordination, and attention to both visual cues and physical action.`
5. **System Response:** `The robot reacts instantly. A successful shot triggers excited eye expressions, sound effects, and LED feedback, while a miss results in sad expressions, failure sounds, and a reset sequence.`
6. **Win / Lose / End Condition:** `The round ends either when the player successfully scores all required points (win) or misses a timing window or shot (lose), which immediately ends the run.`
7. **Reset:** `On a loss or after a win, the system resets the score and restarts the countdown sequence, allowing the player or the next participant to begin again.`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `Rule 1 - 1. Press on time
The player must press the button only when the “SHOOT!” prompt appears, within the limited time window.`
- `Rule 2 - 2. Act immediately after pressing
Once pressed, the player must quickly dunk or place the ball before the mouth closes.`
- `Rule 3 - 3. One mistake resets everything
Missing the timing window or failing to score resets the game back to zero.`
- `Rule 4 - 4. Complete all successful shots to win
The player must score all required points consecutively to complete the game.`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `Player can understand how to start and play after explanation`
- [ ] `System reliably detects button input and ball scoring using sensors`
- [ ] `Robot gives immediate, visible feedback (movement, light, sound) for every action`
- [ ] `Game loop (start → play → win/lose → reset) runs smoothly without breaking`
- [ ] `Interaction is engaging enough that players want to retry multiple times`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`A basic setup where a button press opens a servo “mouth” for a short time window, an IR sensor detects whether the ball passes through, and a simple output (buzzer or single LED) indicates success or failure. The loop resets immediately after each attempt.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Victory flags attached at the back of the robot.`
- `Buzzer`


---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [1 ] Electronics-based
- [ 1] Mechanical
- [1 ] Sensor-based
- [ ] App-connected
- [1 ] Motorized
- [1 ] Sound-based
- [1 ] Light-based
- [1 ] Screen/UI-based
- [ ] Fabricated structure
- [1 ] Game logic based
- [1 ] Installation / tabletop experience
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
`Input
The system takes input from a push button (player action) and an IR sensor (detects whether the ball passes through).

Processing
The ESP32 runs the game logic, checking if the button is pressed within the allowed time and whether the sensor detects a successful shot. Based on this, it decides if the player scores or fails.

Output
The robot responds through servo movement (opening/closing mouth, side motions), buzzer sounds, OLED visuals (eyes and text), and NeoPixel LEDs to indicate success, failure, or game states.

Physical Structure
All components are integrated into a single robot form where the mouth acts as the scoring mechanism, the eye display gives feedback, and the overall structure supports both interaction and stability.

App Interaction (if any)
There is no external app; the entire interaction is physical and self-contained, making it immediate and intuitive without needing a screen or device.`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Button+IR sensor` | Input | `Button captures player timing (press), IR sensor detects whether the ball passes through (score detection)  ` |
| `ESP32` | Processing | ` Runs game logic, checks timing and sensor input, decides win/lose/score states    ` |
| `Servo + Buzzer + OLED + NeoPixel LEDs` | Output | `Servos create movement (mouth/arms), buzzer gives sound feedback, OLED shows eyes/text, LEDs indicate score and reactions` |
| `Robot Body (Mouth/Flap + Structure)` | Physical Action | `Provides the interactive form where the ball is dunked, supports components, and enables physical gameplay interaction` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[attached in mages folder>scroll down till more pages]`

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
`[Upload image and link here]`

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `36.5 cm` |
| Width | `16 cm` |
| Height | `61 cm` |
| Estimated weight | `1.75 kgs` |

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
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [1 ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`The core mechanism is a servo-driven flap (the “mouth”) that opens for a limited time when triggered by a button press. This creates a short window in which the player must place or dunk the ball. An IR sensor positioned inside or behind the opening detects whether the ball successfully passes through during this window. Additional servos provide expressive movement, while the structure holds everything in alignment so the action is consistent and repeatable.

What it’s meant to do:
It’s designed to turn a simple action into a timed, reflex-based challenge. The mechanism enforces urgency by controlling when the player can act, and the sensor verifies success in real time. Together, it creates a clear cause-and-effect loop where the player’s timing and coordination directly determine the outcome, making the interaction engaging, responsive, and slightly stressful in a good way.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`What moves
The main flap ( scoring mechanism) and the side servos at the back move.

What causes the movement
The ESP32 triggers movement based on game states. A button press initiates the main flap opening, and scoring or winning triggers additional servo motions.

How far it moves
The mouth servo rotates roughly from 0° (closed) to 180° (fully open). The side servos move within a smaller range to create expressive gestures.

How fast it moves
The servos move quickly to create a short, timed window, with the mouth snapping open almost instantly and staying open for a controlled duration (a few seconds depending on level).

What could go wrong
Servos may jitter or not reach full angles, timing could be inconsistent, the flap might not align with the sensor, or mechanical stress could loosen parts over time. If timing or alignment fails, the player experience breaks because the detection no longer matches the action.`

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
| `ESP32` | `1` | `Main controller, running main logic` |
| ` Servo Motors ` | `3` | ` Control main flap and side movements for interaction and expression` |
| `OLED Display  ` | `1` | `Displays eyes, prompts, and game feedback` |
| `Push Button (Momentary NO)` | `1` | `Player input to trigger action (timing)` |
| ` IR Sensor  ` | `1` | `Detects whether the ball passes through (scoring)` |
| `Buzzer   ` | `1` | `Provides audio feedback for actions (win, fail, cues) ` |
| `NeoPixel LED Strip ` | `1` | ` Visual feedback for score and reactions` |
| `Buck Convertor LM2596 ` | `1` | `Powers the entire system` |
| `Mechanical Structure (Body + Flap)   ` | `1` | `Holds components and enables physical interaction ` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`Wiring Plan / Connections (ESP32)

1. Power Distribution

ESP32 → powered via USB or regulated 5V
Important: Use a separate 5V supply for servos + NeoPixels (they’re greedy)
All GNDs must be common (ESP32 GND + external supply GND)

2. Servos (x3)
Each servo has 3 wires: VCC (red), GND (brown/black), Signal (yellow/orange)

Mouth Servo signal → GPIO 13
Left Servo signal → GPIO 12
Right Servo signal → GPIO 14
All servo VCC → 5V external supply
All servo GND → common GND

3. OLED Display (I2C)

VCC → 3.3V (ESP32)
GND → GND
SDA → GPIO 21
SCL → GPIO 22

4. Push Button (Momentary NO)

One leg → GPIO 27
Other leg → GND
Uses internal PULL_UP, so:
Not pressed = HIGH
Pressed = LOW

5. IR Sensor

VCC → 3.3V or 5V (depends on module, usually 3.3V safe)
GND → GND
OUT → GPIO 33
Output: LOW when object detected

6. Buzzer (Active/Passive via PWM)

Positive → GPIO 26
Negative → GND

7. NeoPixel LED Strip (10 LEDs)

DIN → GPIO 25
VCC → 5V external supply
GND → common GND
(Optional but smart) Add:
330Ω resistor between GPIO and DIN
1000µF capacitor across 5V & GND`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | ` Adapter (stepped down using LM2596 buck converter)` |
| Voltage required | `5V for servos and NeoPixels, 3.3V for ESP32 and OLED` |
| Current concerns | `Servos and LEDs draw high current; insufficient supply can cause resets, flickering, or unstable behavior  ` |
| Safety concerns | `Incorrect voltage from the buck converter can damage components; overheating, loose connections, or lack of common ground can cause malfunction or short circuits` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `MicroPython` | `Coding` |
| `Codex, Claude` | `Assistance in coding` |
| `Diode(website)` | `Assistance in checking connections` |


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
`Startup Behavior
Initializes all hardware (OLED, servos, button, IR sensor, buzzer, NeoPixels)
Resets score to 0
Shows “READY?” screen and countdown (3 → 1)
Robot eyes open → game begins
Input Handling
Uses a momentary push button (GPIO 27)
Configured as PULL_UP
Press = LOW signal
Player must press during the shoot window
Sensor Reading
IR sensor (GPIO 33) detects ball
LOW = ball detected
Active only when mouth (basket) is open
Decision Logic
Game loop:
Idle (blinking eyes)
Shoot window (3 sec)
Check button press
No → Miss
Yes → Scoring phase
Check ball detection
No → Miss
Yes → Increase score
If score = 4 → Win
Output Behavior
OLED → text + animated eyes
Servos:
Mouth opens for scoring
Arms move on win
NeoPixels:
Show score progress
Blink on win
Buzzer:
Sounds for countdown, hit, miss, win
Communication Logic
No external communication (no WiFi/Bluetooth)
Internal signals only:
GPIO (button, IR)
PWM (servos, buzzer)
I2C (OLED)
Digital output (NeoPixels)
Reset Behavior
On miss:
Score resets to 0
Game restarts from beginning
On win:
Celebration plays
Then full reset and restart`

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
START

INITIALIZE all hardware:
    setup OLED
    setup servos (mouth, left, right)
    setup button (PULL_UP)
    setup IR sensor
    setup buzzer
    setup NeoPixels

SET score = 0

FUNCTION reset_game:
    set score = 0
    reset servos to default positions
    turn off LEDs

FUNCTION start_sequence:
    display "READY?"
    wait
    FOR countdown = 3 to 1:
        display countdown
        play beep
        wait
    show open eyes

MAIN LOOP:

    CALL reset_game
    CALL start_sequence

    WHILE True:

        // IDLE PHASE
        animate blinking eyes

        // SHOOT WINDOW
        display "SHOOT!"
        play sound
        start timer (3 seconds)

        SET button_pressed = False

        WHILE time not over:
            IF button is pressed:
                button_pressed = True
                BREAK

        IF button_pressed == False:
            // MISS
            show sad eyes
            display "MISS!"
            play fail sound
            CALL reset_game
            CALL start_sequence
            CONTINUE loop

        // SCORING PHASE
        open mouth servo
        start timer (based on score level)

        SET ball_detected = False

        WHILE time not over:
            IF IR sensor detects ball:
                ball_detected = True
                BREAK

        close mouth servo

        IF ball_detected == False:
            // MISS
            show sad eyes
            display "MISS!"
            play fail sound
            CALL reset_game
            CALL start_sequence
            CONTINUE loop

        // SCORE SUCCESS
        increment score
        show "HIT!"
        update LEDs
        play score sound

        IF score == MAX_SCORE:
            // WIN CONDITION
            display "YOU WIN!"
            play win sounds
            run celebration (LEDs + servos + eyes)
            CALL reset_game
            CALL start_sequence
        ENDIF

    END WHILE

END
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [ 1] No

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
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `-` | `[Reason]` |
| `ESP32` | `1` | `No` | `Yes` | `560` | `-` | `First esp32 excess heating` |
| `LM2596 buck converter` | `1` | `No` | `Yes` | `75` | `-` | `Power supply module insuffecient` |
| `OLED screen` | `2` | `No` | `Yes` | `230+350=580` | `-` | `Digital display` |
| `Servo` | `3` | `Yes` | `No` | `0` | `-` | `Movement` |
| `Buzzer` | `1` | `Yes` | `No` | `0` | `-` | `Sound` |
| `Neopixel strip` | `1` | `Yes` | `No` | `0` | `-` | `Light` |
| `IR Sensor` | `1` | `Yes` | `No` | `0` | `-` | `Sensing objects` |
| `On/off button` | `1` | `No` | `Yes` | `20` | `-` | `Larger surface area` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`*Cardboard (main body)*
We used cardboard because it’s lightweight, easy to cut and modify, and allows rapid prototyping. It lets us quickly adjust form, fit components, and experiment with structure without committing to permanent materials, while also giving the robot a playful, approachable aesthetic.

*Cans (hands and legs)*
We used cans because they provide a rigid, ready-made cylindrical form that is structurally stable and visually distinct. They add contrast to the soft cardboard body and give the robot a slightly mechanical, assembled-from-found-objects character.

*Magnifying glass (for OLED)*
We used a magnifying glass to enlarge the small OLED display, making expressions and text more visible from a distance. It also adds an unusual, interactive visual layer, turning a limitation (small screen) into a distinctive feature of the experience.
`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `OLED screen` | `Digital display` | `Went to shop` | `4/4/26` | `Received` |
| `LM2596 buck conveter` | `Power supply incapable` | `Nimesh Electronics` | `10/4/26` | `Received` |
| `Push button` | `Larger surface area` | `Nimesh Electronics` | `10/4/26` | `Received` |
| `ESP32` | `Older one stopped working` | `https://www.amazon.in/ESP32-38-Pin-Development-Board-Microcontroller/dp/B0GCLD44M7/ref=sr_1_1_sspa?crid=B1J2YB6OKUDL&dib=eyJ2IjoiMSJ9.1beEuNKPoLJTA-Ge2z6x6ycM9O0z-GCdHZRTudwfTngomSj-C6DMR3z-sX6lVHYPfSgmE1y-i5mmsjeqko_SO8VCO9xlC7LV8im5sQWVnmJHJsV21-sJ00SRwMh4IxMM4Qg-218We4weyUN_17JOscwMiQ2495FHww2lC9u-R4jEnXXTHBNA_Mm94_I9p1FXwu_7bhRqCG6Tp5NrEaOm44frkIg8URW5Jy2-FxJH4BI.KJxmFYIU57rj7a3ctvOAgQNu5ALs9yskPxfwd-E_muI&dib_tag=se&keywords=esp+32&qid=1776620291&sprefix=esp%2Caps%2C419&sr=8-1-spons&aref=Papmiqtu6X&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1` | `7/4/26` | `Received` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `1339` |
| Mechanical parts | `0` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `1339` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`-`

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
`Tasks are divided basied on the skill of the teammate. Decisions on EVERY issue is made collectively, with discussion. Progress will be checked by timely reports and results. If any task is delayed, there will be constrcutive follow up and efforts to complete it on time. Documentation will be mainatined through notes and photographs. `

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `Finalize concept` | `Narayani Sharannya` | `2` | `4/4/26` | `None` | `Done` |
| T2 | `Complete BOM` | `Sharannya` | `1` | `9/4/26` | `T1` | `Done` |
| T3 | `Test electronics` | `Narayani` | `2` | `7/4/26` | `T1` | `Done` |
| T4 | `[Build structure]` | `Narayani Sharannya` | `4` | `10/4/26` | `T1` | `Done` |
| T5 | `[Write control code]` | `Sharannya Narayani` | `4` | `12/4/26` | `T3` | `Done` |
| T6 | `[Integrate system]` | `Narayani Sharannya` | `4` | `15/4/26` | `T4, T5` | `Done` |
| T7 | `[Playtest]` | `Sharannya+Narayni` | `2` | `17/4/26` | `T6` | `Done` |
| T8 | `[Refine and document]` | `Narayani Sharannya` | `3` | `19/4/26` | `T7` | `Done` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `Narayani Sharannya` | `-` |
| Electronics | `Narayani` | `Sharannya` |
| Coding | `Sharannya Narayani` | `-` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `Sharannya` | `-` |
| Testing | `Narayani Sharannya` | `-` |
| Documentation | `SHarannya Narayani` | `-` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [1 ] Idea finalized
- [ 1] Core interaction decided
- [ 1] Sketches made
- [ ] BOM completed
- [1] Purchase needs identified
- [ 1] Key uncertainty identified
- [ 1] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [1 ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [1 ] Mechanical concept tested
- [1 ] Main subsystems partially working
- [1 ] BOM completed

### Week 3 — Integrate
Expected outcomes:
- [ 1] Physical body built
- [ 1] Electronics integrated
- [1 ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ 1] Technical bugs reduced
- [ 1] Playtesting completed
- [ 1] Improvements made
- [ 1] Documentation completed
- [1 ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `Finalise idea` | `Idea finalised and discussed with faculty` | `Iterations made in the idea` | `Procure materail, ideate forms, make sketches, code` |
| Week 2 | `Make prototype, test components individually` | `done` | `changed power supply` | `start making the model` |
| Week 3 | `build model, add mechanisms and electronics` | `done` | `form of the robot` | `test main code + game` |
| Week 4 | `fit components + playtest ` | `done` | `minor angle changes` | `-` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `Servo not moving` | `Technical` | `High` | `High` | `check connections; replace motor` | `-` |
| `Two Oleds not working` | `Technical` | `High` | `High` | `Use of one oled instead of two` | `-` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`Buck converter not working or esp32 ffrying up`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `Servos` | `Running through test codes` | `Servo movement based on main code` |
| `Oled` | `Wiring and main code` | `Display visible on main code` |
| `Sensor` | `Detecting various objects with various range` | `All objecgts detected` |


## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `After explanation, game is easy` |
| Is the interaction satisfying? | `Yes` |
| Do players want another turn? | `Yes` |
| Is the challenge balanced? | `Yes` |
| Is the response clear and immediate? | `Yes` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `9/4/26` | `Power Supply module died` | `Technical` | `Tested servos with another pwoer supply` | `worked` | `got new power supply` |
| `13/4/26` | `Two oleds stopped working when connected togther` | `Technical` | `Made use of one oled with magnifying glass for better visibilty` | `worked` | `Make changes in the code for one oled` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `classmate` | `enjoyed` | `the timing of the flap opening` | `the sensory feedback and the aeshetic of the model` | `-` |
| `friend` | `curious` | `the button` | `the scoreing system and the restarting of the game` | `-` |

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
`We started with estimate measurements. Then we used cardboard to make the head of the robot. then we made the body of the robot, followed by the base; legs and arms, made of cans. flaps were made at the back of the body and the head to insert wiring and breadbard and also for easy access in case of changes. a sqaure was cut out on the body for dunking the balls and a much smaller square on the face to fix the oled. all the connection were made once the breadbaord was fixed insided the body at the bottom. a servo was fixed near the dunking opening for a flap to cover it. a base was added on top of the breadboard and the wores to hide it and also to catch the balls. a magnifying glass was added infront of the oled on the face for better visibilty.`

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
`The project is a compact, character-like robot built from cardboard and soda cans, designed as an interactive dunk based game. It has a boxy blue and silver body(covered with aluminium foil)with a front facing flap at the chest, which opens and closes to create a timed scoring window. The head features a circular magnified display, giving it a single expressive “eye,” while the body integrates hidden electronics and sensors that control the gameplay. The use of foil textures, bold colors, and simple geometric forms gives it a playful, handmade aesthetic that still feels intentional.

Functionally, the robot combines physical interaction with reactive behavior. The player presses a button to trigger the mouth mechanism, attempts to dunk the ball within a short time window, and the system detects success using an internal sensor. The robot responds through movement, light, and sound, creating a loop of anticipation, action, and feedback. Structurally, all components are balanced into one stable form, where the mechanical, electronic, and visual elements work together as a single interactive object rather than separate parts  glued together.`

## 18.2 What Works Well
- `The mechanism`
- `Feedback`
- `The display`

## 18.3 What Still Needs Improvement
- `fans at the back of the robot`
- `sensor detection`
- `ensuring the wiring is securelt fixed`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`the flap was supposed to be at the robots mouth ended up being at the robots chest, and the use of one oled screen instead of two.`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`Collaboration, coding, model making.
Components not working together, code to be edited, procurement of material, securing main components to the model
Division of task, helping each other, showing up.`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`We learned how to manage multiple electronic components together, especially handling power distribution and ensuring stable connections. In coding, we developed a state-based system to control timing, inputs, and outputs reliably. Mechanically, we understood how servo movement, alignment, and timing affect user interaction. Through fabrication, we explored how simple materials like cardboard can be used to build stable, functional structures. Most importantly, integration taught us how to combine electronics, code, and form into a single system where everything works together without conflict.`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`We learned that designing for play requires simplicity, clear goals, and immediate feedback. Small elements like sound, movement, and visual cues significantly enhance delight. Clarity in interaction is crucial, players should instantly understand what to do without instructions. Physical interaction adds engagement but also introduces challenges in timing and coordination. Iteration was key, as repeated testing helped refine responsiveness, usability, and overall player experience.`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`We would improve sensor accuracy and timing to make interactions more reliable, refine the mechanical structure for smoother movement, and enhance visual feedback for clearer communication. Additionally, we would polish the overall build quality and explore adding more dynamic behaviors to increase engagement.`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ 1] Team details are complete
- [1 ] Project description is complete
- [ 1] Inspiration sources are included
- [1 ] Player journey is written
- [ 1] Sketches are added
- [1 ] BOM is complete
- [1 ] Purchase list is complete
- [1 ] Budget summary is complete
- [1 ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [1 ] Code flowchart is added
- [1 ] Task breakdown is complete
- [ 1] Weekly logs are updated
- [1 ] Risk register is complete
- [1 ] Testing log is updated
- [1 ] Playtesting notes are included
- [1 ] Build photos are included
- [1 ] Final reflection is written

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
