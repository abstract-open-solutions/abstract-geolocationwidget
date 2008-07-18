return """
<script type="text/javascript">
var map = null;
var geocoder = null;
var id_field_div = null;
var id_field_input = null;

function setElem(v1, v2){
    id_field_div = v1;
    id_field_input = v2
}

function showAddress(address, obj) {
  geocoder = new GClientGeocoder();
  setElem(obj, address);
  if (geocoder) {
    geocoder.getLocations(document.getElementById(address).value, myHandler);
 }
};

function myHandler(response){
    var i = 0;
    var field = document.getElementById(id_field_div);
    if (document.getElementById('suggestion')){ 
        field.removeChild(document.getElementById('suggestion'));
    }
    try{
        var elem = document.createElement('div'); elem.id = 'suggestion';
        field.appendChild(elem);
        for(i=0; i < response.Placemark.length; i++){
            a = document.createElement('div');
            a.className = 'map_suggestion';
            a.setAttribute('pos', i);
            a.onmouseover = function(){
                    this.style.backgroundColor='#00FFFF';
            };
            a.onmouseout = function(){
                this.style.backgroundColor='#fff';
            }
            a.onclick = function(){
                pos = this.getAttribute('pos');
                place = response.Placemark[pos];
                document.getElementById(id_field_input).value=place.Point.coordinates[1]+";"+place.Point.coordinates[0]+"|"+place.address;
                elem.style.display = "none";
            }
            place = response.Placemark[i];
            a.appendChild(document.createTextNode(place.address));
            elem.appendChild(a);
        }
    }
    catch(error) {
        if (document.getElementById('suggestion')){ 
            field.removeChild(document.getElementById('suggestion'));
        }
        a = document.createElement('div');
        a.id = 'suggestion';
        a.className = 'empty_info';
        a.appendChild(document.createTextNode("Nessun risultato"));
        field.appendChild(a);
    }
};
registerEventListener(window, 'unload', GUnload);
</script>

"""