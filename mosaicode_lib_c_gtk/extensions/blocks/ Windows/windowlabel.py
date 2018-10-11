#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Button(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "gtk"
        self.help = "Not to declare"
        self.label = "Windows Label"
        self.color = "250:150:150:150"
        self.group = "Windows"
        self.ports = []

        self.properties = [{"name": "label",
                            "label": "Label",
                            "type": MOSAICODE_STRING,
                            "value": "Label"
                            }
                           ]
        self.codes["function"] = """
void destroy_$id$(void){
  	gtk_main_quit ();
}


"""

        self.codes["declaration"] = """
	GtkWidget *window_$id$;	
"""

        self.codes["windows"] = """
	window_$id$ = gtk_window_new(GTK_WINDOW_TOPLEVEL);
	gtk_window_set_title(GTK_WINDOW(window_$id$),"$prop[label]$"); 				
	g_signal_connect(window_$id$, "destroy",G_CALLBACK(destroy_$id$), NULL);
	gtk_window_resize(GTK_WINDOW(window_$id$), 800, 600);
	gtk_container_add(GTK_CONTAINER(window_$id$), vbox);
"""

        self.codes["show"] = """
   	gtk_widget_show_all(window_$id$);

"""
