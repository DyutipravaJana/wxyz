from playsound import playsound
import time

def dog_bark(times=3, delay=1):
    for i in range(times):
        print(f"Bark {i+1}!")
        playsound("dog_bark.wav")
        time.sleep(delay)

# Example: Make the dog bark 3 times with a 1-second delay
dog_bark()
