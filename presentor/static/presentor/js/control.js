// add the neccessary ui elements to navbar menu
$(".menuitem.control").show();


var current_slide = 0;
var slidecount = 0;
var slidetitle = "";
var controls_loaded = false;
var showid = 0;
var newDetails = 1;
 
if (sess === null ){
    var all_connected = false;
    var all_connected_reported = false;
    var wsuri;
    if (window.location.protocol === "file:") {
        wsuri = "ws://192.168.1.106:9000";
    } else {
        wsuri = "ws://" + window.location.hostname + ":9000";
    }

    // connect to WAMP server
    ab.connect(wsuri,
        // WAMP session was established
        function (session) {
        sess = session;
        console.log("Connected to " + wsuri);
        sess.subscribe("http://192.168.1.106/messages", onEvent);
        publishCommand("controller_connected");
        setTimeout(function() {
            alertConnection(); 
        }, 500);
        },

        // WAMP session is gone
        function (code, reason) {
            sess = null;
            if (code == ab.CONNECTION_UNSUPPORTED) {
            window.location = "http://autobahn.ws/unsupportedbrowser";
            } else {
            console.log(reason);
            all_connected = false;
            all_connected_reported = false;
            showAlert(reason, "warning");
            }
        }
    );
} else {
    // we still have a session going but we just logged back in
    publishCommand("controller_connected");
}

function alertConnection() {
    console.log("this is a test");
    if( all_connected === false ){
        showAlert("Display and cotroller not connected.", "warning");
    } else if (all_connected_reported === false){
        showAlert("Connected and ready.", "success");
        all_connected_reported = true;
    }
}
 
function publishCommand(command, data) {
   sess.publish("http://192.168.1.106/messages", {'command': command, 'data': data});
}

function onEvent(topicUri, event) {
    if (event.command === "error"){
        showAlert(event.data, "warning");
    }
    if (event.command === "message"){
        showAlert(event.data);
    }
    if (event.command === "slideInfo"){
        if (all_connected === false){
            alertConnection();
            all_connected = true;
        }
        // if any of the info is new run slidebuttons otherwise do nothing
        if ( controls_loaded === false || showid !== event.data.id) {
            slidecount = event.data.count;
            slidetitle = event.data.title;
            current_slide = event.data.current_slide;
            showid = event.data.id;
            loadControls(showid);
        } else if ( slidecount !== event.data.count || current_slide !== event.data.current_slide){
            slidecount = event.data.count;
            slidetitle = event.data.title;
            current_slide = event.data.current_slide;
            slideButtons();
        }
        $("#main").show();
    }
    if (event.command === "showlist"){
        all_connected = true;
        showAlert("Connected & Ready. Select a slideshow.", "success");
        all_connected_reported = true;
        loadSlideList();
    }
}

function playSlideshow(id) {
    loadControls(id);
    publishCommand("playSlideshow", id );
}

// fetch the controls but wait until we hear back from show to unhide
function loadControls(id) {
    $("#main").hide();
    showid = id;
    controls_loaded = true;
    $("#main").load("/presentor/control/" + id, function(){
        slideButtons();
    });
    $(".menuitem.control").show();
}

// activate deactivate the buttons and write the count
function slideButtons() {
    if (current_slide > 1 ){
        activateButton("previous", "previousSlide" );
    } else {
        deactivateButton("previous");
    }
    if (current_slide <= slidecount){
        activateButton('next', "nextSlide");
    } else {
        deactivateButton('next');
    }
    if (current_slide > slidecount){
        $('#slideshowInfo').html("End of " + slidetitle );
    } else {
        showSlideCount();
    }
}

function showSlideCount(){
    $('#slideshowInfo').html(slidetitle + ' (<span id="current_slide">' + current_slide + '</span>/' + slidecount + ")");        
}
function activateButton(buttonId, command){
    $('#'+buttonId+' i').removeClass('disabled');
    $('#'+buttonId).attr('onclick', "publishCommand('" + command+ "')");
}
function deactivateButton(buttonId){
    $('#'+buttonId+' i').addClass('disabled');
    $('#'+buttonId).attr('onclick', "return null;");
}

function loadSlideList(){
    $("#main").load("/presentor/listslideshows", function(){
        // hide the menu link for now active page
        $("#showlist").parent().hide();
    });
}
