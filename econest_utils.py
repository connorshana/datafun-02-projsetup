
''' This module provides a reusable byline for the author's services. '''
import math
import statistics

company_name: str = "EcoNest Consultants."
count_number_of_consultants: int = 50
has_many_collaborators: bool = True
average_client_ratings: float = 8.8
services_offered: list = ["Environmental Data Analysis", "Ecological Consulting"]
client_ratings: list = [8.5, 9, 8, 10, 8.5]
number_of_consultants_string: str = f"Number of Consultants: {count_number_of_consultants}"
many_collaborators_string: str = f"Many Collaborators: {has_many_collaborators}"
client_ratings_string: str = f"Average Client Ratings: {average_client_ratings}"

least= min(client_ratings)
greatest= max(client_ratings)
total= sum(client_ratings)
count= len(client_ratings)
mean= statistics.mean(client_ratings)
mode= statistics.mode(client_ratings)
median= statistics.median(client_ratings)
standard_deviation=statistics.stdev(client_ratings)

stats_string: str = f"""
Descriptive Statistics Client Ratings:
    Least: {least}
    Greatest: {greatest}     
    Total: {total}
    Count: {count}
    Mean: {mean}
    Mode: {mode}
    Median: {median}
    Standard Deviation: {standard_deviation}
"""
byline: str = f"""
{company_name}
{number_of_consultants_string}
{many_collaborators_string}
{client_ratings_string}
{services_offered}
{stats_string}
"""
def main():
    ''' Display all output'''
print(company_name)
print(number_of_consultants_string)
print(many_collaborators_string)
print(client_ratings_string)
print(services_offered)
print(stats_string)

    # If all of the above works, then the byline should work too:
print(byline)
if company_name == '_main_':
    main()
    