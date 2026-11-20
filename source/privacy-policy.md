# Privacy Policy

Last updated: 19 November 2026

This Privacy Policy explains how Marlow ("the App") handles your information. Marlow is published by Fong Whye Hin, an individual based in Singapore ("we", "us", "our"). We are responsible for your personal data as described here, and you can reach us at fwh0115@gmail.com.

## In Short

- **Your money data stays in your own Google Sheet**, in your own Google Drive. We don't run servers that store your transactions, balances, budgets or goals, and we can't see them.
- **The App can only open the files it creates or you choose**, not the rest of your Google Drive, email or contacts.
- **Some features send limited data to an AI provider, through our AI server, only if you allow it:** Auto-Log sends the text of a bank or card notification to be read, and Marlow, the App's AI coach, sends a summary of your money and, when a question needs them, the details it asks about (such as transactions, accounts and goals).
- **No ads, no tracking, no selling.** We don't show ads, track you across other apps or websites, sell or share your personal data for advertising, or use analytics or advertising SDKs.
- **Anonymous usage counts are off unless you turn them on.**
- **You're in control.** You can delete your Marlow account in the App, and delete your sheet from your Drive at any time.

## 1. Information the App Handles, and Why

### Your Google account

When you connect Google, the App receives your Google account email address and name, and a sign-in token. It uses them to create and open your Marlow sheet, to share it with family members you invite, and to show who you're signed in as. The App asks only for Google's `drive.file` permission. That lets it work with the files it creates or you choose, and nothing else in your Drive. The sign-in token is kept in your phone's Keychain.

### Sign in with Apple

If you sign in with Apple, the App receives a sign-in token and, the first time, the name and email address you choose to share (which may be an Apple private relay address). It uses them only to sign you in and to show your name.

### Your financial records

Your transactions, accounts and balances, categories, budgets, goals, debts, investments, recurring payments, family members' names, the priorities you set, your chat with Marlow and what Marlow remembers from it are what you, or Auto-Log, enter into the App. They are stored:

- **in your Google Sheet**, in your Google Drive, which the App reads and writes through Google's APIs and a script inside the sheet that runs under your own Google account; and
- **on your phone**, as a working copy so the App works offline, along with your preferences.

We, the publisher, don't receive them. Google stores your sheet under its own terms and privacy policy.

Your phone's copy is included in your iCloud Backup if you have it turned on (or your Android backup, on Android). Some preferences, like Marlow's style and commitments, are kept only on your phone and in its backup.

### Your family sheet

If you invite family members, they can open the shared sheet. That includes the transactions and accounts shared with them, each person's name, birth year if entered, and priorities, the family's chat with Marlow, and which plan the family's subscriber has and until when, so everyone in the sheet gets that plan's features. Only invite people you trust with this information.

### Asking before AI

Auto-Log and Marlow use AI only if you allow it. The App asks you during setup (or the first time it needs to, if you set up before it asked), shows exactly what is sent and to which provider, and sends nothing until you choose Allow. You can change your mind at any time in Reminders & Marlow › Privacy › Use AI Features.

### Auto-Log (bank, card and broker notifications)

If you set up the Marlow Shortcut, it passes the notifications you choose to the App. If you have allowed AI features, then to read a notification the App sends the following, through our AI server (see below), to our AI provider:

- the notification's text (for example a merchant, an amount, and the last digits of a card if the notification includes them);
- the name of the app it came from and when it arrived; and
- your category names, so the AI can suggest one.

The result is written to your sheet. If you haven't allowed AI features, nothing is sent: the alert is kept on your phone, matched there where it can be, and read once you allow AI (or you fill it in yourself).

Notifications that aren't transactions, like sign-in codes or promotions, are dropped without being stored. The full notification text isn't stored by us.

### Marlow (the AI Coach)

If you have allowed AI features, when you ask Marlow a question or ask it to change a plan or goal, the App sends your question, the last 10 messages of your chat with it and a short recap of the chat before them (so it can follow on, with who asked each said only as "Me" or "Partner"), and a summary of your money (such as your income, spending against your budget, savings, net worth, ages, goals and debts), through our AI server, to our AI provider. When a question needs more, Marlow asks specialists that each look at one part of your money, and the App sends each of them only that part: for example your transactions with their dates, payees, categories and accounts; your account names and balances; your goals and debts; your investments; or the Auto-Log questions waiting for you. In a family chat, it may use what your family shares (its accounts, goals and budget) in full, but another member's own money only as totals, never their transactions; in Just Me, only your own. It never sends your Google sign-in or the account numbers you've saved. Marlow can draft changes (a budget amount, a goal, a recurring payment, a transaction's category, a transaction to log), but nothing in your sheet changes until you tap Apply, and you can undo it. Every ten or so messages, and when you clear the chat, the App sends the older ones the same way (by role, not name) to have that recap written and to note a few things worth remembering (such as goals and ages you chose, decisions, and how you like advice; never account numbers, passwords or health); it isn't counted as one of your questions to Marlow. What Marlow remembers goes with each question you ask it. Your chat with Marlow, its recap and what it remembers are kept in your Google Sheet, so they're there on a new phone and everyone in your family sheet sees the same chat and what Marlow remembers from it (your Just Me chat's only on your phones). Clear Chat in Marlow removes the chat and its recap for everyone; what Marlow remembers stays unless you choose Clear Chat and Memory, and you can see it and remove any of it in Reminders & Marlow › What Marlow Remembers. Your One Thing, forecasts, heads-ups, budget suggestions and nudges are worked out on your phone and aren't sent anywhere.

### Investment sectors

If you have allowed AI features, the App sends the ticker of each stock you hold that doesn't have a sector yet (just the symbol and exchange, such as NASDAQ:PANW), through our AI server, to our AI provider, so it can name the stock's sector (such as Technology). Nothing else goes with it: no amounts, units, prices or anything else about you. Our server keeps each ticker's sector in a list that isn't linked to anyone, so the next person who holds that stock gets its sector without asking the AI again. You can change a stock's sector in the App at any time; your choice is kept in your Google Sheet, not on our server.

### Our AI providers

The App uses Google's Gemini and Anthropic's Claude, both run for us on Google Cloud's Vertex AI. We choose which model answers each feature, and if one is unavailable your request goes to another of them. We use Vertex AI's paid service, whose terms don't allow the content we send to be used to train AI models. It may be kept for a limited time to detect abuse, as those terms describe. These providers may process data in the United States and other countries.

### Our AI server

The App doesn't contain an AI key. It sends each Auto-Log, Marlow or sector request to our server on Google Cloud, together with your Google sign-in token, which proves the request comes from the App. Our server:

- checks the sign-in token, then passes the request to our AI provider and returns the answer;
- adds one to a monthly count of your AI requests, so no one can use more than the App allows. The count is kept under a one-way code made from your Google account ID, not your name or email, and is deleted after about three months; and
- doesn't store what you send or the answers, except each stock ticker's sector (see Investment sectors above), which isn't linked to you. Like any web service, its logs keep technical details such as your IP address and the time of each request for up to 30 days, for security and troubleshooting.

Requests from our server to the AI provider carry no information that identifies you.

### Purchases

When you subscribe, Apple (or Google Play) handles the payment. We don't receive your payment card details. The App receives confirmation of which plan you bought and when it renews or ends, so it can turn on that plan's features, and writes that plan status to your family sheet.

### Investments

The prices of your holdings come from Google Finance formulas inside your own sheet. To show company logos, the App requests logo images by ticker symbol from public logo services (financialmodelingprep.com and parqet.com). Like any web request, these show your IP address to those services, but nothing else about you.

### App settings from us

The App regularly downloads its settings (such as monthly allowances and which AI model to use) from our server on Google Cloud. This download sends nothing about you. To check whether your account has complimentary access, the App asks our server with your Google sign-in, which carries your email address; the server looks up a one-way hash of it in our list and answers only about your own account. It doesn't keep your email address or the request.

### Anonymous usage counts (optional)

Off unless you turn it on, during setup or in Reminders & Marlow › What's Shared. If you do, once a month the App adds these to totals across all users: your plan (Free, Plus or Family), how much you used Auto-Log's AI and Marlow last month, how many times a sync, a Marlow question or an Auto-Log alert didn't work (counts only, never what it was about), and, for whoever set up the family's sheet, whether they did and how many people are in each age group (for example 25–34). Only the combined totals are kept. They carry no identifier for you or your phone, and never your name, email, birth year, amounts or anything in your sheet. You can turn this off at any time.

### Notifications

Reminders and nudges from Marlow are scheduled on your phone. Amounts are hidden on a locked screen unless you turn that off in Reminders & Marlow.

### Diagnostics

If the Shortcut or a sync runs into trouble, the App keeps a short log on your phone to help fix it. It stays on your phone unless you choose to copy and send it to us.

### What we don't collect

We don't collect your location, contacts, photos, browsing history, advertising identifiers or bank login details. We don't connect to your bank accounts.

## 2. Our Legal Bases

Where laws such as the EU or UK GDPR apply, we rely on:

- **providing the service you asked for** (contract), to run the App, sync your sheet, read alerts you choose to send, answer your questions to Marlow and provide your plan;
- **your consent**, for anonymous usage counts and for the features that send data to an AI provider, which you can withdraw at any time by turning them off; and
- **our legitimate interests**, to keep the App secure and working, in ways that don't override your rights.

## 3. How Long Information Is Kept

- Your sheet stays in your Google Drive until you delete it.
- The App's copy on your phone stays until you delete your Marlow account or the App.
- AI providers keep request data only as long as their API terms allow, typically up to about 30 days, for abuse monitoring.
- Our AI server keeps each month's count of your AI requests for about three months, and its technical logs for up to 30 days.
- Anonymous totals are kept as long as they're useful to us. They can't be linked back to you.
- If you email us, we keep your messages for as long as needed to help you, and then up to two years.

## 4. Your Choices and Rights

- **See and change your data:** it's all in your Google Sheet and the App.
- **Export it:** download your sheet from Google Sheets in any format Google offers.
- **Delete your account:** Settings › Delete Account removes your Marlow account and erases the App's data on your phone. You can choose to hand your family sheet to another member first. Your Google Sheet then stays in your Drive until you delete it there.
- **Stop sending data to AI:** turn off Reminders & Marlow › Privacy › Use AI Features.
- **Turn off anonymous usage counts:** Reminders & Marlow › What's Shared.
- **Remove Google access:** in your Google Account › Security › Third-party apps with account access.

Depending on where you live (for example under Singapore's PDPA, the EU or UK GDPR, or Californian law), you may have the right to access, correct, delete, restrict or object to our handling of your personal data, to data portability, and to withdraw consent. To use these rights, email fwh0115@gmail.com. We'll reply within 30 days. You can also complain to your data protection authority; in Singapore, that is the Personal Data Protection Commission.

**California residents:** we don't sell or share personal information for cross-context behavioural advertising, and we don't use sensitive personal information to infer characteristics about you.

## 5. Google API Services

Marlow's use and transfer to any other app of information received from Google APIs will adhere to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements. In particular:

- we use data from your Google Sheet only to provide and improve the App's features for you;
- we transfer it to others only as needed to provide those features (such as reading an alert or answering a coach question), to comply with the law, or as part of a merger or acquisition with your notice;
- we never use it for advertising, never sell it, and never allow humans to read it unless you ask us to (for example for support), it's needed for security or the law, or it's aggregated and anonymised; and
- we don't use it, or allow our AI providers to use it, to develop, improve or train generalised AI or machine-learning models.

## 6. Security

Your data travels over encrypted connections (HTTPS). Sign-in tokens are kept in your phone's Keychain. Your sheet is protected by your Google account, so please use a strong password and two-step verification. No system is perfectly secure, and if a breach affecting your personal data happens, we'll tell you and the authorities as the law requires.

## 7. International Transfers

Google, Apple, our AI providers and the logo services may process data in countries other than yours, including the United States. Where the law requires, we rely on safeguards such as standard contractual clauses in those providers' terms.

## 8. Children

Marlow is not for anyone under 18. We don't knowingly handle children's personal data. If you think a child has used the App, contact us and we'll help remove their information.

## 9. Changes to This Policy

We'll update this policy when the App changes how it handles your information. If a change is significant, we'll tell you in the App before it takes effect. The date at the top shows the latest version.

## 10. Contact Us

Questions, requests or complaints about privacy:

- Email: fwh0115@gmail.com
- Data Protection Officer (Singapore PDPA): fwh0115@gmail.com
