
async function getCoderData() {
    try {
        // Fetch the GitHub user data
        var response = await fetch("https://api.github.com/users/adion81");
        
        // Convert the data into JSON format
        var coderData = await response.json();
        
        // Get the user div element
        var plot_user = document.getElementById('user');
        
        // Create HTML content with the user data
        var htmlContent = '<p>' + coderData.name + ' has ' + coderData.followers + ' followers</p><br>';
        htmlContent += '<img src="' + coderData.avatar_url + '" alt="User Avatar" style="width:100px;height:100px;">';
        
        // Insert the HTML content into the user div
        plot_user.innerHTML = htmlContent;
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}