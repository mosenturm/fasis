# -*- coding: utf-8 -*-

response.menu = [[T('Register Category'), False, URL('register_cust_categorie')],
                 [T('Register Type'), False, URL('register_cust_type')],
                 ['Buy product', False, URL('buy')]]

def register_cust_categorie():
    # create an insert form from the table
    form = SQLFORM(db.cust_categories).process()

    # if form correct perform the insert
    if form.accepted:
        response.flash = T('new record inserted')

    # and get a list of all persons
    records = SQLTABLE(db().select(db.cust_categories.ALL),headers='fieldname:capitalize')

    return dict(form=form, records=records)

# Versuchen Sie so etwas wie
def index():
    return dict(message="hello from fasis.py")
