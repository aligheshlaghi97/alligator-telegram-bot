# Alligator-Cross Telegram Notifier
Alligator-Cross Telegram Notifier is a Docker-based program that sends notifications to a designated Telegram channel when an Alligator-Cross setup is detected in "EURUSD" data on a 5-minute timeframe. An Alligator-Cross setup is defined as a shadow of a candle that intersects with the GreenLine of the Alligator indicator, according to the Bill Williams trading strategy. This program can be extended to detect other trading signals based on various technical indicators such as MACD, Moving Average, RSI, or specific candlestick patterns. With Alligator-Cross Telegram Notifier, traders can receive timely alerts and stay informed of market movements and opportunities.

## Prerequisites
* Docker
* Telegram Bot and Channel
## Installation
* Clone the repository: `git clone https://github.com/aligheshlaghi97/alligator-telegram-bot.git`
* Navigate to the project directory: `cd alligator-telegram-bot`
* Build the Docker image: `docker build -t alligator-telegram-bot` .
## Usage
* Start the Docker container: `docker run -d --name alligator-telegram-bot alligator-cross-notifier`
* To stop the container: `docker stop alligator-cross-notifier`
* To remove the container: `docker rm alligator-cross-notifier`
* The program will automatically check for Alligator-Cross setups (Shadow of candle crosses Alligator Lips (GreenLine)) every 5 minutes (on 5m candles) and send a notification to the specified Telegram channel if one is detected.

## Configuration
You have to make a telegram bot from @BotFather. Then make a channel and make that bot, an admin of your channel (with message sending permissions). The program uses environment variables for configuration. You can set these variables by creating a .env file in the project directory (app/.env) with the following values (like .envsample):

* `BOT_TOKEN`: Your Bot Telegram API key 
* `CHANNEL_ID`: The name of the Telegram channel to send notifications to

## Telegram Channel
Messages and images are sent to a Telegram channel https://t.me/alligator_signal. Please feel free to join the channel to stay updated on the signals.

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

Alligator-Cross Telegram Notifier is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for the full text.



