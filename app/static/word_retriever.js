function showAnagrams() {
    var word = document.getElementById("word").value;
    if (word == "") {
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
            if (anagrams.length == 0) {
                displayResults('No anagrams for ' + word + '.');
            } else {
                num_anagrams = anagrams.length
                word_for_anagram = (num_anagrams == 1) ? " anagram: " : " anagrams: "
                message = "Found " + num_anagrams + word_for_anagram + getList(anagrams)
                displayResults(message);
            }
        }
    }
}

function getList(array) {
    var listElements = ""
    for (var i = 0; i < array.length; i++) {
        listElements += "<li>" + array[i] + "</li>"
    }
    return "<ul>" + listElements + "</ul>";
}
function displayResults(value) {
    document.getElementById("resulting-anagrams").innerHTML = value

}