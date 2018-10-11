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
        self.label = "Draw Area"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = []

        self.properties = [{
                            "name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "value": "100"
                            }
                            {
                            "name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "value": "100"
                            }
                           ]
        self.codes["function"] = """
static cairo_surface_t *surface = NULL;

static void clear_surface (void)
{
  cairo_t *cr;

  cr = cairo_create (surface);

  cairo_set_source_rgb (cr, 1, 1, 1);
  cairo_paint (cr);

  cairo_destroy (cr);
}

static gboolean configure_event_cb (GtkWidget         *widget,
                    GdkEventConfigure *event,
                    gpointer           data)
{
  if (surface)
    cairo_surface_destroy (surface);

  surface = gdk_window_create_similar_surface (gtk_widget_get_window (widget),
                                               CAIRO_CONTENT_COLOR,
                                               gtk_widget_get_allocated_width (widget),
                                               gtk_widget_get_allocated_height (widget));


  clear_surface ();

  return TRUE;
}


static gboolean
draw_cb (GtkWidget *widget,
         cairo_t   *cr,
         gpointer   data)
{
  cairo_set_source_surface (cr, surface, 0, 0);
  cairo_paint (cr);

  return FALSE;
}

static void
draw_brush (GtkWidget *widget,
            gdouble    x,
            gdouble    y)
{
  cairo_t *cr;

  cr = cairo_create (surface);

  cairo_rectangle (cr, x - 3, y - 3, 6, 6);
  cairo_fill (cr);

  cairo_destroy (cr);

  gtk_widget_queue_draw_area (widget, x - 3, y - 3, 6, 6);
}


static gboolean
button_press_event_cb (GtkWidget      *widget,
                       GdkEventButton *event,
                       gpointer        data)
{

  if (surface == NULL)
    return FALSE;

  if (event->button == GDK_BUTTON_PRIMARY)
    {
      draw_brush (widget, event->x, event->y);
    }
  else if (event->button == GDK_BUTTON_SECONDARY)
    {
      clear_surface ();
      gtk_widget_queue_draw (widget);
    }

  return TRUE;
}


static gboolean
motion_notify_event_cb (GtkWidget      *widget,
                        GdkEventMotion *event,
                        gpointer        data)
{
  if (surface == NULL)
    return FALSE;

  if (event->state & GDK_BUTTON1_MASK)
    draw_brush (widget, event->x, event->y);

  return TRUE;
}

static void
close_window (void)
{
  if (surface)
    cairo_surface_destroy (surface);
}


"""
        self.codes["declaration"] = """
   GtkWidget *$draw_area$_$id$;
   GtkWidget *$frame$_$id$;
"""

        self.codes["configuration"] = """
   *$frame$_$id$; = gtk_frame_new (NULL);
   gtk_frame_set_shadow_type (GTK_FRAME ($frame$_$id$), GTK_SHADOW_IN);
   gtk_container_add(GTK_CONTAINER(vbox), $frame$_$id$);


   $draw_area$_$id$ = gtk_drawing_area_new ();
   gtk_widget_set_size_request ($draw_area$_$id$, $prop[width]$, $prop[height]$);

   gtk_container_add (GTK_CONTAINER ($frame$_$id$), $draw_area$_$id$);

   g_signal_connect ($draw_area$_$id$, "draw", G_CALLBACK (draw_cb), NULL);
   g_signal_connect ($draw_area$_$id$,"configure-event",G_CALLBACK (configure_event_cb), NULL);


   g_signal_connect ($draw_area$_$id$, "motion-notify-event",G_CALLBACK (motion_notify_event_cb), NULL);
   g_signal_connect ($draw_area$_$id$, "button-press-event",G_CALLBACK (button_press_event_cb), NULL);

   gtk_widget_set_events ($draw_area$_$id$, gtk_widget_get_events ($draw_area$_$id$)| GDK_BUTTON_PRESS_MASK| GDK_POINTER_MOTION_MASK);
"""
