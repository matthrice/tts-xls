import requests
import xlrd
import string
import json
import sys
import os

CURR_PATH = os.path.abspath(os.curdir)
SETTINGS_PATH = os.path.join(CURR_PATH, 'settings.json')

VALID_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)

"""Read command line arguemnts"""
if len(sys.argv) < 2:
    print("Please enter input file argument")
    sys.exit(1)
infile = os.path.join(CURR_PATH, sys.argv[1])

try:
    outdir = os.path.join(CURR_PATH, sys.argv[2])
except:
    outdir = os.path.join(CURR_PATH, './output_files')
if not os.path.exists(outdir):
        os.makedirs(outdir)

"""Read settings file"""
try:
    info = json.load(open(SETTINGS_PATH))
except ValueError:
    print("Could not load settings.json")
    exit(1)


"""Read xls file"""
book = xlrd.open_workbook(infile)
phrase_list = book.sheet_by_index(0)
#nrows = phrase_list.nrows
nrows = 6

"""Synthesize text"""
i = 1
while i < nrows:
    text = phrase_list.row_values(i)[0]
    payload = {"accept": info["accept"],
               "text": text,
               "voice": info["voice"]}

    filename = ''.join(c for c in text if c in VALID_CHARS)[:30] + '.wav'

    r = requests.get(info["synth_url"],
                 auth=(info["username"], info["password"]),
                 params=payload)

    if r.status_code != 200:
        print("Bad text to speech request")
        exit(1)

    with open(os.path.join(outdir, filename), 'wb') as fd:
        for chunk in r.iter_content(1024):
            fd.write(chunk)
    i += 1




