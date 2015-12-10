$(document).ready(function()
	{
        var user_main = document.getElementsByClassName("user_main");
        var user_popup = document.getElementsByClassName("user_popup");
        user_main.onmouseover=function(){
            user_popup.visibility="visible";
        }
	}	
);

function show_popup () {
    var user_popup = document.getElementsByClassName("user_popup");
    user_popup.visibility="visible";    
}