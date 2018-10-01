#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Scale(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "gtk"
        self.help = "Not to declare"
        self.label = "Scale"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = []

        self.properties = [{"name": "orientation",
                            "label": "Orientation",
                            "type": MOSAICODE_COMBO,
                            "values": ["GTK_ORIENTATION_HORIZONTAL","GTK_ORIENTATION_VERTICAL"],
                            "value": "GTK_ORIENTATION_HORIZONTAL"
                            },
                            {"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "value": "0"
                            },
                            {"name": "lower",
                            "label": "Lower",
                            "type": MOSAICODE_FLOAT,
                            "value": "0"
                            },
                            {"name": "upper",
                            "label": "Upper",
                            "type": MOSAICODE_FLOAT,
                            "value": "100"
                            },
                            {"name": "step_increment",
                            "label": "Step Increment",
                            "type": MOSAICODE_FLOAT,
                            "value": "1"
                            },
                            {"name": "page_increment",
                            "label": "Page Increment",
                            "type": MOSAICODE_FLOAT,
                            "value": "10"
                            },
                            {"name": "page_size",
                            "label": "Page size",
                            "type": MOSAICODE_FLOAT,
                            "value": "10"
                            }
                           ]

        self.codes["declaration"] = """
   GtkWidget *$label$_$id$;
   GtkAdjustment *$label$_$id$_adjustment;
"""

        self.codes["configuration"] = """
   $label$_$id$_adjustment = gtk_adjustment_new($prop[value]$,
                    $prop[lower]$,
                    $prop[upper]$,
                    $prop[step_increment]$,
                    $prop[page_increment]$,
                    $prop[page_size]$);

   $label$_$id$ = gtk_scale_new($prop[orientation]$, $label$_$id$_adjustment);
   gtk_container_add(GTK_CONTAINER(vbox), $label$_$id$);
"""

