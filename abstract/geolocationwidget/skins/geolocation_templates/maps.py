from Products.CMFCore.utils import getToolByName

root = getToolByName(context, 'portal_url')
root = root.getPortalObject()

google_key_d = root.getProperty("gmap_key", "no key")
#key1=abcd,key2=abcd
try:
    google_keys_arr = google_key_d.split(',')
    google_keys = dict([entry.split('=') for entry in google_keys_arr])
    google_key = google_keys[root.absolute_url()]
except:
    google_key = google_key_d
    
return google_key
