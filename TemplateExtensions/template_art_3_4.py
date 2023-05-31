#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Juan Pablo G.C. <juanpablogc@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
Generic template functionality controlled by the INX file.
"""

import inkex


class Document(inkex.TemplateExtension):
    """Create an empty Document (in mm)"""

    multi_inx = True

    def add_arguments(self, pars):
        pars.add_argument(
            "-a",
            "--aspect_ratio",
            type=str,
            default="6|8",
            help="Aspect ratio (width:height)",
        )
        pars.add_argument(
            "-or",
            "--orint",
            type=int,
            default=0,
            help="Orientation (0:Portrait,1:Landscape)",
        )

    def get_size(self):
        # Dimensions in mm
        aspect_ratio = self.options.aspect_ratio
        orientation = self.options.orint

        s_width_ratio, s_height_ratio = aspect_ratio.split('|')
        
        width_ratio = int(s_width_ratio)
        height_ratio = int(s_height_ratio)

        if orientation == 1:
            width_ratio =  int(s_height_ratio)
            height_ratio =  int(s_width_ratio)

        return (width_ratio*10.0, "mm", height_ratio*10.0, "mm")

    def set_namedview(self, width, height, unit):
        super(Document, self).set_namedview(width, height, unit)
        namedview = self.svg.namedview
        


if __name__ == "__main__":
    Document().run()