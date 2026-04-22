# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 4 students  
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
`Anda Fundas`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Vibhor` | `[Electronics / Coding / Fabrication / Mechanics]` | `[Conveyor Belt{coding, mechanics, building and assembly}, repo updation till 4.4, ODT parts' sketches]` | `[Write here]` |
| `Ranya` | `[Electronics / Coding / Fabrication / Mechanics]` | `[Cracking egg mechanism (servo coding, building, assembling); planning and execution of physical structure and props]` | `[Write here]` |
| `Anusha` | `[Electronics / Coding / Fabrication / Mechanics]` | `[Role]` | `[Write here]` |
| `Avani` | `[Electronics / Coding / App / Fabrication / Mechanics]` | `[Complete functioning of app, connection to Thonny code, building and finalising of structure & aesthetics]` | `[Write here]` |


## 1.3 Project Title
`Hen's Kitchen`

## 1.4 One-Line Pitch
A fast-paced, interactive cooking game where players crack, catch, cook, and plate a slime egg using physical controls, sensors, and timing-based challenges.

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
This project is a physical-digital hybrid cooking game inspired by high-pressure kitchen environments and playful cooking simulators. The setup consists of two stacked shelves forming a multi-stage gameplay system. In the first stage, a servo-driven plastic egg cracks open on button press, releasing slime that represents the yolk. The player must time their input precisely to catch the falling “yolk” in a bowl that continuously moves back and forth on a conveyor belt. If successful, the bowl tips at the edge, transferring the slime into a pan on the lower level. The second stage shifts from timing to spatial control: the player must hold the pan at varying heights over a NeoPixel “stove,” guided by changing light colors and measured using an ultrasonic sensor. The system evaluates how accurately and quickly the player responds to these dynamic cues.
The experience is designed to feel tense, playful, and slightly chaotic; mirroring the pressure of real-time cooking while exaggerating it through tactile and unexpected interactions (like slime as yolk). It combines anticipation (timing the egg crack), unpredictability (moving bowl and randomized heat cues), and satisfaction (successfully completing each stage). The final outcome—ranging from undercooked to perfectly cooked to disintegrated—is determined by performance metrics such as timing and accuracy, reinforcing a sense of challenge and replayability. Technologies involved include servo motors, conveyor mechanisms, ultrasonic distance sensing, NeoPixel LEDs for feedback, and a mobile interface built with MIT App Inventor for final interaction and seasoning, blending physical computing with digital feedback into a cohesive, game-like system.

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
What is the experience?
The project creates a fast-paced, multi-stage interactive cooking game that blends physical actions with digital feedback. Players move through a sequence of challenges such as timing the cracking of an egg, coordinating with a moving target, and then controlling distance and positioning based on real-time visual cues. It feels like a condensed, exaggerated version of a high-pressure cooking show translated into a hands-on, playful system.

What do you want the player or participant to feel?
The experience is designed to make players feel anticipation, focus, and slight tension as they react to moving elements and changing cues. Instead of explicit time pressure, the uncertainty of not knowing how well they are performing adds to the engagement. There is also a sense of unpredictability and controlled chaos due to the moving conveyor and randomized heat instructions. When successful, it should feel satisfying and rewarding. The use of slime and exaggerated mechanics adds humor and lightness, keeping the experience playful rather than stressful.

Why would someone want to try it again?
The game encourages replayability through variability and delayed feedback. Since players only discover the final result at the end, there is curiosity about how their actions translated into outcomes. The moving elements and randomized instructions ensure each attempt feels different. Players are motivated to improve their results from undercooked or disintegrated to perfectly cooked, creating a natural progression and challenge. The tactile interaction and slightly messy, unexpected nature of the slime also make it enjoyable to repeat and watch others play.

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
We are designing this project as if we are a small creative studio making a playable interactive experience for classmates and exhibition visitors.

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Papa's Pizzeria]` | `https://papaspizzeria.io/` | `Borrowed the concept of a cooking game with different stages for each process` |
| `Purble Place]` | `https://purbleplace-online.com/` | `Borrowed the concept of a cooking game with different stages for each process` |
| `[Toy / Board game / App / Video / Website / Object]` | `[Link or title]` | `[What did you learn or borrow?]` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`What makes Hen’s Kitchen original is that it blends a real physical cooking process with the structure of a multi-level digital game, so it feels like a real-life version of a cooking simulator. Instead of the player only tapping on a screen, the gameplay depends on actual motion, gravity, timing, and interaction. Cracking a real egg, watching it fall through different stages, and physically catching it in the right place.

The project is also unique because each stage focuses on timing-based precision (dropping the egg into the moving bowl), hand-eye coordination (catching it in the pan), reflex-based decision making (reacting to changing Neopixel flame colours), and creativity/personalization (adding toppings through the MIT app). This mix makes it feel like a complete cooking process.

Most importantly, the identity of the game (the hen mascot, the vertical wooden structure, and the real egg interaction) makes it playful and memorable. It stands out from typical cooking games because it combines physical gameplay with digital scoring, making the whole experience more interactive and engaging.`

---

# 4. Project IntentS

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
press button → egg cracks → attempt to catch yolk in moving bowl → bowl tips into pan → adjust pan height based on light cues → sensor validates position → repeat adjustments → final result revealed → reset and play again


## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Classmates and exhibition visitors who are interested in playful, interactive installations]` |
| Age range | `13–25` |
| Solo or multiplayer | `Solo` |
| Expected duration of one round | `1–2.5 minutes` |
| What should the player feel? | `Anticipation, focus, curiosity, and satisfaction, along with light humor from the messy and unpredictable interactions` |
| Is explanation required before use? | `Yes, a short initial explanation is needed for controls and stages` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `The player walks up to the Hen’s Kitchen setup and sees the vertical wooden structure with the hen at the top, the bowl system in the middle, and the stove/pan stage below. They also notice the button controls and the MIT app interface.`
2. **Start:** `The player is instructed to begin and the system activates the moving bowl mechanism. The game begins once the bowl starts sliding back and forth via the conveyor belt under the egg drop point.`
3. **First Action:** `The player’s first task is to time the egg crack. They press the switch labelled "Crack Egg!" to trigger the servo motor mechanism so the eggshells open and drop the egg at the exact moment the bowl is positioned underneath.`
4. **Main Interaction:** `The player continues through the stages in order:
-They try to successfully drop the egg into the moving bowl.
-Once the egg lands, the bowl automatically moves, rotates and drops the egg down.
-The player must catch the egg using the pan placed underneath.
-Then they move into the stove stage where the Neopixel flame changes colours and they must react quickly to avoid over/undercooking.
-Finally, they use the MIT app to draw toppings onto the egg image.`
5. **System Response:** `The system responds in real time by moving the bowl, triggering the rotation once the egg hits the switch, lighting up the Neopixel stove in different flame colours, and tracking the player’s reaction speed and accuracy.`
6. **Win / Lose / End Condition:** `The first stage ends once the egg successfully falls into the bowl (by triggering a switch inside the bowl). The second round ends once the egg falls into the pan, upon which the third round begins (the neopixel starts lighting up). The neopixel lights up green to indicate the ending og the neopixel round. The player then moves to the topping stage in the MIT app. The game ends after the topping stage is completed.`
7. **Reset:** `The system resets by returning the bowl to its starting position, turning off the Neopixel stove, and preparing the egg drop mechanism again. The next player can then start a new round.`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `The player must crack the egg only when the moving bowl is directly under the egg opening.`
- `The egg must land inside the bowl to proceed to the next stage. If the egg misses the bowl, the game ends.`
- `Once the egg lands, the bowl will automatically move, rotate and drop the egg`
- `The player must place the pan correctly under the bowl to catch the egg. If the egg falls outside the pan, the game ends.`
- `The player must place the pan correctly under the bowl to catch the egg. If the egg falls outside the pan, the game ends.`
- `During the stove stage, the Neopixel flame changes colours randomly. The player must react quickly to the colour changes to gain points.`
- `The faster the player reacts to the colour change, the higher their score. Delayed reaction reduces points.`
- `If the player reacts too late or misses the colour changes, the egg is given a rating of overcooked/undercooked/burnt based on the time and points are deducted.`
- `In the toppings stage, the player must draw toppings using the MIT app.`
- `The game successfully ends once the toppings stage is completed and the final score is displayed.`

---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `Servos successfully release egg yolk slime on button press.`
- [ ] `Conveyor belt tips over the egg into the pan`
- [ ] `Neopixel changes to color red, asking the player to move the pan closer to the flame`
- [ ] `Neopixel changes to color orange, asking the player to move the pan a bit higher from the flame`
- [ ] `Neopixel changes to color blue, asking the player to move the pan vertically away from the flame`
- [ ] `MIT App Inventor opens the egg image and allows player to draw on it.`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`The minimum viable version of Hen’s Kitchen would include the core physical gameplay of timing and reaction. This would mean having the moving bowl stage where the player must correctly time the egg drop using a button. After that, the egg would drop into a pan and the Neopixel stove stage would run, where the player reacts to flame colour changes for points. Minimally, it should deliver a fun, interactive experience even without mechanisms, extra visual effects or toppings.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Visually appealing structure, interface, extra animations/sound effects like hen noises, sizzling sounds, and music`
- `A leaderboard system to compare scores between players`
- `Difficulty modes (easy/medium/hard) with faster bowl movement and quicker flame changes`

---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [x] Electronics-based
- [x] Mechanical
- [x] Sensor-based
- [x] App-connected
- [x] Motorized
- [ ] Sound-based
- [x] Light-based
- [x] Screen/UI-based
- [x] Fabricated structure
- [x] Game logic based
- [ ] Installation / tabletop experience
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
The system is built around an ESP32 that connects multiple inputs, outputs, and mechanical components to create a multi-stage interactive game. The main input begins with a button press that triggers servo motors to crack open a plastic egg. Additional input comes from an ultrasonic sensor that detects the height of the pan during the cooking stage. The player also interacts through a mobile interface built using MIT App Inventor for the final seasoning step.

The ESP32 processes these inputs by controlling timing, coordinating motor movements, and comparing sensor data against predefined conditions. Based on this, it activates outputs such as servo motion for the egg, a motorized conveyor belt for bowl movement, and NeoPixel LEDs that provide real-time visual instructions through color changes.

The physical structure consists of two stacked shelves. The top layer handles the egg cracking and catching mechanism, while the bottom layer handles the cooking simulation using the pan, sensor, and lighting system. The mobile app acts as a final interaction layer where players complete the experience. Together, these components create a continuous loop of physical action, sensing, and responsive feedback.

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Switch` | Input | `Player presses it to trigger the egg cracking/drop mechanism at the correct time.` |
| `Switch` | Input | `Detects when the egg lands in the bowl and triggers the next stage automatically.` |
| `Ultrasonic Sensor` | Input | `Detects the distance of the pan from the Neopixel to measure reaction time` |
| `MIT App` | Input | `Player draws/adds toppings digitally on the egg image as the final customization stage.` |
| `ESP32` | Processing | `Controls the full sequence of stages, reads button/switch inputs, and calculates scoring.` |
| `Servo (x2)` | Output | `Activates the egg cracking action when the player presses the button.` |
| `DC Motor` | Output | `Moves the bowl left and right continuously to create a timing challenge.` |
| `Neopixel Ring` | Output | `Displays changing flame colours to simulate cooking and create the reaction challenge.` |
| `App Screen` | Output | `Shows image, player's toppings and final grading` |
| `Wooden Vertical Structure` | Physical Action | `Guides the egg through gravity-based falling stages from top to bottom.` |
| `Conveyor Belt` | Physical Action | `Allows the bowl to move back and forth to catch the egg, then moves the bowl to rotate and drop the egg into the pan` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

**Insert image below:**  
`[Upload image and link here]`

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
| Length | `[7.5 inches]` |
| Width | `[24.5 inches]` |
| Height | `[28 inches]` |
| Estimated weight | `[4.5 kgs]` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [x] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [ ] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`Button press opens servos → egg drops`
`Bowl moves side-to-side on conveyor belt`
`Egg lands in bowl → switch gets pressed`
`Switch triggers bowl to move forward + tip over`
`Egg falls out → player catches using pan`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`What moves:`
`Egg servos`
`Conveyor belt bowl`
`Bowl tipping mechanism`

`What causes movement:`
`Button triggers egg drop`
`Motor moves conveyor`
`Switch triggers tipping`

`How far it moves:`
`Bowl moves across belt length`
`Servos rotate ~90°`
`Bowl tips over`

`How fast it moves:`
`Bowl moves constant speed`
`Tip action is quick`
`Servos crack egg in a quick action`

`What could go wrong:`
`Egg misses bowl`
`Egg doesn’t press switch`
`Belt gets stuck`
`Egg misses pan`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[N/A]` | `[N/A]` | `[N/A]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`[N/A]`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `[Main controller]` |
| `[Servo Motors]` | `[2]` | `[Egg cracking]` |
| `[DC motor + Motor driver]` | `[2]` | `[Conveyor belt movement]` |
| `[Neopixel ring]` | `[1]` | `[Stove flame colour changing]` |
| `[Ultrasonic sensor]` | `[1]` | `[Detect pan distance from stove]` |
| `[Limit switch]` | `[2]` | `[Triggers egg cracking and triggers bowl tipping once egg lands in the bowl]` |
| `[External power supply]` | `[2]` | `[Powers all input and output components]` |

## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**
`ESP32 controls all components.`
`2 breadboards with 2 external power supplies connected to 1 ESP32.`
`1 power supply reserved to run the DC motor due to voltage requirement`  
`DC motor connected to motor driver which connects to ESP32 pins for control`  
`Limit switches connected to ESP32 input pin and GND`  
`Servo motors connected to ESP32 PWM pins and external power supply GND and 5V`  
`Neopixel connected to ESP32 pin and GND and 3V3`  
`Ultrasonic sensor trig and echo connected to ESP32 pins`  
`GND to GND between ESP32 and power supplies & between the 2 breadboards`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `[adapter]` |
| Voltage required | `[5V for servos, 6-12V for DC motor]` |
| Current concerns | `[require 2 power supplies as DC motor voltage requirement is already large]` |
| Safety concerns | `[accidental GND to voltage connection, connection to VIN, fusing of esp32 and power supplies]` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython & Thonny IDE]` | `[Programming motors and servos, writing & sending code to ESP32]` |
| `[MIT App Inventor]` | `[Creating toppings interface and displaying the egg player has cooked with rating]` |

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
`startup behavior:`
`esp32 powers on`
`wifi hotspot starts (hen’s kitchen)`
`servos set to default positions`
`motor driver, neopixel, ultrasonic sensor initialized`

`input handling:`
`switch press triggers egg cracking servos`
`bowl switch press triggers stop + tipping of bowl`

`sensor reading:`
`ultrasonic sensor keeps reading pan distance during cooking stage`

`decision logic:`
`if button pressed → open servos → drop egg → reset servos`
`if switch pressed → stop conveyor → delay → rotate bowl`
`if ultrasonic reads correct distance in minimal reaction time → gain points`
`if ultrasonic reads incorrect distance or slow reaction time → lose points`

`output behavior:`
`servos rotate to crack egg and reset`
`motor moves bowl left-right and then tips it`
`neopixel flames flash in different colours`
`reaction time recorded and printed for each colour change`
`final score calculated + printed`

`communication logic:`
`app sends request to esp32`
`esp32 replies with final score through wifi`

`reset behavior:`
`atored score stays available for MIT app to call`
`neopixel turns off`
`servos return to default position`

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
[INITIALIZE servo1 on pin 18
INITIALIZE servo2 on pin 5
INITIALIZE button on pin 15 (pull-up)

DEFINE function angle_to_duty(angle):
    CONVERT angle (0–180) → PWM duty

DEFINE function set_angle_servo1(angle):
    APPLY duty to servo1

DEFINE function set_angle_servo2(angle):
    APPLY duty to servo2

SET initial positions:
    servo1 → 180°
    servo2 → 0°

SET servo_active = FALSE
SET servo_timer = 0

LOOP:
    IF button is pressed AND servo not active:
        MOVE both servos to 90°
        SET servo_active = TRUE
        RECORD current time

    IF servo_active:
        AFTER 1.2 seconds:
            RESET servos to initial positions

        AFTER 2.5 seconds:
            SET servo_active = FALSE
            
            INITIALIZE motor pins IN1, IN2, ENA
SET PWM frequency

INITIALIZE stop switch (pull-up)

DEFINE:
    forward() → motor rotates forward
    backward() → motor rotates backward
    stop_motor() → motor stops

SET motor_state = "forward"
SET motor_timer = current time

SET stop_mode = FALSE
SET delay_done = FALSE

SET rotation_time = 20 seconds
SET rotations_done = 0
SET rotation_direction = "cw"

LOOP:
    IF stop switch is pressed AND stop_mode is FALSE:
        ENABLE stop_mode
        RECORD delay_start time

    IF stop_mode:
        IF delay not completed:
            STOP motor
            WAIT 3 seconds
            SET delay_done = TRUE
            SET rotation_direction = "ccw"
            RESET timers

        IF rotation_direction == "cw":
            RUN motor forward
            AFTER rotation_time:
                INCREMENT rotations_done

            IF rotations_done ≥ 1:
                SWITCH to "ccw"

        ELSE IF rotation_direction == "ccw":
            RUN motor backward
            AFTER rotation_time:
                INCREMENT rotations_done

            IF rotations_done ≥ 1:
                STOP motor
                EXIT loop (move to next phase)

LOOP:
    IF motor_state == "forward":
        RUN forward
        AFTER 7 seconds:
            SWITCH to "backward"

    ELSE IF motor_state == "backward":
        RUN backward
        AFTER 9 seconds:
            SWITCH to "forward"

INITIALIZE 16 NeoPixels

DEFINE colors:
    RED, ORANGE, BLUE, GREEN, OFF

DEFINE function set_all(color):
    SET all LEDs to color

DEFINE function pulse_color(color, time):
    CREATE wave using sine function
    ADJUST brightness dynamically
    APPLY gradient across LEDs


INITIALIZE trig and echo pins

DEFINE function measure_distance:
    SEND ultrasonic pulse
    MEASURE echo duration
    CONVERT to distance (cm)
    RETURN distance



DEFINE function interpolate(color1, color2, factor):
    RETURN blended color

DEFINE function get_blended_color(distance):
    IF distance 0–7:
        RETURN blend RED → ORANGE

    IF distance 7–14:
        RETURN blend ORANGE → BLUE

    IF distance 14–21:
        RETURN BLUE

    ELSE:
        RETURN NONE


SET total_score = 0

PRINT "Game Starting"
WAIT 2 seconds

FOR each round (1 to 10):
    SELECT random target color

    RECORD start time
    SET scored = FALSE

    WHILE 1.5 seconds not passed:
        DISPLAY pulsing target color

        MEASURE distance
        CONVERT distance → current color

        IF current color matches target AND not scored:
            CALCULATE reaction time
            CALCULATE score
            ADD to total_score
            PRINT result
            SET scored = TRUE

    IF not scored:
        PRINT "Missed"

    WAIT 0.4 seconds
    TURN OFF LEDs
]
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [x] Yes
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
`personalization: allows topping customization via brush tools, brush size changer, undo button, `
`displays data: lets the player see how well they cooked the egg visually by showing a burnt egg, runny egg, etc and their corresponding rating`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[wifi connect]` | `[connects device to esp32 via network]` |
| `[score request]` | `[fetches the final score from the esp32]` |
| `[egg photo screen]` | `[lets the player see the egg they cooked based on score (burnt, runny, etc)]` |
| `[egg reference]` | `[randomized egg images for players to use as a reference when drawing toppings, saves their topping drawing]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `Player taps “Get Result” button to get their result from the Ultrasonic/Neopixel game.`
2. `⁠Final score and egg state from the game prints on the screen on the label.`
3. `⁠The final score shows respective image of the state of the egg.`
4. `If score ≤ 20, egg is burnt; ≤ 40, egg is undercooked; ≤ 60, egg is overcooked else, egg is perfectly cooked.`
5. `⁠Player chooses colour to draw with and draws on the canvas with the image; colours can be changed as and when they want.`
6. `Colour preview shows which colour brush is chosen.`
7. `⁠Player can choose brush size on the slider.`
8. `⁠If any mistake, player can undo their stroke.`
9. `Player can toggle on and off the eraser button to erase a stroke.`
10. `⁠Clear canvas cleans the canvas of any strokes completely.`
11. `Player may or may not enter name (leaves the file name as “Player”).`
12. `After finishing, player taps on “Submit button”.`
13. `⁠Image gets saved as: PlayerName (or Player)_finalScore_eggState_Date (MMDDYYYY)_Time (HHMMSS).png in Downloads.`
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
| Concept and gameplay | `[Avani, Vibhor]` | `[Anusha, Ranya]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Avani, Vibhor, Anusha, Ranya ]` | `[Name]` |
| App | `[Avani]` | `[Anusha]` |
| Mechanical build | `[Ranya, Vibhor]` | `[Avani, Anus]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
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
| Week 1 | `[Idea finalized, Core interaction decided, Sketches made ` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[BOM completed, Purchase needs identified, Key uncertainty identified, Basic feasibility tested]` | `[Write here]` | `[Write here]` | `[Write here]` |
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
```
<img src="images/initial-brainstorming-sketches.jpeg" width="400">
<img src="images/initial-rough-sketch.jpeg" width="400">
<img src="initial-whiteboard-sketch.jpeg" width="400">



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
`[Team worked well in task distribution, everyone was an equal asset and ]`

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
`[-Find a better way to create a mock egg yolk to look more convinving but also have enough weight to initiate the conveyor belt stop switch in the bowl.
-Make the conveyor belt more smooth
-Improve bowl stability
-Instead of the reaction time deciding cooking quality, an "order" from a customer could initiate the game and each type of order could have a unique red, orange, blue light configuration]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Player journey is written
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [x] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written

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
