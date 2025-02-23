# Maths Using Hand Gesture

## Overview
This project, **Maths Using Hand Gesture**, is an AI-powered system that enables users to draw mathematical problems using hand gestures detected via a webcam. The drawn problem is then processed using Google's Gemini AI model to solve the problem and provide the result.

## Features
- **Hand Gesture Recognition**: Uses OpenCV and cvzone's HandTrackingModule to detect hand gestures.
- **Drawing Using Fingers**: Index finger can be used to draw on a virtual canvas.
- **Clearing the Canvas**: Spreading all five fingers clears the canvas.
- **Sending the Drawing to AI**: Specific gestures trigger the AI model to analyze and solve the drawn mathematical problem.
- **Real-time Interaction**: The system continuously processes the hand movements and updates the canvas dynamically.

## Technologies Used
- Python
- OpenCV
- cvzone
- NumPy
- PIL (Pillow)
- Google Gemini AI

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/mathsusinghandgesture.git
   cd mathsusinghandgesture
   ```
2. Install required dependencies:
   ```sh
   pip install cvzone opencv-python numpy Pillow google-generativeai
   ```
3. Obtain an API key for Google Gemini AI and configure it in the script.
4. Run the program:
   ```sh
   python main.py
   ```

## How It Works
1. **Run the script**: The webcam will open and start detecting your hand.
2. **Draw with index finger**: Keep only the index finger up (gesture `[0,1,0,0,0]`) to start drawing on the virtual canvas.
3. **Clear the canvas**: Spread all fingers (gesture `[1,1,1,1,1]`) to erase everything.
4. **Solve the problem**: Make a specific hand gesture (thumb and pinky up `[1,0,0,0,1]`) to send the drawing to the AI model for solving.
5. **Get the solution**: The AI processes the drawing and provides the mathematical solution in the console.

## Future Improvements
- Improve digit recognition and problem parsing.
- Add GUI-based output for displaying solutions.
- Enhance AI accuracy with preprocessing techniques.
- Develop a standalone application.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

## License
This project is licensed under the MIT License.

## Author
**Uday Gandhi**  
[GitHub](https://github.com/uday-gandhi04)

