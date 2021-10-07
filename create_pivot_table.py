from main import creds, key
from googleapiclient.discovery import build

service = build('sheets', 'v4', credentials=creds)



SAMPLE_SPREADSHEET_ID = key
source_sheet_id = "1612700398"
destination_sheet_id = "1582392283"



request_body = {
    'requests': [
        {
            'updateCells': {
                'rows': {
                    'values': [
                        {
                            'pivotTable': {
                                #Data Source
                                'source': {
                                    'sheetId': source_sheet_id,
                                    'startRowIndex': 1,
                                    'startColumnIndex': 0,
                                    'endRowIndex': 972,
                                    'endColumnIndex': 11,
                                },
                                #Row Field(s)
                                'rows': [
                                    #field #1
                                    {
                                        'sourceColumnOffset': 3,

                                        'sortOrder': 'ASCENDING',
                                        'repeatHeadings': True,
                                        'label': 'Meteor Class'
                                    }
                                ],
                                #Column Field(s)
                                'columns': [
                                    #column field #1
                                    {
                                        'sourceColumnOffset': 6,
                                        'sortOrder': 'ASCENDING',

                                        'label': "Year"

                                    }
                                ],

                                #Values Field(s)
                                'values': [
                                    #value field #1
                                    {
                                        'sourceColumnOffset': 5,
                                        'summarizeFunction': 'COUNTA',
                                        'name': 'COUNTA of Class'

                                    }
                                ],

                                'valueLayout': 'HORIZONTAL'
                            }
                        }
                    ]
                },
                'start': {
                    'sheetId': destination_sheet_id,
                    'rowIndex': 3,
                    'columnIndex': 1,

                },
                'fields': 'pivotTable'

            }
        }
    ]
}

response = service.spreadsheets().batchUpdate(
    spreadsheetId=SAMPLE_SPREADSHEET_ID,
    body=request_body
).execute()