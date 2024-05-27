# Time_Tamer

Time_Tamer is a simple yet effective command-line alarm clock written in Python. Set a timer, and it will play an alarm sound once the time is up.

## Features

- Set a custom timer in minutes and seconds.
- Plays a sound when the timer finishes.
- Simple and easy-to-use command-line interface.
- Clear and informative countdown display.

## Requirements

- Python 3.x
- `playsound` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Baelrin/Time_Tamer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Time_Tamer
   ```

3. Install the required library:

   ```bash
   pip install playsound
   ```

## Usage

1. Run the script:

   ```bash
   python master.py
   ```

2. Enter the number of minutes and seconds you want the timer to run.

3. The timer will start counting down and will play an alarm sound when the time is up.

## Code Overview

- `alarm(seconds)`: Sets an alarm to go off after a specified number of seconds.
- `get_positive_int(prompt)`: Prompts the user for a positive integer.
- Main script: Gathers user input for the timer and starts the alarm.

## Example

```bash
$ python master.py
How many minutes to wait: 1
How many seconds to wait: 30
Alarm will sound in: 01:30
```

## Contributing

Feel free to fork this repository and submit pull requests. Any enhancements or bug fixes are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [playsound](https://github.com/TaylorSMarks/playsound) for the simple sound playing functionality.
