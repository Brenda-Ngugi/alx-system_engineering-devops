Done by : Brenda Ngugi
Issue Summary:

Duration of the outage: 2 hours from 2024-02-03 10:00 PM EST to 2024-02-03 12:00 AM EST.

Impact: The web application was down during the outage period, resulting in a complete service disruption. All users were affected, and they were unable to access the application.

Root Cause: The root cause of the outage was a database failure due to a corrupted database index.

Timeline:

2024-02-03 10:00 PM EST: The issue was detected when the monitoring alert triggered for the database server.
The investigation started immediately, and it was determined that the database server was experiencing high CPU usage.
The assumption was made that the high CPU usage was due to a database query issue, so the query logs were analyzed.
However, this investigation path turned out to be misleading, as the query logs did not reveal any issues.
The incident was then escalated to the database team, who determined that the root cause was a corrupted database index.
The corrupted index was fixed, and the database server was restored to normal operation.
Finally, the web application was restarted, and users were able to access it again.
Root Cause and Resolution:

The root cause of the outage was a corrupted database index. This caused the database server to consume high CPU usage, leading to a complete service disruption.

To fix the issue, the database team had to rebuild the corrupted index. Once this was done, the database server returned to normal operation. After that, the web application was restarted, and users could access it again.

Corrective and Preventative Measures:

To prevent similar issues from happening in the future, we have identified several corrective and preventative measures:

We will implement a regular backup schedule for all databases to ensure data integrity.
We will implement a monitoring system that will alert us of any unusual CPU usage or errors in the database server.
We will review our disaster recovery plan to ensure that we have clear procedures in place for handling similar incidents.
We will conduct regular training sessions for our technical team on how to handle similar incidents in the future.

TODOs:
Implement regular backup schedule for all databases
Implement monitoring system for unusual CPU usage or errors in the database server
Review disaster recovery plan
Conduct regular training sessions for technical team




Conclusion
The outage was caused by a corrupted database index, which resulted in a complete service disruption. However, we were able to resolve the issue quickly and have identified several corrective and preventative measures to prevent similar incidents from happening in the future.
