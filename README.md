# Alligator-Cross Telegram Notifier
This program uses Docker to send a Telegram notification (text and image) to a specified channel whenever there is an Alligator-Cross setup occurring in "EURUSD" data on 5m timeframe.

## Prerequisites
* Docker
* Telegram API key and channel name
## Installation
* Clone the repository: git clone https://github.com/your-username/alligator-cross-telegram-notifier.git
* Navigate to the project directory: cd alligator-cross-telegram-notifier
* Build the Docker image: docker build -t alligator-cross-notifier .
## Usage
Start the Docker container: docker run -d --name alligator-cross-notifier alligator-cross-notifier
To stop the container: docker stop alligator-cross-notifier
To remove the container: docker rm alligator-cross-notifier
The program will automatically check for Alligator-Cross setups every minute and send a notification to the specified Telegram channel if one is detected.

## Configuration
The program uses environment variables for configuration. You can set these variables by creating a .env file in the project directory with the following values:

* API_KEY: Your Bot Telegram API key
* CHANNEL_NAME: The name of the Telegram channel to send notifications to
## Credits
This program was created by Ali Gheshlaghi.

The Alligator indicator was created by Bill Williams.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



