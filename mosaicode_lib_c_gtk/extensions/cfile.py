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
        self.code_parts = ["function", "declaration", "configuration"]
        self.code = r"""
#include <gtk/gtk.h>

void destroy(void){
   gtk_main_quit ();
}

$code[function]$

int main(int argc, char *argv[]){
   GtkWidget *window;
   GtkWidget *vbox;
   $code[declaration]$

   gtk_init(&argc, &argv);

   window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
   g_signal_connect(window, "destroy",G_CALLBACK(destroy), NULL);
   gtk_window_resize(window, 800, 600);

   vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL,3);
   gtk_container_add(GTK_CONTAINER(window), vbox);

   $code[configuration]$
   $connections$
   //gtk_container_add(GTK_CONTAINER(vbox), botao);

   gtk_widget_show_all(window);
   gtk_main();
   return 0;
}
"""

# -------------------------------------------------------------------------
