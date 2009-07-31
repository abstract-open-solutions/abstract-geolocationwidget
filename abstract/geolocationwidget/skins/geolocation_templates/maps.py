from Products.CMFCore.utils import getToolByName

root = getToolByName(context, 'portal_url')
root = root.getPortalObject()
google_key_d = root.getProperty("gmap_key", "no key")
try:
    print 'ciao'
    google_keys = eval(google_key_d)
    google_key = google_keys[root.absolute_url()]
except:
    print 'bla'
    google_key = google_key_d
    
return google_key