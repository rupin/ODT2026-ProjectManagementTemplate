from machine import Pin, PWM
from neopixel import NeoPixel
import time

# -------------------------------------------------------
# PINS
# -------------------------------------------------------
ir_sensor    = Pin(34, Pin.IN)
neopixel_pin = Pin(2, Pin.OUT)
pixels       = 16
np           = NeoPixel(neopixel_pin, pixels)

SERVO_PIN = 5

# -------------------------------------------------------
# SERVO HELPER — moves then kills PWM to stop vibration
# -------------------------------------------------------
def servo_move(angle, settle_ms=400):
    pwm = PWM(Pin(SERVO_PIN), freq=50)
    min_us = 500
    max_us = 2500
    us     = min_us + (max_us - min_us) * angle // 180
    duty   = int(us * 65535 // 20000)
    pwm.duty_u16(duty)
    time.sleep_ms(settle_ms)
    pwm.deinit()

# -------------------------------------------------------
# NEOPIXEL FUNCTIONS
# -------------------------------------------------------
def neopixel_off():
    np.fill((0, 0, 0))
    np.write()

def pink_loading(duration_ms):
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < duration_ms:
        np.fill((0, 0, 0))
        for i in range(pixels):
            np[i] = (255, 20, 147)
            np.write()
            time.sleep_ms(50)
            np[i] = (0, 0, 0)
            np.write()
        time.sleep_ms(20)

def green_dispensing():
    np.fill((0, 255, 0))
    np.write()

# -------------------------------------------------------
# COIN DETECTION
# -------------------------------------------------------
def coin_detected():
    if ir_sensor.value() == 0:
        time.sleep_ms(50)
        if ir_sensor.value() == 0:
            return True
    return False

# -------------------------------------------------------
# DISPENSE — servo flap 0° → 90° → 0°
# -------------------------------------------------------
def open_flap():
    green_dispensing()
    servo_move(0,  settle_ms=300)
    servo_move(90, settle_ms=800)
    servo_move(0,  settle_ms=500)

# -------------------------------------------------------
# STARTUP
# -------------------------------------------------------
servo_move(0, settle_ms=500)
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
        open_flap()
        neopixel_off()
        print("Done. Ready for next coin.")
        time.sleep_ms(1000)
    time.sleep_ms(50)