async function getgame(userMove) {
  var result = document.getElementById("result");
  try{
    var response = await fetch("https://rock-paper-scissors-web.onrender.com/Game", {
      method: "POST",
      headers:{
        "Content-Type":"application/json"
      },
      body: JSON.stringify({move:userMove})
    });
    var data = await response.json();

    var gameResult = "<p><strong>Your Move: <strong>" +data.user+ "</p>";
    gameResult+= "<p><strong>Computer Move: <strong>" +data.comp+ "</p>";
    gameResult+= "<p><strong>Result: <strong>" +data.result+ "</p>";
    gameResult+= "<p><strong>Total Wins: <strong>" +data.win+ "</p>";
    gameResult+= "<p><strong>Total Ties: <strong>" +data.tied+ "</p>";
    gameResult+= "<p><strong>Total Lose: <strong>" +data.lose+ "</p>";
    result.innerHTML = gameResult;
  } catch(err){
    console.log("err",err);
  }
}
