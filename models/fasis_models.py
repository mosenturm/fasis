# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# table definition for FASIS
#
# Name: fasis_models.py
# Author: Andreas Kaiser
# Email: kaiser.vocote@gmail.com
# Version: 0.0.1
# Date: 2016-10-15
#
# ---------------------------------------------------------------------

db.define_table(
    'cust_categories',
    Field('name', 'string', label=T('Cat.-name')),
    format = '%(name)s',
    singular=T("Categorie"), plural=T("Categories"))

db.define_table(
    'cust_types',
    Field('name', 'string', label=T('Typename')),
    format = '%(name)s',
    singular=T("Type"), plural=T("Types"))

#  `cust_name` varchar(100) NOT NULL,
#  `cust_contact` varchar(100) DEFAULT NULL,
#  `street` varchar(100) DEFAULT NULL,
#  `city` varchar(100) DEFAULT NULL,
#  `zip` varchar(20) DEFAULT NULL,
#  `email` varchar(100) DEFAULT NULL,
#  `website` varchar(100) DEFAULT NULL,
#  `telefon` varchar(50) DEFAULT NULL,
#  `mobile_phone` varchar(50) DEFAULT NULL,
#  `fax` varchar(50) DEFAULT NULL,
#  `note` text,
#  `category_id` int(11) NOT NULL DEFAULT '0',
#  `type_id` int(11) NOT NULL,
#  PRIMARY KEY (`id`),
#  KEY `category_id` (`category_id`),
#  KEY `type_id` (`type_id`),
#  KEY `cust_contact` (`cust_contact`),
#  KEY `website` (`website`)
db.define_table(
    'customer',
    Field('cust_name', 'string', label=T('Name')),
    Field('cust_contact', 'string', label=T('Contact')),
    Field('street', 'string', label=T('street')),
    Field('city', 'string', label=T('city')),
    Field('zip', 'string', label=T('zipcode')),
    Field('email', 'string'),
    Field('website', 'string'),
    Field('telefon', 'string'),
    Field('mobile_phone', 'string', label=T('mobile_phone')),
    Field('fax', 'string'),
    Field('note', 'text', label=T('note')),
    Field('category_id', db.cust_categories, label=T('Categorie')),
    Field('type_id', db.cust_types, label=T('Type')),
    format = '%(cust_name)s',
    singular=T("Customer"), plural=T("Customers"))


db.cust_categories.name.requires = IS_NOT_EMPTY()
db.cust_types.name.requires = IS_NOT_EMPTY()
