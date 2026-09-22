import pandas as pd
import random

random.seed(42)

banks = ["SBI", "HDFC", "ICICI", "Axis Bank", "PNB", "Kotak", "Paytm", "PhonePe", "Google Pay", "BOB"]
names = ["Rahul", "Priya", "Amit", "Sneha", "Vikram", "Anjali", "Rohan", "Kavita", "Suresh","Arush", "Arpit", "abhijeet", "Neha"]
amounts = [500, 999, 1500, 2000, 2500, 5000, 9999, 10000, 15000, 25000, 50000, 100000]
fake_links = [
    "bit.ly/kyc-update", "tinyurl.com/claim-now", "verify-account.xyz",
    "secure-bank-verify.com", "refund-claim.tk", "kyc-update-now.info",
    "instant-loan-approve.com", "account-block-alert.xyz", "cashback-claim.tk",
    "prize-winner-claim.info",
]

scam_templates = [
    "Dear customer your {bank} KYC will expire today. Update immediately or account will be blocked https://{link}",
    "Congratulations! You have won Rs {amount} in {bank} lucky draw. Click here to claim https://{link}",
    "URGENT: Your {bank} account has been suspended. Verify your UPI PIN now to reactivate https://{link}",
    "You have received Rs {amount} refund from {bank}. Click link to collect https://{link}",
    "Your electricity bill of Rs {amount} is pending. Pay now to avoid disconnection https://{link}",
    "{bank} alert: Unusual activity detected on your account. Confirm your identity by entering OTP on this link https://{link}",
    "Job offer! Earn Rs {amount} daily working from home. Register now and pay registration fee https://{link}",
    "Your {bank} account will be blocked in 24 hours. Update PAN card details immediately https://{link}",
    "Free recharge of Rs {amount} waiting for you. Click to claim before offer expires https://{link}",
    "Loan approved instantly! No documents required. Click here to get Rs {amount} in your account https://{link}",
    "Your {bank} KYC is incomplete. Complete now or wallet will be frozen https://{link}",
    "Congratulations you are selected for lucky winner prize of Rs {amount}. Claim now https://{link}",
    "Dear user, someone tried to login to your {bank} account. Click to secure your account immediately https://{link}",
    "Your UPI ID has been used for a transaction of Rs {amount}. If not done by you click here to block https://{link}",
    "Get Rs {amount} cashback instantly. Just click and enter your UPI PIN to receive https://{link}",
    "Income tax refund of Rs {amount} approved. Click to claim before deadline https://{link}",
    "Your mobile number won a lottery of Rs {amount}. Send your bank details to claim now",
    "Alert: Your {bank} debit card will expire today. Update details on this link https://{link}",
    "Free 1 year subscription waiting for you. Click here to activate https://{link}",
    "Your electricity connection will be cut tonight. Pay pending bill immediately https://{link}",
    "{name} has sent you a payment request of Rs {amount} on {bank}. Approve now https://{link}",
    "Your {bank} net banking has been locked due to suspicious activity. Unlock here https://{link}",
    "Last warning: Your Aadhaar linked {bank} account will be deactivated today. Verify now https://{link}",
    "You are eligible for a government subsidy of Rs {amount}. Claim before it expires https://{link}",
    "Your credit card limit has been increased to Rs {amount}. Click to activate now https://{link}",
    "Hurry! Only 2 hours left to claim your Rs {amount} cashback reward https://{link}",
    "{bank} security team: verify your account within 30 minutes to avoid permanent block https://{link}",
    "You have an unclaimed parcel. Pay Rs {amount} customs fee to release it https://{link}",
    "Your SIM card will be deactivated today due to KYC mismatch. Update now https://{link}",
    "Work from home and earn Rs {amount} per week guaranteed, limited seats, register now https://{link}",
]

safe_templates = [
    "Your OTP for login is {otp}. Do not share this with anyone.",
    "Rs {amount} has been debited from your account for Swiggy order. Available balance Rs {amount2}",
    "Your Amazon order has been shipped and will arrive by tomorrow evening",
    "Meeting scheduled for 3pm today. Please join the call on time",
    "Rs {amount} credited to your account from salary. Available balance Rs {amount2}",
    "Your electricity bill of Rs {amount} has been paid successfully",
    "Reminder: Your exam is scheduled for next Monday at 10am",
    "Thank you for shopping with us. Your invoice has been generated",
    "Your flight PNR {pnr} is confirmed for tomorrow 6am departure",
    "Happy birthday {name}! Wishing you a wonderful year ahead",
    "Your electricity meter reading has been recorded for this month",
    "Your college fee payment of Rs {amount} has been received successfully",
    "Rs {amount} sent to {name} via UPI. Transaction ID {txnid}",
    "Your Zomato order is out for delivery, arriving in 15 minutes",
    "Class test postponed to next week due to holiday",
    "Your monthly statement is ready. Please check your email",
    "Reminder: Submit your assignment by Friday 5pm",
    "Your recharge of Rs {amount} was successful. Validity till next month",
    "Doctor appointment confirmed for tomorrow at 11am",
    "Your package has been delivered. Thank you for shopping with us",
    "{name}, your {bank} account balance is Rs {amount2} as of today",
    "Your rent payment of Rs {amount} has been received by your landlord",
    "Your gym membership has been renewed for another month",
    "Your book is due for return at the library by next Tuesday",
    "Your Netflix subscription has been renewed for Rs {amount}",
    "Your {bank} statement for last month is now available in the app",
    "Your ticket booking for the movie tonight is confirmed",
    "Your internet bill of Rs {amount} has been auto-debited successfully",
    "Congratulations on completing your course! Certificate will be issued soon",
    "Your food delivery partner {name} has picked up your order",
]

def fill_template(template):
    return template.format(
        bank=random.choice(banks),
        name=random.choice(names),
        amount=random.choice(amounts),
        amount2=random.choice(amounts),
        link=random.choice(fake_links),
        otp=random.randint(100000, 999999),
        pnr="".join(random.choices("ABCDEFGH12345", k=6)),
        txnid=random.randint(100000000, 999999999),
    )

NUM_SCAM = 500
NUM_SAFE = 500

scam_messages = set()
while len(scam_messages) < NUM_SCAM:
    template = random.choice(scam_templates)
    scam_messages.add(fill_template(template))

safe_messages = set()
while len(safe_messages) < NUM_SAFE:
    template = random.choice(safe_templates)
    safe_messages.add(fill_template(template))

data = []
for msg in scam_messages:
    data.append({"message": msg, "label": "scam"})
for msg in safe_messages:
    data.append({"message": msg, "label": "safe"})

df = pd.DataFrame(data)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("messages.csv", index=False)

print(f"Dataset created with {len(df)} messages")
print(f"Scam messages: {len(scam_messages)}")
print(f"Safe messages: {len(safe_messages)}")
print("Saved to messages.csv")