// function used for changing the change in account section
function changeNameAjax(first_name,last_name){
	var xhttp = new XMLHttpRequest();
	var formData = new FormData();
	formData.append('first_name',first_name);
	formData.append('last_name',last_name);
	formData.append('csrfmiddlewaretoken',CSRF_TOKEN_GLOBAL);

	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			data = JSON.parse(this.responseText);
			document.getElementById('account').innerHTML=first_name;
			document.getElementById('fullName').innerHTML=first_name+" "+last_name;
			document.getElementById('top_first_name').innerHTML=first_name;
			document.getElementById('top_last_name').innerHTML=last_name;
		}
	};
	xhttp.open("POST", "../updateName", true);
	xhttp.send(formData);
}


// function that sends the mail to verify
// when user press verify email button
function verifyEmailAjax(){	
	document.getElementById('emailSent').innerHTML="Email sent, please verify!";
	var xhttp = new XMLHttpRequest();
	var formData = new FormData();
	formData.append('csrfmiddlewaretoken',CSRF_TOKEN_GLOBAL);
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			data = JSON.parse(this.responseText);
		}
	};
	xhttp.open("POST", "../email-verify", true);
	xhttp.send(formData);
}

// this is first time when user change the mail and just press save
function changeEmailAjax(){
	if(verifyButton==false){
		// addVerifyButton like <button id="verifyEmail" onclick="verifyEmailAjax()">Verifiy</button>
		var btn = document.createElement("BUTTON");   // Create a <button> element
		btn.innerHTML = "verify"; 
		btn.id="verifyEmail" ;                 // Insert text
		btn.setAttribute('onclick','verifyEmailAjax()');
		document.getElementById('addVerifyButton').appendChild(btn);
		verifyButton=true;
		// when user press button he/she will get mail regaring to cnf mail
	}	   	

	var xhttp = new XMLHttpRequest();
	var formData = new FormData();
	document.getElementById('emailWithoutEdit').innerHTML=document.getElementById('eEmail').value;
	formData.append('email',document.getElementById('eEmail').value);
	formData.append('csrfmiddlewaretoken',CSRF_TOKEN_GLOBAL);
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
		data = JSON.parse(this.responseText);
		document.getElementById('emailWithoutEdit').innerHTML=document.getElementById('eEmail').value;
		}
	};
  xhttp.open("POST", "../updateEmail", true);
  xhttp.send(formData);
}


// initialize Account Kit with CSRF protection
AccountKit_OnInteractive = function(){
  AccountKit.init(
    {
        appId:FACEBOOK_APP_ID_GLOBAL, 
        state:CSRF_TOKEN_GLOBAL, 
        version:ACCOUNT_KIT_API_VERSION_GLOBAL,
        fbAppEventsEnabled:true,
        debug:true,
    }
  );
}; 

// function used to verify phone number after you enter the otp      
function loginCallback(response) {
	if (response.status === "PARTIALLY_AUTHENTICATED") {
		var code = response.code;
		var xhttp = new XMLHttpRequest();
		var formData = new FormData();
		formData.append('accountkit_data',code);
		formData.append('csrfmiddlewaretoken',CSRF_TOKEN_GLOBAL);

		xhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				data = JSON.parse(this.responseText);
				// replace content of old phone number with updated phone number
				document.getElementById('oldPhone').innerHTML=document.getElementById('sel').options[document.getElementById('sel').selectedIndex].value+document.getElementById('eNumber').value;
			}
		};
		xhttp.open("POST", "../updatePhone", true);
		xhttp.send(formData);
	}
	else if (response.status === "NOT_AUTHENTICATED") {
		// handle authentication failure
		alert("Not auhtenticated");
		console.log(response);
	}
	else if (response.status === "BAD_PARAMS") {
		// handle bad parameters
		console.log(response);
	}
}

// this function receive country code and phone number
// when user clicks the save button on change phone number
function changePhoneAjax(country_code,phone_number){
	//send otp to that number and verify in loginCallback function
	AccountKit.login(
        'PHONE',
        {countryCode: country_code, phoneNumber: phone_number},
        loginCallback
      );
}	