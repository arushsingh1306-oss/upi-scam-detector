import pandas as pd

scam_messages = [
    "Dear customer your KYC will expire today. Update immediately or account will be blocked https://bit.ly/kyc-update",
    "Congratulations! You have won Rs 50,000 in lucky draw. Click here to claim https://tinyurl.com/claim-prize",
    "URGENT: Your account has been suspended. Verify your UPI PIN now to reactivate https://verify-account.xyz",
    "You have received Rs 5000 refund. Click link to collect https://refund-claim.tk",
    "Your electricity bill is pending. Pay now to avoid disconnection https://bill-pay-now.info",
    "Bank alert: Unusual activity detected. Confirm your identity by entering OTP on this link https://secure-bank-verify.com",
    "Job offer! Earn Rs 5000 daily working from home. Register now and pay Rs 199 registration fee",
    "Your SBI account will be blocked in 24 hours. Update PAN card details immediately https://sbi-kyc-update.net",
    "Free recharge of Rs 999 waiting for you. Click to claim before offer expires https://free-recharge-claim.xyz",
    "Loan approved instantly! No documents required. Click here to get Rs 50000 in your account https://instant-loan-approve.com",
    "Your Paytm KYC is incomplete. Complete now or wallet will be frozen https://paytm-kyc-verify.tk",
    "Congratulations you are selected for Amazon lucky winner prize of Rs 25000. Claim now https://amazon-lucky-draw.xyz",
    "Dear user, someone tried to login to your account. Click to secure your account immediately https://secure-login-alert.com",
    "Your UPI ID has been used for a transaction of Rs 9999. If not done by you click here to block https://upi-block-now.tk",
    "Get Rs 2000 cashback instantly. Just click and enter your UPI PIN to receive https://cashback-claim-now.xyz",
    "Income tax refund of Rs 15000 approved. Click to claim before deadline https://tax-refund-claim.info",
    "Your mobile number won a lottery of Rs 1000000. Send your bank details to claim now",
    "Alert: Your debit card will expire today. Update details on this link https://card-update-secure.tk",
    "Free Netflix subscription for 1 year. Click here to activate https://free-netflix-offer.xyz",
    "Your electricity connection will be cut tonight. Pay pending bill immediately https://electricity-bill-pay.info",
]

safe_messages = [
    "Your OTP for login is 482910. Do not share this with anyone.",
    "Rs 500 has been debited from your account for Swiggy order. Available balance Rs 12450",
    "Your Amazon order has been shipped and will arrive by tomorrow evening",
    "Meeting scheduled for 3pm today. Please join the call on time",
    "Rs 2000 credited to your account from salary. Available balance Rs 45000",
    "Your electricity bill of Rs 850 has been paid successfully",
    "Reminder: Your exam is scheduled for next Monday at 10am",
    "Thank you for shopping with us. Your invoice has been generated",
    "Your flight PNR ABC123 is confirmed for tomorrow 6am departure",
    "Happy birthday! Wishing you a wonderful year ahead",
    "Your electricity meter reading has been recorded for this month",
    "Your college fee payment of Rs 15000 has been received successfully",
    "Rs 1200 sent to Rahul via UPI. Transaction ID 123456789",
    "Your Zomato order is out for delivery, arriving in 15 minutes",
    "Class test postponed to next week due to holiday",
    "Your monthly statement is ready. Please check your email",
    "Reminder: Submit your assignment by Friday 5pm",
    "Your recharge of Rs 199 was successful. Validity till next month",
    "Doctor appointment confirmed for tomorrow at 11am",
    "Your package has been delivered. Thank you for shopping with us",
]

data = []
for msg in scam_messages:
    data.append({"message": msg, "label": "scam"})
for msg in safe_messages:
    data.append({"message": msg, "label": "safe"})

df = pd.DataFrame(data)
df.to_csv("messages.csv", index=False)

print(f"Dataset created with {len(df)} messages")
print(f"Scam messages: {len(scam_messages)}")
print(f"Safe messages: {len(safe_messages)}")
print("Saved to messages.csv")