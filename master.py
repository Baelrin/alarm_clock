import logging
import time
from playsound import playsound

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants for clearing the screen and returning the cursor
CLEAR = "\033[2j"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    """
    Sets an alarm to go off after a specified number of seconds.

    :param seconds: Number of seconds until the alarm goes off.
    """
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        # Print the time left until the alarm sounds
        print(
            f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}",
            end="\r",
        )

    try:
        # Play the alarm sound
        playsound("alarm.mp3")
        logging.info("Alarm sound played successfully.")
    except Exception as e:
        logging.error(f"Error playing sound: {e}")


def get_positive_int(prompt):
    """
    Prompts the user for a positive integer.

    :param prompt: The prompt to display to the user.
    :return: A positive integer input by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Value must be a positive integer.")
            return value
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    # Get the number of minutes and seconds from the user
    minutes = get_positive_int("How many minutes to wait: ")
    seconds = get_positive_int("How many seconds to wait: ")
    total_seconds = minutes * 60 + seconds

    # Start the alarm
    alarm(total_seconds)
