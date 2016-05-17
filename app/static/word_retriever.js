function showAnagrams() {
    var word = document.getElementById("word").value;
    if (word == ""){
        displayResults('Please enter a word.');
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
        if (anagrams.length == 0){
            displayResults('No anagrams for ' + word + '.');
        } else {
            displayResults('Anagrams: ' + anagrams);
        }
        }
    }
}

function displayResults(value){
    document.getElementById("resulting-anagrams").innerHTML = value

}