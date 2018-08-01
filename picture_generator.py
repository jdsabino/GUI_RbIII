import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf
import matplotlib.pyplot as plt

def generate_pic(filename, factor=1, title=""):
    '''
    filename: the name of the file to be imported
    factor: rescaling factor
    title: title to be shown with the picture
    Returns: Gtk.Image
    
    A image file is imported with picbuf, it is manipulated
    and then transformed into a Gtk.Image object. The main 
    purpose is to generate pictures of plots, so the matplotlib
    is used to set the kind of plot as well as axis and title.
    '''


    ### TODO
    #read pic
    #load picbuf
    #rescale
    #generate Gtk.Image
    #
    
