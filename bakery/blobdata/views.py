# coding: utf-8
# Copyright 2013 The Font Bakery Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# See AUTHORS.txt for the list of Authors and LICENSE.txt for the License.

import os
from flask import Blueprint, request, json, current_app, g
from ..models import Project, ProjectBuild

blobdata = Blueprint('data', __name__, static_folder=current_app.config.get('DATA_ROOT'))

# @blobdata.route('/font/<int:project_id>.png')
# def font(project_id):
#     p = Project.query.filter_by(
#         login=g.user.login, id=project_id).first_or_404()

#     b = ProjectBuild.query.filter_by(project=p).order_by("id desc").first()
#     if not b:
#         p.make_build(revision='HEAD')
#         send_from_directory(current_app.static_folder, 'empty.png')

# @blobdata.route('/data/<path:file>')
# def static_from_root():
#     # Static items
#     return send_from_directory(current_app.static_folder, request.path[1:])

#     from PIL import ImageFont, ImageDraw

#     draw = ImageDraw.Draw(image)

#     # use a truetype font
#     font = ImageFont.truetype("arial.ttf", 15)

#     draw.text((10, 25), "world", font=font)

