$(document).ready(function() {
    console.log("Page Loaded");
  
    $("#filter").click(function() {
        //alert (button clicked)
        predictions();
    });
  });
  
  
  // call Flask API endpoint
  function predictions() {
    let age = $("#age").val();
    let gender = $("#gender").val();
    let ethnicity = $("#ethnicity").val();
    let bmi = $("#bmi").val();
    let smoking = $("#smoking").val();
    let alcohol_consumption = $("#alcohol_consumption").val();
    let physical_activity = $("#physical_activity").val();
    let diet_quality = $("#diet_quality").val();
    let sleep_quality = $("#sleep_quality").val();
    let family_history_alzheimers = $("#family_history_alzheimers").val();
    let cardiovascular_disease = $("#cardiovascular_disease").val();
    let diabetes = $("#diabetes").val();
    let depression = $("#depression").val();
    let head_injury = $("#head_injury").val();
    let hypertension = $("#hypertension").val();
    let functional_assessment = $("#functional_assessment").val();
    let memory_complaints = $("#memory_complaints").val();
    let behavioral_problems = $("#behavioral_problems").val();
    let confusion = $("#confusion").val();
    let disorientation = $("#disorientation").val();
    let personality_changes = $("#personality_changes").val();
    let difficulty_completing_tasks = $("#difficulty_completing_tasks").val();
    let forgetfulness = $("#forgetfulness").val();
  
  
    // create the payload
    let payload = {
        "age": age,
        "gender": gender,
        "ethnicity": ethnicity,
        "bmi": bmi,
        "smoking": smoking,
        "alcohol_consumption": alcohol_consumption,
        "physical_activity": physical_activity,
        "diet_quality": diet_quality,
        "sleep_quality": sleep_quality,
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
            let prob = parseFloat(returnedData["predictions"]);
  
            if (prob < 0.5) {
                $("#output").text(`The user is not likely to be impacted by Alzheimers ${(prob * 100).toFixed(2)}%!!`);
            } else {
                $("#output").text(`Unfortunately, the user is likely to experience symptoms related to Alzheimers ${(prob * 100).toFixed(2)}%!.`);
            }
        }
    })}