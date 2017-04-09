from RFHistory.settings import ROBOT_OUTPUT_PATH

import os
import uuid
import json


def handle_uploaded_file(file):
    file_name = str(uuid.uuid4())
    os.makedirs(ROBOT_OUTPUT_PATH, exist_ok=True)
    _create_info_file(file_name)
    _create_output_file(file, file_name)


def _create_info_file(file_name):
    data = { "status":"received", "output":file_name+'.xml' }
    with open(os.path.join(ROBOT_OUTPUT_PATH, file_name + '.json'), 'w') as file:
        json.dump(data, file)


def _create_output_file(file, file_name):
    with open(os.path.join(ROBOT_OUTPUT_PATH, file_name + '.xml'), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
