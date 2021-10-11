def create_new_spreadsheet(name: str, gc):
    """Function responsible for creation of brand new spreadsheet
    :param name: variable consist of given spreadsheet name
    :param gc: variable for storing credentials for service (located in files/main.py)

    """
    sheet = gc.create('{}'.format(name))

    # share to users
    sheet.share('m.p.milinski@gmail.com', perm_type='user', role='writer')

    sh = gc.open(name)

    # New sheets creation process
    sh.add_worksheet(title="Main_data", rows=1020, cols=12)
    sh.add_worksheet(title="Pivot_table", rows=350, cols=200)

    # Delete of first sheet in our worksheet
    sh.del_worksheet(sh.sheet1)

    return sheet, gc
