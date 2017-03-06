function request_access(id){  var request_data = id;
	console.log("start break data: " + request_data);
	 $.post({ url: "/start/break/", data : 	
		{ attendance_id: id}, success :
		function(json) { $("#request-access").hide(); 
		console.log("requested access complete"); } }) 
}

