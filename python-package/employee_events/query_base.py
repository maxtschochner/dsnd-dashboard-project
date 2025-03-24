# Import any dependencies needed to execute sql queries
from sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = "" # Can either be 'team' or 'employee'

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return list()


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        query_string = f'SELECT COUNT(positive_events), COUNT(negative_events) FROM {name} JOIN employee_events GROUP BY event_date ORDER BY event_date'

        # Examples
        # from sqlite3 import connect
        # mycon = connect('employee_events.db')
        # mycur = mycon.cursor()
        # print(mycur.execute("SELECT event_date, team.team_id FROM team JOIN employee_events ON team.team_id=employee_events.team_id LIMIT 10").fetchall())

        self.pandas_query(query_string)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

