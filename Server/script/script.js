document.getElementById("search-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission
    
    var keyword = document.getElementById("keyword").value; // Get keyword from input field

    // Send keyword to gRPC server
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ keyword: keyword })
    })
    .then(response => response.arrayBuffer())
    .then(data => {
        // Convert image data to base64
        var binary = '';
        var bytes = new Uint8Array(data);
        var len = bytes.byteLength;
        for (var i = 0; i < len; i++) {
            binary += String.fromCharCode(bytes[i]);
        }
        var base64Image = window.btoa(binary);

        // Display image on HTML page
        var imageContainer = document.getElementById("image-container");
        imageContainer.innerHTML = '<img src="data:image/jpeg;base64,' + base64Image + '" />';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
