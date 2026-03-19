# 📡 LED Control using Raspberry Pi


## 📌 About the Project

This LED control project was developed as part of the **Samsung Innovation Campus training program** conducted at our college.

The project demonstrates how a **Raspberry Pi** can be used to control an LED through a **web-based interface**. By connecting hardware with a custom-built website, users can remotely switch the LED **ON** and **OFF** in real time.

It showcases the integration of **IoT, web development, and hardware control** into a single working system.


## 🚀 Features

- 🌐 Control LED via a web browser  
- ⚡ Real-time ON/OFF switching  
- 🔌 GPIO-based hardware control  
- 🧠 Combines frontend + backend + hardware  
- 📡 Basic IoT implementation  


## 🧰 Tech Stack

- **Hardware:** Raspberry Pi, LED, Resistor  
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS  
- **Interface:** Web Browser  
- **GPIO Control:** Raspberry Pi GPIO pins  



## ⚙️ How It Works

1. The LED is connected to the Raspberry Pi GPIO pins  
2. A Flask web server runs on the Raspberry Pi  
3. The website provides buttons to control the LED  

**When a user clicks a button:**
- A request is sent to the server  
- The server triggers GPIO pins  
- The LED turns ON/OFF instantly  


## 🛠️ Setup Instructions

### 1️⃣ Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2️⃣ Install dependencies

pip install flask RPi.GPIO

### 3️⃣ Run the application

python app.py

### 4️⃣ Open in browser

http://<your-raspberry-pi-ip>:5000

### 🔌 Hardware Connections

Connect LED positive leg → GPIO pin

Connect LED negative leg → Resistor → Ground (GND)


### 🎯 Learning Outcomes

Understanding Raspberry Pi GPIO control

Basics of IoT system design

Backend-frontend integration

Real-time hardware interaction via web

### 🙌 Acknowledgement

This project was completed as part of the Samsung Innovation Campus Training Program conducted at our college.

### ⭐ Future Improvements

Add brightness control (PWM)

Mobile-friendly UI

Add authentication (login system)

Control multiple devices
