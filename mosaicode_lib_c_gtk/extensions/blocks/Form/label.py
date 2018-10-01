#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Label(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "gtk"
        self.help = "Not to declare"
        self.label = "Label"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = []

        self.properties = [{"name": "label",
                            "label": "Label",
                            "type": MOSAICODE_STRING,
                            "value": "Label"
                            }
                           ]

        self.codes["function"] = """
"""

        self.codes["declaration"] = """
   GtkWidget *$label$_$id$;
"""

        self.codes["configuration"] = """
   $label$_$id$ = gtk_label_new("$prop[label]$");
   gtk_container_add(GTK_CONTAINER(vbox), $label$_$id$);
"""

