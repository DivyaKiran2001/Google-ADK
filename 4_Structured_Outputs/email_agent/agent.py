from google.adk.agents import LlmAgent
from pydantic import BaseModel,Field
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# Define Output Schema

class EmailContent(BaseModel):
    subject : str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )

    body : str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )

# Create Email Generator Agent

root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email"
)

def send_email_smtp(sender_email, app_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)


if __name__ == "__main__":
    user_prompt = input("What should be the email be about?")

    response = root_agent.invoke(user_prompt)

    subject = response['email']['subject']
    body = response['email']['body']

    print("\n📨 Generated Email:")
    print(f"Subject: {subject}")
    print("Body:")
    print(body)

    # Step 4: Send via SMTP
    sender = input("\nEnter your Gmail address: ")
    app_password = input("Enter your App Password (not Gmail password): ")
    recipient = input("Enter recipient email address: ")

    send_email_smtp(sender,app_password,recipient,subject,body)
    