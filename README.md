# virtual-cursor
A Python-based virtual cursor system that leverages hand tracking to control mouse movements and actions. This project utilizes computer vision techniques to interpret hand gestures, enabling users to interact with their computer without traditional input devices.

## Features

- **Hand Tracking**: Detects and tracks hand movements in real-time using a webcam.
- **Virtual Mouse Control**: Translates hand gestures into mouse movements and click actions.
- **Gesture Recognition**: Identifies specific hand gestures to perform actions like clicking or dragging.
- **Customizable Gestures**: Allows users to define and customize gestures for different actions.
- **Cross-Platform**: Designed to work on multiple operating systems with minimal setup.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Bryium/virtual-cursor.git
   cd virtual-cursor

2. **Create  avirtual environment (optional)
   ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
   source venv/bin/activate
3. **Runnig the project**
   ```bash
    python VirtualMouse.py

4. **Tech Stack**
   - **OpenCV** – for video capture and image processing.
   - **MediaPipe** – for accurate hand landmark detection.
   - **PyAutoGUI** – for simulating mouse movements.
   - **NumPy** – for numerical operations

   **Acknowledgements**
   - **Google’s MediaPipe team for their open-source hand tracking library.
   - **OpenCV and PyAutoGUI for simplifying real-world computer interaction.
   

 


   
   
