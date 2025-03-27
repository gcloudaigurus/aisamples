from datetime import datetime
from collections import defaultdict

class CustomerSupportApp:
    def __init__(self):
        self.customer_tickets = defaultdict(list)  # {customer_id: [ticket_id]}
        self.ticket_details = {}  # {ticket_id: {received_time, description, priority}}
        self.support_engineers = defaultdict(list)  # {engineer_id: [(customer_id, ticket_id, status)]}
        self.initialize_sample_data()

    def initialize_sample_data(self):
        sample_tickets = [
            (101, '2025-03-15 10:00:00', 'Issue with login', 'High'),
            (102, '2025-03-16 12:30:00', 'Payment failure', 'Critical'),
            (103, '2025-03-17 15:45:00', 'Page not loading', 'Medium'),
            (104, '2025-03-18 09:15:00', 'Account locked', 'High'),
            (105, '2025-03-19 14:00:00', 'Slow response time', 'Low')
        ]
        
        customers = [1, 2, 1, 3, 4]  # Mapping customers to ticket IDs
        
        for i, (ticket_id, received_time, description, priority) in enumerate(sample_tickets):
            self.ticket_details[ticket_id] = {
                'received_time': datetime.strptime(received_time, '%Y-%m-%d %H:%M:%S'),
                'description': description,
                'priority': priority
            }
            self.customer_tickets[customers[i]].append(ticket_id)
        
        sample_engineers = [
            (201, 1, 101, 'Open'),
            (202, 2, 102, 'Closed'),
            (201, 1, 103, 'Open'),
            (203, 3, 104, 'Closed'),
            (202, 4, 105, 'Open')
        ]
        
        for engineer_id, customer_id, ticket_id, status in sample_engineers:
            self.support_engineers[engineer_id].append((customer_id, ticket_id, status))

    def search_customer_issues(self, customer_id):
        return [self.ticket_details[ticket_id] for ticket_id in self.customer_tickets.get(customer_id, [])]

    def top_10_issues_by_priority(self):
        priority_map = {'Critical': 1, 'High': 2, 'Medium': 3, 'Low': 4}
        sorted_tickets = sorted(
            self.ticket_details.items(), key=lambda x: priority_map[x[1]['priority']]
        )
        return sorted_tickets[:10]

    def issues_by_engineer(self, engineer_id):
        return self.support_engineers.get(engineer_id, [])

    def issues_status_by_engineer(self, engineer_id, status):
        return [ticket for ticket in self.support_engineers.get(engineer_id, []) if ticket[2] == status]

# Example Usage
app = CustomerSupportApp()

# Search for specific customer issues
print("Customer 1 Issues:", app.search_customer_issues(1))

# List top 10 issues by priority
print("Top 10 Issues by Priority:", app.top_10_issues_by_priority())

# Get issues assigned to a support engineer
print("Issues handled by Engineer 201:", app.issues_by_engineer(201))

# Get open issues for a support engineer
print("Open issues for Engineer 201:", app.issues_status_by_engineer(201, 'Open'))

# Get closed issues for a support engineer
print("Closed issues for Engineer 202:", app.issues_status_by_engineer(202, 'Closed'))
