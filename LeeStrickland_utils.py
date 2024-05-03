'''Lee Strickland 44608
This module provides a reusable byline for the author's services.'''

import math
import statistics

def main():

    #Define Variables
    company_name: str = 'Grateful Analytics LLC'
    company_description: str = 'Data Analytics consulting company working hard for you'
    company_founding_year: int = 2024
    company_city: str = 'Kansas City'
    company_state: str = 'Missouri'
    company_number_employees: int = 5
    has_international_presence: bool = True
    employee_benefits: list = ['Insurance', 'Flexable Schedule', 'Matching Retirement']
    services_offered: list = ['Data Analysis', 'Machine Learning Consulting', 'Business First Data Reviews']
    customer_satisfaction: float = 9.8
    service_pricing: list = [350, 850, 100]

# Multiline string with byline using f-string formatting
    byline: str = f"""
    Information:
    Name: {company_name}
    Description: {company_description}
    Founded: {company_founding_year}
    City: {company_city}
    State: {company_state}
    Number of Employees: {company_number_employees}
    International: {has_international_presence}
    Employee Benefits: list = ['Insurance', 'Flexable Schedule', 'Matching Retirement']
    Services Offered: list = ['Data Analysis', 'Machine Learning Consulting', 'Business First Data Reviews']
    Customer Satisfaction: {customer_satisfaction} Out of 10!
    """

#Prices for services offered
    stats_string: str = f"""
    Services with Pricing:
    Services Offered: {services_offered}
    Service Prices: {service_pricing}
    Maximum Service Price: {max(service_pricing)}
    Minimum Service Price: {min(service_pricing)}
    Mean Service Price: {statistics.mean(service_pricing)}
    Median Service Price: {statistics.median(service_pricing)}
    Standard Deviation of Service Price: {statistics.stdev(service_pricing)}
    """

    print(byline)
    
# Call the main function to execute the code
if __name__ == '__main__':
        main()
