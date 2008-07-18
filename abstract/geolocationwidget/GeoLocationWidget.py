from AccessControl import ClassSecurityInfo
from Products.Archetypes.public import StringWidget
from Products.Archetypes.Registry import registerWidget

class GeoLocationWidget(StringWidget):
    
    _properties = StringWidget._properties.copy()
    _properties.update({
        'macro' : "geolocation",
        'helper_css': ('geolocation_widget.css',),
    })
    
    security = ClassSecurityInfo()

registerWidget(GeoLocationWidget,
               title='GeoLocation',
               description="Text field for geolocation by google maps api.",
               used_for=('Products.Archetypes.public.StringField',)
               )
