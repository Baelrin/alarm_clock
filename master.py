from playsound import playsound
import time

CLEAR = "\033[2j"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(
            f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}",
            end="\r",
        )

    try:
        playsound("alarm.mp3")
    except Exception as e:
        print(f"Error playing sound: {e}")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Value must be a positive integer.")
            return value
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    minutes = get_positive_int("How many minutes to wait: ")
    seconds = get_positive_int("How many seconds to wait: ")
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)
