# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate


class CFile(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "gtk"
        self.language = "c"
        self.description = "A full template to generate gtk code"
        self.extension = ".c"
        self.command = "g++ -o $dir_name$$filename$ $dir_name$$filename$$extension$ `pkg-config --cflags --libs gtk+-3.0`\n"
        self.command += "$dir_name$./$filename$"
        self.code_parts = ["destroy","windows","function", "declaration", "configuration","show","struct","callback"]
        self.code = r"""
#include <gtk/gtk.h>

$code[struct]$

$code[destroy]$

$code[function]$

$code[callback]$

int main(int argc, char *argv[]){
	

	GtkWidget *vbox;
	$code[declaration]$

	gtk_init(&argc, &argv);
	
	vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL,3);
	$code[windows]$	


  $code[configuration]$
  $connections$

  $code[show]$
  gtk_main();
  return 0;
}
"""

# -------------------------------------------------------------------------
