# Amazon Price Tracker

This is a Python script that monitors the price of a product on Amazon and sends an email alert when the product's price falls below a specified target price.

## Features

- Scrapes product prices from Amazon using `requests` and `BeautifulSoup`.
- Sends an email alert using the `smtplib` library when the product's price drops below the target price.
- Configurable target price and email settings.

---

## Requirements

- Python 3.6+
- Libraries: `requests`, `beautifulsoup4`, `dotenv`
- An Amazon product URL
- A valid email account to send alerts

---


3. **Set up environment variables**  
   Create a `.env` file in the project directory with the following content:
   ```dotenv
   sender_email=your_email@example.com
   sender_password=your_email_password
   receiver_email=receiver_email@example.com
   smtp_address=smtp.your_email_provider.com
   ```
   Replace the placeholders with your email credentials and SMTP server address.

4. **Update script settings**  
   - Set the `URL` variable to the product's Amazon page URL:  
     `https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6`
   - Set the `target_price` variable to your desired price threshold.

---

## Usage

1. **Run the script**  
   Execute the script using the command:
   ```bash
   python main.py
   ```

2. The script will:
   - Fetch the product price from the specified URL.
   - Compare the current price to the target price.
   - Send an email alert if the current price is below the target price.

---

## Example Output

![Screenshot 2024-12-08 133355](https://github.com/user-attachments/assets/20c931a6-9650-4919-a90b-522368bee1b2)

---

## Notes

- **Amazon Website Changes**: The script may stop working if Amazon changes its website structure. Update the `class_` or `id` values in the `BeautifulSoup` selectors if this happens.
- **Rate Limits**: Avoid frequent scraping to prevent being blocked by Amazon.
- **Security**: Store sensitive credentials securely and avoid hardcoding them in the script.

---
