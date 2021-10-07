import gspread as gs


def create_new_spreadsheet(name: str):

    gc = gs.service_account(filename='meteors_client_secret.json')
    sheet = gc.create('{}'.format(name))

    #share to users
    sheet.share('m.p.milinski@gmail.com', perm_type='user', role='writer')


    sh = gc.open(name)

    # New sheets creation process
    sh.add_worksheet(title="Main_data", rows=1020, cols=12)
    sh.add_worksheet(title="Pivot_table", rows=350, cols=200)


    # Delete of first sheet in our worksheet
    sh.del_worksheet(sh.sheet1)

    return sheet


name = 'Meteors-analysis'
create_new_spreadsheet(name)













