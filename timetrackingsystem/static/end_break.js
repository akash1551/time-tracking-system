function request_accept(id){ var request_data = id; 
	console.log("end break data: " + id);
	 $.post({ url: "/end/break/", data : 	
		{ attendence_id: request_data}, success :
		function(json) { $("request_accept").hide(); 
		console.log("requested accepted"); } }) 
}
