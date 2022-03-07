from djitellopy import Tello

import time


def main() -> None:
    tello = Tello()
    tello.connect()
    try:
        while True:
            cmd = input("> ")
            print(f"Running {cmd} command")
            # TODO (Task 1): Fill in your code ########################################################
            ##################################################################################
            tello.takeoff()
            ##################################################################################
            if tello.is_flying:
                tello.land()
    except Exception as e:
        print(e)
    finally:
        tello.end()


if __name__ == "__main__":
    main()
