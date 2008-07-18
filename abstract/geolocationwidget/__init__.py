from config import *
from Products.CMFCore.DirectoryView import registerDirectory

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    registerDirectory(SKINS_DIR, GLOBALS)