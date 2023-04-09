from microbit import *
import uarray as np


# Set up initial values for the pet
name = "Pet"
age = 0
hunger = 0
happiness = 0
health = 100
level = 0

#Machine Learning


# Collect and preprocess Tamagotchi data
data = np.loadtxt("tamagotchi_data.csv", delimiter=",")
X = data[:, :-1]
y = data[:, -1]

# Split data into training and testing sets
X_train, y_train = X[:100], y[:100]
X_test, y_test = X[100:], y[100:]

# Define the machine learning model
model = tf.keras.Sequential([
  tf.keras.layers.Dense(32, activation='relu', input_shape=(4,)),
  tf.keras.layers.Dense(16, activation='relu'),
  tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# Train the model on the training data
model.fit(X_train, y_train, epochs=10)

# Evaluate the model on the testing data
loss = model.evaluate(X_test, y_test)

# Save the model in the TensorFlow Lite Micro format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("tamagotchi_model.tflite", "wb").write(tflite_model)


# Define function to display the pet's current status
def display_name():
    status_str = "{0}\n".format(name)
    display.scroll(status_str)

# Initialize the menu options
menu_options = ["Status", "Feed", "Play Pong", "Sleep", "Evolve"]

# Initialize the current menu option to 0 (the first option)
current_option = 0

# Main loop
while True:
    # Display the current menu option
    display.scroll(menu_options[current_option], delay=100)

    # Check if the A button was pressed
    if button_a.was_pressed():
        # Decrement the current menu option (wrap around to the end of the list)
        current_option = (current_option - 1) % len(menu_options)

    # Check if the B button was pressed
    if button_b.was_pressed():
        # Increment the current menu option (wrap around to the beginning of the list)
        current_option = (current_option + 1) % len(menu_options)

    # Check if the current option is "Status"
    if menu_options[current_option] == "Status":
        # Display the current status (e.g. temperature)
        temperature = temperature()
        display.scroll("Temperature: {} C".format(temperature), delay=100)

    # Check if the current option is "Feed"
    elif menu_options[current_option] == "Feed":
        # Do something to feed the tamagotchi
        display.show(Image.HAPPY)

    # Check if the current option is "Play Pong"
    elif menu_options[current_option] == "Play Pong":
        # Do something to play pong
        display.show(Image.ARROW_W)

    # Check if the current option is "Sleep"
    elif menu_options[current_option] == "Sleep":
        # Do something to put the tamagotchi to sleep (e.g. play a sound)
        display.scroll("Shhhhh")
    
    # Check if the current option is "Evolve"
    elif menu_options[current_option] == "Evolve":
        # Do something to evolve the tamagotchi
        display.show(Image.SILLY)
        sleep(1000)
        display.show(Image.SAD)
        sleep(1000)

    # Wait for a short time to avoid rapid button presses
    sleep(100)
