# AVIV technical test solution

You can use this file to write down your assumptions and list the missing features or technical revamp that should
be achieved with your implementation.

## Notes

## Write here notes about your implementation choices and assumptions.
This approach involves the use of a lookup table for easy access to data while keeping a record of price change history. The architecture is designed to capture data changes in the listings table and reflect them in the listing_price_log table seamlessly. Here are further details and clarifications:

Implementation Choices:
Table Design: 
The listing_price_log table is structured as follows to accommodate data for API access and facilitate price change history tracking:
Table Structure
Listing_price_log 
    id SERIAL4 PRIMARY KEY,
    listing_id INT REFERENCES listing(id),
    price_change Float8, 
    updated_time TIMESTAMP

Function and Trigger: A function and trigger have been implemented to ensure automatic data insertion into the Listing_price_log table whenever there are any inserts or updates in the Listings table. This approach does not necessitate any changes to the existing architecture, thus ensuring a seamless integration.
Note: code is available at db/01_init_listing_table.sql

assumptions:
Unique Price Updates: the current implementation assumes that multiple consecutive updates with the same price for a particular listing are considered as single. 

Selected Columns: The data reporting specifically focuses on two key columns, namely "Date" and "Price," emphasizing their significance in the context of the listings and price change logs.

This implementation demonstrates a systematic approach to data management, allowing for efficient data access and tracking of price fluctuations. This strategy ensures that the existing architecture remains unaltered, minimizing potential disruptions while enabling comprehensive data monitoring and analysis.
## Questions

This section contains additional questions your expected to answer before the debrief interview.

- **What is missing with your implementation to go to production?**
current implementation showcases a robust data management system and an effective approach to tracking price changes, there are certain aspects to consider before deploying the system into a production environment. Here are some key considerations to ensure that implementation is production-ready:

Data Validation and Error Handling: Ensuring comprehensive data validation checks and robust error handling mechanisms are in place to prevent data inconsistencies and handle unforeseen errors effectively.additional test cases to improve the code coverage.

Security Measures: Implementing security measures to safeguard sensitive data, including user authentication, authorization controls, encryption for data at rest and in transit, and protection against common security threats.implementing Authentication mechanism.

Performance Optimization: Conducting thorough performance testing and optimization to ensure that the system can handle a large volume of data and user requests without compromising speed and efficiency. This may involve optimizing database queries, employing caching mechanisms, and scaling the system as needed.proper indexing and multi level table partitioning will help in organizing and aggregating the data. also Data retention tenure to be defined so historic data can be backup in different place.

Logging and Monitoring: Implementing comprehensive logging and monitoring solutions to track system activities, identify potential issues, and facilitate timely troubleshooting. This includes logging database transactions, monitoring system performance, and setting up alerts for critical events.

Scalability and Redundancy: Plan for scalability by designing the system to handle increased data and user loads over time. Implement redundancy measures to ensure high availability and data resilience, including data backups, failover mechanisms, and disaster recovery plans.

Documentation and Maintenance: Create detailed documentation outlining the system architecture, data models, API endpoints, and any relevant processes for future reference. Establish a systematic maintenance plan for regular updates, bug fixes, and system enhancements.

Compliance and Regulations: Ensure compliance with relevant data protection regulations and industry standards, especially if handling sensitive or personally identifiable information.
- **How would you deploy your implementation?**
Container Orchestration with Kubernetes: in the current architecture Docker was used, but for production deployment its better to Incorporate Kubernetes to manage containerized applications efficiently. 

CI/CD setup: Implement a robust CI/CD pipeline to automate the build, testing, and deployment processes.

Infrastructure as Code (IaC): Use infrastructure-as-code tools such as Terraform or AWS CloudFormation to automate the provisioning and management of infrastructure resources.

Monitoring and Logging: Implement monitoring and logging solutions such as Prometheus, Grafana, ELK stack, or Splunk to ensure real-time visibility into the application's performance and health.

Security Best Practices: Apply security best practices such as encryption, and secure network policies to safeguard the application and data.

Scalability and Load Balancing: Implement load balancing strategies to distribute traffic evenly and prevent service disruptions during high traffic periods.

Backup and Disaster Recovery: Set up data backup mechanisms and disaster recovery plans to protect against data loss and ensure business continuity. Regularly test the backup and recovery procedures to verify their effectiveness.

Documentation and Knowledge Transfer: Maintain comprehensive documentation detailing the deployment process, configurations, and troubleshooting guidelines. Facilitate knowledge transfer to the operations team to ensure smooth handover and efficient management of the deployed system.

- **If you had to implement the same application from scratch, what would you do differently?**

- **The application aims at storing hundreds of thousands listings and millions of prices, and be accessed by millions
  of users every month. What should be anticipated and done to handle it?**

  NB: You must update the [given architecture schema](./schemas/Aviv_Technical_Test_Architecture.drawio) by importing it
  on [diagrams.net](https://app.diagrams.net/) 

To handle a large-scale application with hundreds of thousands of listings, millions of prices, and millions of monthly users,consideration of the database design is crucial. Given the scale of the application, a robust and scalable database solution is essential. In this scenario, considering a combination of different database technologies can be beneficial.

Relational Database for Structured Data: Utilize a relational database for structured data like user information, listings, and other related metadata ensuring data integrity and reliability.

NoSQL Database : Incorporate a NoSQL database to handle large volumes of semi-structured data, such as prices and other dynamic information.

Data Sharding: Implement data sharding techniques to horizontally partition data across multiple database instances. This strategy can distribute the database load and facilitate seamless scalability as the application grows.

Caching Mechanisms for Performance: Integrate caching mechanisms to improve performance and reduce the load on databases. Caching frequently accessed data can significantly enhance response times and overall system performance.

Replication for High Availability: Set up database replication to ensure high availability and fault tolerance. By replicating data across multiple nodes, the system can remain operational even in the event of hardware failures or other disruptions.

Indexing and Query Optimization: Implement indexing strategies to improve query performance and optimize database operations. Regularly analyze query execution plans and optimize queries for better performance.

Regular Database Maintenance and Monitoring: Schedule regular database maintenance tasks such as backups, data cleanup, and optimization. Implement robust monitoring solutions to track database performance, identify bottlenecks, and proactively address issues.

New proposed Design is in Schema direstory as Aviv_proposed_Design