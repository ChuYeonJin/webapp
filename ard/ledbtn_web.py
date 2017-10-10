from bottle import route, run, template
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
leds = [17, 27]
ledStates = [0, 0]
button = 18
GPIO.setup(leds[0], GPIO.OUT)
GPIO.setup(leds[1], GPIO.OUT)
GPIO.setup(button, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def update_leds():
    for i, value in enumerate(ledStates):
        GPIO.output(leds[i], value)

controll_page = """
<script>
function changed(id)
{
    window.location.href='/' + id
}
</script>
<h1> GPIO Control </h1>
<h2> Button
% if btnState:
    =Up
% else:
    =Down
% end
</h2>
<h2> LED </h2>
<input type='button' onClick='changed({{led0}})' value='LED{{led0}}'/>
<input type='button' onClick='changed({{led1}})' value='LED{{led1}}'/>
"""

@route('/')
@route('/<led>')
def index(led = "n"):
    if led != "n" and led != "favicon.ico":
        num = int(led)
        ledStates[num] = not ledStates[num]
        update_leds()
    state = GPIO.input(button)
    return template(controll_page, btnState=state, led0=0, led1=1)

run(host='192.168.0.126', port='8888')
