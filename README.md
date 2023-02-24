# Alligator-Cross Telegram Notifier
This program uses Docker to send a Telegram notification (text and image) to a specified channel whenever there is an Alligator-Cross setup occurring in "EURUSD" data on 5m timeframe.

## Prerequisites
* Docker
* Telegram API key and channel name
## Installation
* Clone the repository: git clone https://github.com/aligheshlaghi97/alligator-telegram-bot.git
* Navigate to the project directory: cd alligator-cross-telegram-notifier
* Build the Docker image: docker build -t alligator-cross-notifier .
## Usage
* Start the Docker container: docker run -d --name alligator-cross-notifier alligator-cross-notifier
* To stop the container: docker stop alligator-cross-notifier
* To remove the container: docker rm alligator-cross-notifier
* The program will automatically check for Alligator-Cross setups every minute and send a notification to the specified Telegram channel if one is detected.

## Configuration
You have to make a telegram bot from @BotFather. Then make a channel and make that bot, an admin of your channel (with message sending permissions). The program uses environment variables for configuration. You can set these variables by creating a .env file in the project directory (app/.env) with the following values:

* BOT_TOKEN: Your Bot Telegram API key 
* CHANNEL_ID: The name of the Telegram channel to send notifications to

## Telegram Channel
Messages and images are sent to a Telegram channel "@alligator_signal". Please feel free to join the channel to stay updated on the signals.

## Contributing
Thank you for your interest in contributing to Alligator-Cross Telegram Notifier! There are several ways you can help:

### Bug Reports
If you encounter a bug while using Alligator-Cross Telegram Notifier, please open a new issue on the project's GitHub page. When submitting a bug report, please include:

* A detailed description of the issue
* Steps to reproduce the issue, if possible
* Any error messages or other relevant information
### Feature Requests 
If you have an idea for a new feature or improvement to Alligator-Cross Telegram Notifier, please open a new issue on the project's GitHub page. When submitting a feature request, please include:

* A detailed description of the feature or improvement
* Any relevant use cases or scenarios
* Any potential drawbacks or concerns
### Pull Requests

If you would like to contribute code to Alligator-Cross Telegram Notifier, please submit a pull request on the project's GitHub page. When submitting a pull request, please:

* Create a new branch for your changes
* Follow the existing code style and conventions
* Write clear commit messages and include any necessary documentation or tests

### Contact
If you have any questions or concerns about contributing to Alligator-Cross Telegram Notifier, please feel free to contact me at Aliigheshlaghi97@gmail.com.







## License
This project is licensed under the MIT License. See the LICENSE file for details.



