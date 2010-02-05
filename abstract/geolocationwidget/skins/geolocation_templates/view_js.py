## Script (Python) "view_js"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters= result=None
##title=
##

map_center = (0,0)
x = 0
y = 0

sMarker = ""
if result:
    #map_center = result
    if result.split('|'):
        point_coord = result.split('|')[0];
        coord = point_coord.split(';');
        x = coord[0]
        y = coord[1]
        x = float(x)
        y = float(y)
    except:
        x = float(0)
        y = float(0)
    sMarker = """
var point = new GLatLng(parseFloat(%f), parseFloat(%f));
var marker = new GMarker(point);
/*
GEvent.addListener(marker, "click", function() {
  var html = '<div style="width: 210px; padding-right: 10px"><a href="./signup.html">Sign up<\/a> for a Google Maps API key, or <a href="./documentation/index.html">read more about the API<\/a>.<\/div>';
  marker.openInfoWindowHtml(html);
});
*/
map2.addOverlay(marker);
/* GEvent.trigger(marker, "click"); */
""" % (x, y)

return """
<script type="text/javascript">
function initialize() {
    if (GBrowserIsCompatible()) {
        var map2 = new GMap2(document.getElementById("mapView"));
        map2.addControl(new GLargeMapControl3D());
        map2.addControl(new GMapTypeControl());
        <!-- map2.addControl(new GOverviewMapControl()); -->
        map2.setCenter(new GLatLng(%(lat)f, %(lng)f), 8, G_HYBRID_MAP);
        %(marker)s
    }
    else window.alert("Google maps aren't compatible with current Browser.");
}

registerPloneFunction(initialize);
registerEventListener(window, 'unload', GUnload);
</script> """ % {
                  'lat'     : x,
                  'lng'     : y,
                  'marker'  : sMarker,
                }