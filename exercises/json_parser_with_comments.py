import json

# 1. Open and read JSON file
with open('sentry_weekly_export.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

issues_list = data['issues']
filtered_issues = []

# 2. Filter bugs (collect the right ones into the list)
for issue in issues_list:
    # Access values via dictionary keys 
    if issue['status'] == 'unresolved' or issue['affected_users'] > 100:
        filtered_issues.append(issue)

# 3. Sort the records from the largest to the smallest quantity 'affected_users'
# Use lambda to specify which key to sort by
filtered_issues.sort(key=lambda x: x['affected_users'], reverse=True)

# Include only the top-3 in the report, to not spam
top_issues = filtered_issues[:3]

# 4. Creating nice text and write it in file
message_lines = ["🚨 *Weekly Sentry Crash Report - Top 3 Critical Issues* 🚨\n"]
for i, bug in enumerate(top_issues, 1):
    line = f"{i}. {bug['error_type']} in {bug['location']} ({bug['platform']}) - {bug['affected_users']} users affected"
    message_lines.append(line)

final_message = "\n".join(message_lines)

# Create file slack_message.txt and add text into there
with open('slack_message.txt', 'w', encoding='utf-8') as msg_file:
    msg_file.write(final_message)

print("✅ File slack_message.txt is created!\n")


# 5. Stub function for creating bugs in Jira
def create_jira_ticket(bug):
    # in real project I would call requests.post('https://jira.vinted.com/rest/api/...', json={...})
    print(f"[JIRA API] Bug report is created {bug['error_type']} on {bug['platform']} (Ticket: VNT-101)")

# Create bug for each issue in the list
for bug in top_issues:
    create_jira_ticket(bug)


# 6. Send file into Slack chat
def send_to_slack(text):
    # in real project I would use Slack Webhook:
    # webhook_url = "https://hooks.slack.com/services/T0000/B0000/XXXXX"
    # requests.post(webhook_url, json={"text": text})
    print("\n[SLACK API] Message is sent to #dev-alerts!")
    print("-" * 40)
    print(text)
    print("-" * 40)

send_to_slack(final_message)