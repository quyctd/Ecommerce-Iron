(function ($) {
    // USE STRICT
    "use strict";

        $(document).ready(function () {
        var icon = "../static/images/icons/icon-position-map.png";
        // The location of Shop
        var uluru = {lat: 21.0204386, lng: 105.8024246};
        // The map, centered at Shop
        var map = new google.maps.Map(
            document.getElementById('google_map'), {zoom: 15, center: uluru});
        // The marker, positioned at Shop
        var marker = new google.maps.Marker({position: uluru, map: map, icon: icon});
        });

})(jQuery);