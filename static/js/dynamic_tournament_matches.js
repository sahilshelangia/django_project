function dynamicTrournamentMatches(idd,req_color){
	// send ajax request to get all info for that tournament like
		var xhttp = new XMLHttpRequest();
		var formData = new FormData();
		// trn_id is tournament_id for which we want to get info
		formData.append('trn_id',idd);
		formData.append('csrfmiddlewaretoken',CSRF_TOKEN_GLOBAL)
      
		xhttp.onreadystatechange = function() {
			if (this.readyState == 4 && this.status == 200) {
				data = JSON.parse(this.responseText);
				data=JSON.parse(data['trn']);
				data=data[0];
				data=data.fields;
				document.getElementById("tournament_name").innerHTML=data.name;
				var from_date=new Date(data.start_date).toDateString().split(' ');
				from_date=from_date[2]+" "+from_date[1]+" "+from_date[3];
				var to_date=new Date(data.end_date).toDateString().split(' ');
				to_date=to_date[2]+" "+to_date[1]+" "+to_date[3];
				document.getElementById("tournament_matches_and_date").innerHTML=data.cnt_match+" Matches"+"<br>"+from_date+" - "+to_date;
				document.getElementById("tournament_introduction").innerHTML=data.intro;
				document.getElementById("tournament_venue").innerHTML=data.venue;
  	}			              
	};
	xhttp.open("POST", "../detail_tournament", true);
	xhttp.send(formData);


  // now make a ajax request to get match information
  var xhttp = new XMLHttpRequest();
	var formData = new FormData();
	formData.append('trn_id',idd);
	formData.append('csrfmiddlewaretoken',CSRF_TOKEN_GLOBAL)
        
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			data = JSON.parse(this.responseText);
			team_home=data.team_home;
			team_away=data.team_away;
			// match_thumnail=data.match_thumnail;
			// console.log(match_thumnail)
			data=data.matches;
      $('.slider_4').slick('removeSlide', null, null, true);						
			for(i=0;i<data.length;i=i+1){
				match=data[i];

				// DOM for macth grid
				var match_div=document.createElement("DIV");
				match_div.className = "slick-slideshow__slide_4";	

				var linking=document.createElement("A");
				linking.href="../video/"+match.id;

				var images=document.createElement("IMG");
				images.src=match.image;

				// {% static 'img/1554700132_Football.jpg' %};
				linking.appendChild(images);
				match_div.append(linking);

				var bottom=document.createElement("DIV");
				bottom.className="slid_4";

				var team1=document.createElement("H6");
				team1.innerHTML=team_home[i];
				bottom.appendChild(team1);

				var vs=document.createElement("SMALL");
				vs.innerHTML="VS";
				bottom.appendChild(vs);

				var team2=document.createElement("H6");
				team2.innerHTML=team_away[i];
				bottom.appendChild(team2);						

				var para=document.createElement("P");
				var spn=document.createElement("SPAN");
				var res=compareDates(match.start_time,match.end_time);
				if(res==1){
					spn.innerHTML="LIVE";
					spn.className="live";
				}
				else{
					startDate=new Date(match.start_time);
					const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"	];
					spn.innerHTML=startDate.getHours()+":"+startDate.getMinutes()+" ,"+startDate.getDay()+" "+monthNames[startDate.getMonth()]+" "+startDate.getFullYear();
					spn.className="live";
				}

				para.appendChild(spn);
				bottom.appendChild(para);
				var bbc=$('.slider_4').parent().css('border-bottom-color');
				bottom.style.backgroundColor= req_color;
				match_div.append(bottom);								
				$('.slider_4').slick('slickAdd', match_div);
			}							
    }			              
  };
  xhttp.open("POST", "../match_in_tournament", true);
  xhttp.send(formData);
}


function compareDates(start,end){
	start=new Date(start);
	end=new Date(end);
	if(start<=new Date()&&end>=new Date())
		return 1;
	return 0;
}