from machine import Pin
from neopixel import NeoPixel
from servo import Servo
import time
# -------------------------------------------------------
# PINS
# -------------------------------------------------------
ir_sensor = Pin(34, Pin.IN)
in1 = Pin(25, Pin.OUT)
in2 = Pin(18, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(21, Pin.OUT)
servo_pin = Pin(5, Pin.OUT)
flap = Servo(servo_pin)
neopixel_pin = Pin(2, Pin.OUT)
pixels = 16
np = NeoPixel(neopixel_pin, pixels)
# -------------------------------------------------------
# STEPPER
# -------------------------------------------------------
stepPatternCW = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
delay = 3
def stepper_off():
    in1.value(0); in2.value(0)
    in3.value(0); in4.value(0)
# -------------------------------------------------------
# NEOPIXEL FUNCTIONS
# -------------------------------------------------------
def neopixel_off():
    np.fill((0,0,0))
    np.write()
def pink_loading(duration_ms):
    """Chase animation in pink (255,20,147) for duration."""
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        np.fill((0,0,0))
        for i in range(pixels):
            np[i] = (255, 20, 147)
            np.write()
            time.sleep_ms(50)
            np[i] = (0,0,0)
            np.write()
        time.sleep_ms(20)
def green_dispensing():
    """Solid green during dispensing."""
    np.fill((0, 255, 0))
    np.write()
# -------------------------------------------------------
# PHASE 1 -- Coin Detection
# -------------------------------------------------------
def coin_detected():
    if ir_sensor.value() == 0:
        time.sleep_ms(50)
        if ir_sensor.value() == 0:
            return True
    return False
# -------------------------------------------------------
# PHASE 2 -- Stepper Motor (90 degrees = 512 steps)
# -------------------------------------------------------
def dispense_candy():
    green_dispensing()
    for _ in range(128):        # 128 outer loops x 4 steps = 512 steps = 90°
        for step in stepPatternCW:
            in1.value(step[0])
            in2.value(step[1])
            in3.value(step[2])
            in4.value(step[3])
            time.sleep_ms(delay)
    stepper_off()
# -------------------------------------------------------
# PHASE 3 -- Servo Flap
# -------------------------------------------------------
def open_flap():
    flap.write_angle(90)
    time.sleep_ms(800)
    flap.write_angle(0)
    time.sleep_ms(300)
# -------------------------------------------------------
# STARTUP
# -------------------------------------------------------
flap.write_angle(0)
stepper_off()
neopixel_off()
for i in range(2):
    np[0] = (255, 20, 147)
    np.write()
    time.sleep_ms(300)
    neopixel_off()
    np[0] = (0, 255, 0)
    np.write()
    time.sleep_ms(300)
    neopixel_off()
print("Ready. Waiting for coin...")
# -------------------------------------------------------
# MAIN LOOP
# -------------------------------------------------------
while True:
    if coin_detected():
        print("Coin detected!")
        pink_loading(1000)
        dispense_candy()
        open_flap()
        neopixel_off()
        print("Done. Ready for next coin.")
        time.sleep_ms(1000)
    time.sleep_ms(50)

