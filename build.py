#!/usr/bin/env python

# Creates zip archive for Google Market extension deployment

import os
import os.path
import re
import json

# ---

SRC_PATH = './sources'
MANIFEST_FILE = SRC_PATH + '/manifest.json'
BUILD_PATH = './versions'
ZIP_COMMAND = "7za a -tzip -r -xr!.svn* {dest} {source}"
ZIP_NAME = "{name}_{version}.zip"

# ---

def get_manifest_details():
	print("Reading manifest file [%s]..." % MANIFEST_FILE)
	with open(MANIFEST_FILE, "rt") as f:
		manifest = json.load(f)
		return manifest["name"], manifest["version"]

def get_cmd():
	name, version = get_manifest_details()
	print("Extension name: %s\nVersion: %s" % (name, version))
	zip_name = ZIP_NAME.format(name=name.lower(), version=version)
	return ZIP_COMMAND.format(source=os.path.join(SRC_PATH, '*'),
		dest=os.path.join(BUILD_PATH, zip_name))


if(not os.path.exists(BUILD_PATH)):
    os.makedirs(BUILD_PATH)

cmd = get_cmd()
print("Command: " + cmd)
os.system(cmd)
