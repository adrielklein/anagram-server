function showAnagrams() {
    var word = document.getElementById("word").value;
    if (word == ""){
        document.getElementById("resulting-anagrams").innerHTML = "Please enter a word.";
        return;
    }
    var url = "/anagrams/" + word + ".json";

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = processRequest;
    xhr.open("GET", url, true);
    xhr.send();

    function processRequest(e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
        var anagrams = JSON.parse(xhr.responseText)["anagrams"];
        document.getElementById("resulting-anagrams").innerHTML = anagrams;
        }
    }
}