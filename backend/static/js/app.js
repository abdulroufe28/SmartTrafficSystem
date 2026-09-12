/* ================= LOGIN ================= */

function login(event){

    event.preventDefault();

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;

    if(username === "admin" &&
       password === "admin123"){

        window.location.href = "/dashboard";

    }else{

        alert("Invalid Username or Password");

    }

}

/* ================= SIDEBAR NAVIGATION ================= */

function goDashboard(){

    window.location.href = "/dashboard";

}

function goAnalytics(){

    window.location.href = "/analytics";

}

function goEmergency(){

    window.location.href = "/emergency";

}

/* ================= BAR CHART ================= */

const barChart =
    document.getElementById("barChart");

if(barChart){

    new Chart(barChart,{

        type:"bar",

        data:{
            labels:[
                "Junction A",
                "Junction B",
                "Junction C",
                "Junction D"
            ],

            datasets:[{

                label:"Vehicle Count",

                data:[110,180,90,140],

                backgroundColor:[
                    "#2563eb",
                    "#16a34a",
                    "#f97316",
                    "#7c3aed"
                ]

            }]
        },

        options:{
            responsive:true
        }

    });

}

/* ================= PIE CHART ================= */

const pieChart =
    document.getElementById("pieChart");

if(pieChart){

    new Chart(pieChart,{

        type:"pie",

        data:{

            labels:[
                "Cars",
                "Buses",
                "Trucks",
                "Motorcycles"
            ],

            datasets:[{

                data:[30,5,8,6],

                backgroundColor:[
                    "#2563eb",
                    "#16a34a",
                    "#f97316",
                    "#7c3aed"
                ]

            }]
        }

    });


}

async function loadTrafficData() {

    try {

        const response = await fetch("/traffic_data");

        const data = await response.json();

        // VEHICLE COUNT
        document.getElementById("vehicle-count").innerText =
            data.vehicle_count;

        // TRAFFIC DENSITY
        document.getElementById("traffic-density").innerText =
            data.traffic_density;

        // EMERGENCY STATUS
        document.getElementById("emergency-count").innerText =
            data.emergency_status;

        // SIGNAL TIME
        document.getElementById("signal-time").innerText =
            data.signal_time + " sec";

    } catch(error) {

        console.log(error);

    }
}

loadTrafficData();

setInterval(loadTrafficData, 2000);