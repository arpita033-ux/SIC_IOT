from flask import Flask, redirect
import RPi.GPIO as GPIO

app = Flask(__name__)

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

LED1 = 17   # Physical Pin 11
LED2 = 27   # Physical Pin 13

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

# Start LEDs OFF
GPIO.output(LED1, False)
GPIO.output(LED2, False)

@app.route('/')
def home():

    led1_state = GPIO.input(LED1)
    led2_state = GPIO.input(LED2)

    led1_color = "lime" if led1_state else "red"
    led2_color = "lime" if led2_state else "red"

    led1_text = "ON" if led1_state else "OFF"
    led2_text = "ON" if led2_state else "OFF"

    return f'''
    <html>
    <head>
        <title>Two LED Control</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #1f4037, #99f2c8);
                text-align: center;
                padding-top: 80px;
                color: white;
            }}

            h1 {{
                margin-bottom: 40px;
            }}

            .card {{
                background: rgba(255,255,255,0.15);
                padding: 30px;
                margin: 20px auto;
                width: 320px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            }}

            .status {{
                height: 20px;
                width: 20px;
                border-radius: 50%;
                display: inline-block;
                margin-left: 10px;
            }}

            button {{
                padding: 10px 20px;
                margin: 10px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }}

            .on {{
                background-color: #4CAF50;
                color: white;
            }}

            .off {{
                background-color: #f44336;
                color: white;
            }}

            button:hover {{
                opacity: 0.8;
            }}
        </style>
    </head>

    <body>
        <h1>Two LED Control Panel</h1>

        <div class="card">
            <h2>LED 1 
                <span class="status" style="background:{led1_color};"></span>
            </h2>
            <p>Status: {led1_text}</p>
            <a href="/led1/on"><button class="on">ON</button></a>
            <a href="/led1/off"><button class="off">OFF</button></a>
        </div>

        <div class="card">
            <h2>LED 2 
                <span class="status" style="background:{led2_color};"></span>
            </h2>
            <p>Status: {led2_text}</p>
            <a href="/led2/on"><button class="on">ON</button></a>
            <a href="/led2/off"><button class="off">OFF</button></a>
        </div>

    </body>
    </html>
    '''


@app.route('/led1/on')
def led1_on():
    GPIO.output(LED1, True)
    return redirect('/')

@app.route('/led1/off')
def led1_off():
    GPIO.output(LED1, False)
    return redirect('/')

@app.route('/led2/on')
def led2_on():
    GPIO.output(LED2, True)
    return redirect('/')

@app.route('/led2/off')
def led2_off():
    GPIO.output(LED2, False)
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
