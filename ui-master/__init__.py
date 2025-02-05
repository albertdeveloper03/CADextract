# Copyright (C) 2021  Beate Scheibel
# This file is part of DigiEDraw.
#
# DigiEDraw is free software: you can redistribute it and/or modify it under the terms
# of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
#
# DigiEDraw is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# DigiEDraw.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask

    #app = Flask(__name__)
app = Flask(__name__, static_url_path="", static_folder="static")
app.debug = True
    #app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

