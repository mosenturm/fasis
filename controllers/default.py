# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

response.menu += [[T('Register Category'), False, URL('register_cust_categorie')],
                 [T('Register Type'), False, URL('register_cust_type')],
                 [T('Customers'), False, URL('manage_customers')],
                 [T('TestDT'), False, URL('manage_customers_DT')]]

def register_cust_categorie():
    grid = SQLFORM.smartgrid(db.cust_categories, 
                             user_signature=False, 
                             buttons_placement='left',
                             links_placement='right')
    return dict(grid=grid)


def register_cust_type():
    grid = SQLFORM.smartgrid(db.cust_types, 
                             user_signature=False,
                             buttons_placement='left',
                             links_placement='right')
    return dict(grid=grid)


def manage_customers():
    grid = SQLFORM.smartgrid(db.customer, 
                             linked_tables=['cust_types','cust_categories'],
                             divider=' -> ', 
                             user_signature=False,
                             buttons_placement='left',
                             links_placement='right',
                             formstyle='bootstrap3_stacked')
    return dict(grid=grid)

def manage_customers_DT():
    import json
    # Select all the records, to show how
    # datatables.net paginates.
    # Rows can't be serialized because they contain a reference to
    # an open database connection. Use as_list()
    # to serialize the query result.
    customer = json.dumps(db(db.customer).select().as_list())
    # Convert to XML for DataTable
    return dict(results=XML(customer), message='DataTable in Benutzung')  
  
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    #return dict(message=T('Welcome to web2py!'))
    return dict(message="Hello FASIS!")


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
