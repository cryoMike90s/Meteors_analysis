def pivot_table_creation(key, gc, working_spreadsheet, service):
    """
    Function that provide creation of pivot table from first sheet data
    :param key: actual worksheet id (defined in console.py)
    :param gc: variable for storing credentials for service (located in files/main.py)
    :param working_spreadsheet: actual worksheet instance (defined in console.py)
    :param service: Google Sheet API instance (located in files/main.py)

    `request_body`: structure from https://developers.google.com/sheets/api/samples/pivot-tables
    """
    worksheet_list = working_spreadsheet.worksheets()
    source_sheet_id = str(worksheet_list[0].id)
    destination_sheet_id = str(worksheet_list[1].id)
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

    service.spreadsheets().batchUpdate(
        spreadsheetId=key,
        body=request_body
    ).execute()