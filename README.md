This Stock Trading News Alert project is a simple yet powerful Python tool that keeps you updated on stock market movements and related news. It tracks a specified stock's daily closing prices using the Alpha Vantage API and calculates the percentage change between consecutive days. If the price change exceeds a defined threshold, the tool fetches the top three news articles related to the company using the NewsAPI and sends you an SMS alert via Twilio. The SMS includes the stock's price change percentage, a directional indicator (🔺 or 🔻), and news headlines with brief descriptions to keep you informed without manual monitoring.

To set up, you'll need API keys for Alpha Vantage and NewsAPI, as well as Twilio credentials for SMS notifications. Replace the placeholder keys in the script with your credentials and configure your Twilio phone number and recipient's number. Once the setup is complete, simply run the script to monitor your chosen stock and receive timely alerts whenever there’s a significant price movement. This project is perfect for traders, investors, or anyone who wants quick updates on stock trends and company news directly on their phone.
