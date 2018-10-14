// Initialize selector drop-downs
$(document).ready(function(){
    $('select').formSelect();
});

// plz no hack
const apiKey = "AIzaSyChPUazt0gK4qMjVJDpo8hPE49QAUfZW4w";

// Set endpoints
const endpoints = {
  translate: "",
  detect: "detect",
  languages: "languages"
};

// Abstract API request function
function makeApiRequest(endpoint, data, type) {
  url = "https://www.googleapis.com/language/translate/v2/" + endpoint;
  url += "?key=" + apiKey;

  // If not listing languages, send text to translate
  if (endpoint !== endpoints.languages) {
    url += "&q=" + encodeURI(data.text);
  }

  // If translating, send target and source languages
  if (endpoint === endpoints.translate) {
    url += "&target=" + data.target;
    url += "&source=" + data.source;
  }

  // Return response from API
  return $.ajax({
    url: url,
    type: type || "GET",
    data: data ? JSON.stringify(data) : "",
    dataType: "json",
    async: false,
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    }
  });
}

function translate(text, source, target) {
    res = makeApiRequest(endpoints.translate, {
        'text': text,
        'source': source,
        'target': target
    }, 'GET');

    return res.responseJSON.data.translations[0].translatedText;
}

// Convert country code to country name
function getLanguageNames() {
  return $.getJSON("https://api.myjson.com/bins/155kj1");
}





/*
 * JTip
 * By Cody Lindley (http://www.codylindley.com)
 * Under an Attribution, Share Alike License
 * JTip is built on top of the very light weight jquery library.
 */

//on page load (as soon as its ready) call JT_init
$(document).ready(JT_init);

function JT_init(){
	       $("a.jTip")
		   .hover(function(){JT_show(this.href,this.id,this.name)},function(){$('#JT').remove()})
           .click(function(){return false});	   
}

function JT_show(url,linkId,title){
	if(title == false)title="&nbsp;";
	var de = document.documentElement;
	var w = self.innerWidth || (de&&de.clientWidth) || document.body.clientWidth;
	var hasArea = w - getAbsoluteLeft(linkId);
	var clickElementy = getAbsoluteTop(linkId) - 3; //set y position
	
	var queryString = url.replace(/^[^\?]+\??/,'');
	var params = parseQuery( queryString );
	if(params['width'] === undefined){params['width'] = 250};
	if(params['link'] !== undefined){
	$('#' + linkId).bind('click',function(){window.location = params['link']});
	$('#' + linkId).css('cursor','pointer');
	}
	
	if(hasArea>((params['width']*1)+75)){
		$("body").append("<div id='JT' style='width:"+params['width']*1+"px'><div id='JT_arrow_left'></div><div id='JT_close_left'>"+title+"</div><div id='JT_copy'><div class='JT_loader'><div></div></div>");//right side
		var arrowOffset = getElementWidth(linkId) + 11;
		var clickElementx = getAbsoluteLeft(linkId) + arrowOffset; //set x position
	}else{
		$("body").append("<div id='JT' style='width:"+params['width']*1+"px'><div id='JT_arrow_right' style='left:"+((params['width']*1)+1)+"px'></div><div id='JT_close_right'>"+title+"</div><div id='JT_copy'><div class='JT_loader'><div></div></div>");//left side
		var clickElementx = getAbsoluteLeft(linkId) - ((params['width']*1) + 15); //set x position
	}
	
	$('#JT').css({left: clickElementx+"px", top: clickElementy+"px"});
	$('#JT').show();
	$('#JT_copy').load(url);

}

function getElementWidth(objectId) {
	x = document.getElementById(objectId);
	return x.offsetWidth;
}

function getAbsoluteLeft(objectId) {
	// Get an object left position from the upper left viewport corner
	o = document.getElementById(objectId)
	oLeft = o.offsetLeft            // Get left position from the parent object
	while(o.offsetParent!=null) {   // Parse the parent hierarchy up to the document element
		oParent = o.offsetParent    // Get parent object reference
		oLeft += oParent.offsetLeft // Add parent left position
		o = oParent
	}
	return oLeft
}

function getAbsoluteTop(objectId) {
	// Get an object top position from the upper left viewport corner
	o = document.getElementById(objectId)
	oTop = o.offsetTop            // Get top position from the parent object
	while(o.offsetParent!=null) { // Parse the parent hierarchy up to the document element
		oParent = o.offsetParent  // Get parent object reference
		oTop += oParent.offsetTop // Add parent top position
		o = oParent
	}
	return oTop
}

function parseQuery ( query ) {
   var Params = new Object ();
   if ( ! query ) return Params; // return empty object
   var Pairs = query.split(/[;&]/);
   for ( var i = 0; i < Pairs.length; i++ ) {
      var KeyVal = Pairs[i].split('=');
      if ( ! KeyVal || KeyVal.length != 2 ) continue;
      var key = unescape( KeyVal[0] );
      var val = unescape( KeyVal[1] );
      val = val.replace(/\+/g, ' ');
      Params[key] = val;
   }
   return Params;
}

function blockEvents(evt) {
              if(evt.target){
              evt.preventDefault();
              }else{
              evt.returnValue = false;
              }
}