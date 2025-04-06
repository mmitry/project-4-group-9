$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        predictions();
    });
});


// call Flask API endpoint
function predictions() {
    var unnamed = $("#unnamed").val();
    var paitient_id = $("paitient_id").val();
    var age = $("#age").val();
    var gender = $("#gender").val();
    var ethnicity = $("#ethnicity").val();
    var bmi = $("#bmi").val();
    var smoking = $("#smoking").val();
    var alcohol_consumption = $("#alcohol_consumption").val();
    var physical_activity = $("#physical_activity").val();
    var diet_quality = $("#diet_quality").val();
    var sleep_quality = $("#sleep_quality").val();
    var family_history_alzheimers = $("#family_history_alzheimers").val();
    var cardiovascular_disease = $("#cardiovascular_disease").val();
    var diabetes = $("#diabetes").val();
    var depression = $("#depression").val();
    var head_injury = $("#head_injurye").val();
    var hypertension = $("#hypertension").val();
    var functional_assessment = $("#functional_assessment").val();
    var memory_complaints = $("#memory_complaints").val();
    var behavioral_problems = $("#behavioral_problems").val();
    var confusion = $("#confusion").val();
    var disorientation = $("#disorientation").val();
    var personality_changes = $("#personality_changes").val();
    var difficulty_completing_tasks = $("#difficulty_completing_tasks").val();
    var forgetfulness = $("#forgetfulness").val();


    // create the payload
    var payload = {
        "unnamed": unnamed,
        "patient_id": patient_id,
        "age": age,
        "gender": gender,
        "ethnicity": ethnicity,
        "bmi": bmi,
        "smoking": smoking,
        "alcohol_consumption": alcohol_consumption,
        "physical_activity": physical_activity,
        "diet_quality": diet_quality,
        "sleep_qualtiy": sleep_quality,
        "family_history_alzheimers": family_history_alzheimers,
        "cardiovascular_disease": cardiovascular_disease,
        "diabetes": diabetes,
        "depression": depression,
        "head_injury": head_injury,
        "hypertension": hypertension,
        "functional_assessment": functional_assessment,
        "memory_complaints": memory_complaints,
        "behavioral_problems": behavioral_problems,
        "confusion": confusion,
        "disorientation": disorientation,
        "personality_changes": personality_changes,
        "difficulty_completing_tasks": difficulty_completing_tasks,
        "forgetfulness": forgetfulness

    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/predictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it for debugging
            console.log(returnedData);
            var prob = parseFloat(returnedData["prediction"]);

            if (prob > 0.5) {
                $("#output").text(`The passenger is likely to be satisfied with the flight with a satisfaction rating of ${(prob * 100).toFixed(2)}%!!`);
            } else {
                $("#output").text(`Unfortunately, the passenger is unlikely to be satisfied with the flight with a satisfaction rating of ${(prob * 100).toFixed(2)}%!.`);
            }

            // Call buildDonut function
            buildDonut(prob)

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}

function buildDonut(prob) {
    // Data
    var satis = prob;
    var unsatis = 1 - prob;

    var data = [{
        values: [satis, unsatis],
        labels: ['Satisfied', 'Unsatisfied or Neutral'],
        hole: .5,
        marker: {
            colors: ['#45CAFF', '#FF1B6B']
          },
        textinfo: "label+percent",
        type: 'pie'
    }];
    
    var layout = {
        annotations: [{
            font: { size: 30 },
            showarrow: false,
            text: 'Satisfaction',
            x: 0.5,
            y: 0.5
        }],
        height: 800,
        width: 1200,
        showlegend: false
    };
    
    Plotly.newPlot('donut', data, layout);  
};