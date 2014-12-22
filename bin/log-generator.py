#!/usr/bin/env python

"""
Author: Peter Salas
Project Name: Log Generator
Date: 07/18/2014
Description:

    This is a very quick model generator for the purpose of this demo.
    The script generates a log file of 1000 - 100000 lines, with
    a random distribution of response codes, and appropriate
    error messages.
"""

from time import sleep
from datetime import datetime
from random import randrange
import sys

## Create a reasonable distribution of response codes
response_codes = {'200':80, '302':0, '400':0, '401':0, '404':0, '415':0, '500':100}
total = randrange(60,101)
response_codes['200'] = total
rand_num = randrange(2)
total += rand_num
response_codes['302'] = total
if total < 100:
    rand_num = randrange(100 - total)
    total += rand_num
    response_codes['400'] = total
if total < 100:
    rand_num = randrange(100 - total)
    total += rand_num
    response_codes['401'] = total
if total < 100:
    rand_num = randrange(100 - total)
    total += rand_num
    response_codes['404'] = total
if total < 100:
    rand_num = randrange(100 - total)
    total += rand_num
    response_codes['415'] = total

## For dubugging purposes only to make sure creating reasonable distribution
print "# %s" % (response_codes)

## Map the codes to certain methods
codes_map = {
    '200':['GET', 'POST', 'PUT', 'DELETE'],
    '302':['GET'],
    '400':['GET','POST', 'PUT'],
    '401':['GET', 'PUT', 'DELETE'],
    '404':['GET','DELETE'],
    '415':['GET', 'POST', 'PUT'],
    '500':['GET', 'POST', 'PUT', 'DELETE']}

## Map the methods and codes to a finite list of messages
message_map = {
    'GET':    { '200': [ 'Successfully found account', 'Successfully found accounts', 'Login page loaded', 'Directory listing page', 'Dashboard found' ],
                '302': [ 'Redirect' ],
                '400': [ 'Account balance too low', 'Invalid JSON', 'Missing Account ID', 'Missing Transaction ID' ],
                '401': [ 'Unauthorized' ],
                '404': [ 'Account does not exist', 'Object not found', 'Not Found' ],
                '415': [ 'Method not allowed' ],
                '500': [ 'Unknown server error' ]},
    'POST':   { '200': [ 'Successfully authenticated' ],
                '400': [ 'Invalid user/password credentials', 'Account does not exist' ],
                '415': [ 'Method not allowed' ],
                '500': [ 'Unknown server error', 'Nullpointer Exception', 'Illegal Division by zero', 'Cannot convert Boolean to Integer' ]},
    'PUT':    { '200': [ 'Successfully created/updated account', 'Token Generated' ],
                '400': [ 'Invalid JSON', 'Missing Transaction ID', 'Missing Account ID', 'Invalid user/password credentials', 'Account does not exist' ],
                '401': [ 'Unauthorized' ],
                '415': [ 'Method not allowed' ],
                '500': [ 'Unknown server error', 'Nullpointer Exception', 'Malformed JSON', 'Cannot convert String to Integer' ]},
    'DELETE': { '200': [ 'Successfully deleted account' ],
                '401': [ 'Unauthorized' ],
                '404': [ 'Account does not exist', 'Transaction does not exist' ],
                '500': [ 'Unknown server error' ]}}

###############################################################################
# Data Generation Methods
###############################################################################

def generate_ip():
    return "%s.%s.%s.%s" % (10, 10, randrange(255), randrange(255))

def generate_time():
    sleep (2.0/float(randrange(1,22)))
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') 

def generate_code():
    rand_num = randrange(100)
    if rand_num < response_codes['200']:
        return 200
    elif rand_num >= response_codes['200'] and rand_num < response_codes['302']:
        return 302
    elif rand_num >= response_codes['302'] and rand_num < response_codes['400']:
        return 400
    elif rand_num >= response_codes['400'] and rand_num < response_codes['401']:
        return 401
    elif rand_num >= response_codes['401'] and rand_num < response_codes['404']:
        return 404
    elif rand_num >= response_codes['404'] and rand_num < response_codes['415']:
        return 415
    else:
        return 500

def generate_method(code):
    methods = codes_map[str(code)]
    return methods[randrange(len(methods))]

def generate_message(code, method):
    messages = message_map[method][str(code)]
    return messages[randrange(len(messages))]

###############################################################################
# Main
#
# Description:  Generate between 800 and 5000 log lines
###############################################################################

for x in range(0, randrange(800,5001)):
    code = generate_code()
    method = generate_method(code)
    message = generate_message(code, method)

    print "%s %s %s %s \"%s\"" % (
            generate_ip(), 
            generate_time(),
            code,
            method,
            message)

    sys.stdout.flush()
