from microbit import *

# Initialize the tamagotchi's status
hunger = 0
happiness = 50
temperature = 25

# Define the avatar images
happy_image = Image("09090:"
                    "09090:"
                    "00900:"
                    "99999:"
                    "09990:")

neutral_image = Image("09090:"
                      "09990:"
                      "00900:"
                      "90009:"
                      "09990:")

sad_image = Image("09090:"
                  "90909:"
                  "00900:"
                  "09990:"
                  "00900:")

surprised_image = Image("09090:"
                        "09090:"
                        "00900:"
                        "90909:"
                        "09990:")

angry_image = Image("09090:"
                    "09090:"
                    "00900:"
                    "99999:"
                    "00900:")

sleeping_image = Image("00000:"
                       "09090:"
                       "09090:"
                       "00000:"
                       "09990:")

# Main loop
while True:
    # Check the tamagotchi's status and adjust the avatar image accordingly
    # Assign the avatar image based on the tamagotchi's emotion
    if happiness > 80:
        avatar = happy_image
    elif happiness > 60:
        avatar = neutral_image
    elif happiness > 40:
        avatar = surprised_image
    elif happiness > 20:
        avatar = sad_image
    else:
        avatar = sleeping_image

    # Display the avatar image
    display.show(avatar)

    # Check if the top button was pressed (to show the tamagotchi's status)
    if pin_logo.is_touched():
        display.scroll("Hunger: {}".format(hunger))
        display.scroll("Happiness: {}".format(happiness))
        display.scroll("Temperature: {} C".format(temperature))

    # Check if the A button was pressed (to feed the tamagotchi)
    if button_b.was_pressed():
        hunger = max(0, hunger - 10)
        happiness = min(100, happiness + 10)
        display.scroll("Yum!", delay=100)

    # Check if the B button was pressed (to play with the tamagotchi)
    if button_a.was_pressed():
        happiness = min(100, happiness + 20)
        display.scroll("Whee!", delay=100)

    # Adjust the tamagotchi's status over time
    hunger = min(100, hunger + 1)
    happiness = max(0, happiness - 1)
    # Read the temperature sensor and update the temperature variable
    temperature = temperature # assuming a temperature sensor is connected

    # Wait for a short time to avoid rapid updates
    sleep(1000)
