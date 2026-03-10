const form = document.getElementById("uploadForm");

if(form){

form.addEventListener("submit", async (e) => {

e.preventDefault();

const status = document.getElementById("status");

status.innerText = "Analyzing...";

const fileInput = document.getElementById("logfile");

const formData = new FormData();

formData.append("logfile", fileInput.files[0]);

const res = await fetch("/analyze",{

method:"POST",

body:formData

});

const data = await res.json();

localStorage.setItem("analysis", JSON.stringify(data));

status.innerText = "Analysis complete";

});

}


window.onload = () => {

const data = JSON.parse(localStorage.getItem("analysis"));

if(!data) return;

if(document.getElementById("metrics"))
document.getElementById("metrics").innerText = JSON.stringify(data.stats,null,2);

if(document.getElementById("explanation"))
document.getElementById("explanation").innerText = data.explanation;

if(document.getElementById("alert"))
document.getElementById("alert").innerText = JSON.stringify(data.alert,null,2);

if(document.getElementById("riskChart")){

const ctx = document.getElementById("riskChart").getContext("2d");

new Chart(ctx,{

type:"bar",

data:{

labels:["Risk Score"],

datasets:[{

label:"System Risk",

data:[data.summary.risk_score]

}]

}

});

}

};