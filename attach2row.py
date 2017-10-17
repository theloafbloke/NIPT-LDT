# Install the smartsheet sdk with the command: pip install smartsheet-python-sdk
import smartsheet
import logging

# TODO: Set your API access token here, or leave as None and set as environment variable "SMARTSHEET_ACCESS_TOKEN"
access_token = '276xti64p303m1pchqhab4fzrw'

# TODO: Update this with the ID of your sheet to update
sheet_id = '4793023683946372'

# The API identifies columns by Id, but it's more convenient to refer to column names. Store a map here
column_map = {}


# Helper function to find cell in a row
def get_cell_by_column_name(row, column_ame):
    column_id = column_map[column_ame]
    return row.get_column(column_id)

print("Starting ...")

# Initialize client
ss = smartsheet.Smartsheet(access_token)
# Make sure we don't miss any error
ss.errors_as_exceptions(True)
logging.basicConfig(filename='mylog.log', level=logging.INFO)

# Load entire sheet
sheet = ss.Sheets.get_sheet(sheet_id)

print ("Loaded " + str(len(sheet.rows)) + " rows from sheet: " + sheet.name)

# Build column map for later reference - translates column names to column id
response = ss.Attachments.list_all_attachments(sheet_id, include_all=True)

print response



print ("Done")
